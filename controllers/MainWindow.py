'''
Script en Python
'''

from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QThread, Signal
from PySide6.QtCore import QDate
import time
from bd_mysql.connection import create_connection
from controllers.copia_seguridad import copia_seguridad
from controllers.copia_selectiva import obtener_id, borrar_datos, obtener_registros
from controllers.liberacion import obtener_id_liberacion, borrar_registros, borrar_id_liberacion
from controllers.cargar_copia import cargar_copia
from controllers.DATOS import *
from views.frm_mantenimiento import Dialog

class Mantenimiento(QMainWindow, Dialog):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Mantenimiento')        
        self.setToday() # Obtenemos el día actual       

        global RUTA_COPIA
        global RUTA_DUMP
        RUTA_COPIA, RUTA_DUMP = cargar_variables()
        self.meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.pb_copia_seguridad.setValue(0)
        self.pb_copia_selectiva.setValue(0)
        self.pb_liberacion.setValue(0)
        self.config()
        self.tabWidget.setCurrentIndex(4)
        self.tab = 0
        self.last_tab = 4

        # Crear el hilo para la copia
        self.backup_thread = BackupThread()
        # Conectar la señal de progreso con el método para actualizar la barra
        self.backup_thread.progress.connect(self.update_progress)

        self.sings_controls()

    def copia_seguridad(self): # **************************************************************
        # Creamos una variable que nos retorne 'True' o 'False' en caso de que haga o no la copia
        #   de seguridad, ya sea por algún error o porque ya exista dicha copia, lanzando así la barra de proceso
        copiar = copia_seguridad(self)

        if copiar == True:
            self.start_backup() 
            msg = QMessageBox.information(self, 'Copia de Seguridad', 'Proceso completado...')
        else:
            msg = QMessageBox.information(self, 'Error en la Copia', 'Proceso NO completado...')

    def copia_selectiva(self): # ***************************************************************
       # Definimos el valor de la variable para borrar o no los registros
        if self.cb_borrar_seleccion.isChecked(): borrar = 'Yes'
        else: borrar = 'None'

        if self.rd_fechas.isChecked():
            fecha_inicio = self.de_fecha_incial.date().toPython()
            fecha_final = self.de_fecha_final.date().toPython()
            mes = None
            ano = None

        else:
            fecha_inicio = None
            fecha_final = None
            mes = self.cb_mes.currentIndex() + 1
            ano = self.cb_ano.currentText()

        id_copia = obtener_id(self, fecha_inicio, fecha_final, mes, ano)
        
        if len(id_copia) == 0:
            msg = QMessageBox.information(self, 'Error en la copia', 'No hay registros en el periodo especificado.')

        else:
            self.start_backup()
            obtener_registros(self, id_copia)            
            if borrar == 'Yes':
                borrar_datos(self, id_copia)
        
    def liberacion(self):      # ****************************************************************
        msg = QMessageBox.question(self, 'No se podrán recuperar los datos', '¿Desea continuar con la liberación?')
        if msg == QMessageBox.Yes:
            self.liberar()

    def cargar_copia(self):    # ****************************************************************
        msg = QMessageBox.question(self, 'Cargar copia', 'Se perderán los datos actuales\n¿Desea continuar con la carga?')
        if msg == QMessageBox.Yes:
            msg = QMessageBox.information(self, 'Tiempo de espera', 'Este proceso puede tardar varios minutos.\nPor favor, espere...')

            # Obtenemos los datos del nombre del archivo y el tipo de archivo
            file = self.btn_seleccionar_archivo.text()
            tipo = file[-3:] # Los tres últimos caracteres nos dicen el tipo de archivo
            
            self.setEnabled(False)
            # Ejecutamos la función
            cargar = cargar_copia(self, file, tipo)
            print(f'Main cargar copia. Estado de cargar: {cargar}')
            if cargar == True:
                msg = QMessageBox.information(self, 'Carga Completa', 'Proceso finalizado...')            
            else:
                msg = QMessageBox.information(self, 'Error en la Copia', 'Proceso NO completado...')
            self.setEnabled(True)

# **************** Copia Selectiva ****************************************
    def inicio_pestaña_1(self, today):
        self.btn_aceptar_co_selec.setEnabled(True)
        self.rd_fechas.setChecked(True)
        self.de_fecha_incial.calendarWidget().setSelectedDate(today)
        self.de_fecha_final.calendarWidget().setSelectedDate(today) 
        self.cb_borrar_seleccion.setChecked(False)           
        self.populate_combobox_1()
        self.cambia_opcion_1()
    
    def cambia_opcion_1(self):
        if self.rd_fechas.isChecked():
            self.cb_ano.setEnabled(False)
            self.cb_mes.setEnabled(False)
            self.de_fecha_incial.setEnabled(True)
            self.de_fecha_final.setEnabled(True)

        elif self.rd_mes.isChecked():
            self.de_fecha_incial.setEnabled(False)
            self.de_fecha_final.setEnabled(False)
            self.cb_mes.setEnabled(True)
            self.cb_ano.setEnabled(True)

    # Rellenamos los combo con los meses y los años, y dejamos seleccionado
    #   los datos que corresponden con la fecha actual
    def populate_combobox_1(self):
        for mes in self.meses:
            self.cb_mes.addItem(mes)
        self.cb_mes.setCurrentIndex((self.today.month() - 1))

        # Añadimos el rango de años correspondiente a 5 años menos y 5 mas
        #   del año actual
        ano_actual = self.today.year()
        for ano in range((ano_actual - 5), (ano_actual + 5)):
            self.cb_ano.addItem(str(ano))
        self.cb_ano.setCurrentText(str(ano_actual))

# ************************* Liberación ***************************************
    def liberar(self):
        fecha_final = self.de_fecha_lib.date().toPython()
        records = obtener_id_liberacion(self, fecha_final)
        if len(records) > 0:
            self.start_backup()
            borrar_registros(self, records)
            borrar_id_liberacion(self, fecha_final)

        else:
            msg = QMessageBox.information(self, 'Liberación', 'No hay datos para liberar.')

# ************************* Cargar Copia *************************************            
    # Rellenamos el combo con las opciones de tipos de archivo para la carga de
    #   datos; sql, o json. Deshabilitar el botón de carga de archivo hasta que 
    #   seleccionemos un archivo.
    def populate_combobox_3(self):
        self.cb_tipo_archivo.clear()
        self.cb_tipo_archivo.addItem("Sql")
        self.cb_tipo_archivo.addItem("Json")

        self.btn_cargar_archivo.setEnabled(False)

    def select_file(self):
        opcion = self.cb_tipo_archivo.currentText() # Definimos la variable con el tipo de documento
        # Abrimos el cuadro de diálogo para seleccionar el archivo
        file_path, _ = QFileDialog.getOpenFileName(self, 'Abrir Copia',RUTA_COPIA,f'*.{opcion}')
        
        '''
        Primero creamos una tupla con los valores que están entre la barra diagonal (/).
        Después obtenemos el número de elementos que compone la tupla.
            Si el número es 1, esta vacío.  Deshabilitamos el botón de carga.
                                            Rellenamos el texto del botón.
            Si el número es otro, esta lleno.   Habilitamos el botón de carga.
                                                Obtenemos el elemento más a la derecha de la tupla,
                                                    el nombre del archivo.
        '''
        try:
            file_name = file_path.split("/")
            n = len(file_name)

            if n == 1: 
                self.btn_cargar_archivo.setEnabled(False)
                self.btn_seleccionar_archivo.setText('Seleccionar archivo')
            else:
                self.btn_cargar_archivo.setEnabled(True)
                self.btn_seleccionar_archivo.setText(str(file_name[n-1]))

        except:
            self.btn_seleccionar_archivo.setText('Seleccionar archivo')

    # ************************* Configuración *************************************            
    # Esta función es la primera que se ejecuta en la aplicación, en ella comprobamos
    #   si hay o no conexión con la base de datos, para avisar al usuario. Además 
    #   establecemos en los cuadros de texto las rutas de los directorios de las copias,
    #   y de los exe para realizar la copia y restauración de la base completa.
    def config(self):
        conn = create_connection(self)

        self.lineEdit_copia.setText(RUTA_COPIA)
        self.lineEdit_mysql.setText(RUTA_DUMP)

    # Esta función nos servirá para seleccionar el directorio donde queremos guardar
    #   nuestras copias de seguridad.
    def select_url_copia(self):
        options = QFileDialog.Options()
        directory_url = QFileDialog.getExistingDirectoryUrl(self, 'Seleccionar directorio para la copia de seguridad', options=options)
        if directory_url.isValid():
            self.lineEdit_copia.setText(directory_url.toLocalFile())

    # Con esta función elegimos el directorio donde tenemos instalado el 'xamp' y en 
    #   concreto los exe de 'mysqldump' y 'mysql', para hacer y restablecer las copias.
    def select_url_mysql(self):
        options = QFileDialog.Options()
        directory_url = QFileDialog.getExistingDirectoryUrl(self, 'Seleccionar directorio para el archivo mysql', options=options)
        if directory_url.isValid():
            self.lineEdit_mysql.setText(directory_url.toLocalFile())

    # *****************************************************************************            

    def start_backup(self):
        # Iniciar el hilo
        self.backup_thread.start()

    def update_progress(self, value):
        # Actualizar el valor de la barra de progreso
        if self.tab == 0:
            self.pb_copia_seguridad.setValue(value)

        elif self.tab == 1:
            self.pb_copia_selectiva.setValue(value)

        elif self.tab == 2:
            self.pb_liberacion.setValue(value)

    '''
    Esta función es llamada cuando cambiamos de pestaña, ejecutando el código
        que corresponde a cada una.
        Lo primero que hacemos es comprobar que la pestaña de la que venimos sea
            la de 'configuración', porque de ser así, automáticamente escribremos
            en el archivo de variables el contenido de las cajas de texto.
    '''
    def pestana(self, value):
        self.tab = value
        if self.last_tab == 4:
            grabar_variables(self.lineEdit_copia.text(), self.lineEdit_mysql.text())

        if self.tab == 1:
            self.last_tab = 0
            self.inicio_pestaña_1(self.today)

        elif self.tab == 2:
            self.last_tab = 0            
            self.de_fecha_lib.calendarWidget().setSelectedDate(self.today)

        elif self.tab == 3:
            self.last_tab = 0            
            self.populate_combobox_3()

        elif self.tab == 4:
            self.last_tab = 4
            self.config()

    def setToday(self):
        self.today = QDate().currentDate()

    def sings_controls(self):
        self.tabWidget.currentChanged.connect(self.pestana)
        self.btn_aceptar_co_seg.clicked.connect(self.copia_seguridad)
        self.rd_fechas.clicked.connect(self.cambia_opcion_1)
        self.rd_mes.clicked.connect(self.cambia_opcion_1)
        self.btn_aceptar_co_selec.clicked.connect(self.copia_selectiva)
        self.btn_aceptar_liberacion.clicked.connect(self.liberacion)
        self.btn_seleccionar_archivo.clicked.connect(self.select_file)
        self.btn_cargar_archivo.clicked.connect(self.cargar_copia)
        self.btn_ubica_copia.clicked.connect(self.select_url_copia)
        self.btn_ubica_mysql.clicked.connect(self.select_url_mysql)
        self.btn_salir.clicked.connect(lambda: self.close())

class BackupThread(QThread):
    # Senal que emite el porcentaje de progreso
    progress = Signal(int)

    def run(self):
        # Similar la copia
        for i in range(50):
            # Esperar un segundo
            time.sleep(0.1)
            # Emitir el porcentaje de progreso
            self.progress.emit((i + 1) * 2)