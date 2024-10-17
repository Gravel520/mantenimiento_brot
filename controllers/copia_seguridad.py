'''
Script en Python.
Contiene las funciones para hacer la copia de seguridad de toda
    la base de datos.

Utilizamos el archivo exe que proporciona 'xampp' para realizar copias de la base de datos entera.
El nombre del archivo resultante, lo forma la palabra 'copia_', seguda de la fecha actual en la 
    que se crea la misma.
    Para realizarla primero comprobamos que no haya ninguna copia de el día en el que se quiere
    realizar, si existe se preguntará si queremos sobreescribirla o no.

Necesitamos la ruta de los directorios donde se crearán la copia de segudidad al instalar el programa.
Sería recomendable poder definir esta ruta nosotros mismos y guardarla en un archivo de texto, ya que
    esta ruta podría variar de una instalación a otra.
Del mismo modo sería recomendable hacerlo también con el programa 'Xampp'.

El módulo 'os' nos servirá para ejecutar el archivo 'exe', que realiza la copia de seguridad completa.
    También para buscar el archivo en la ruta expecificada, y poder, en su caso sobreescribirlo.
'''

import os 
from PySide6.QtWidgets import QMessageBox
from datetime import datetime # Módulo para obtener la fecha actual
from controllers.DATOS import cargar_variables

# Función para crear una copia de seguridad en formato sql
#   de toda la base de datos. Self para que herede las características
#   del formulario principal.
def copia_seguridad(self):
    RUTA_COPIA, RUTA_DUMP = cargar_variables()
    copia = False
    fecha = datetime.today().strftime('%d-%m-%Y') # Creamos el nombre de la fecha con el formado (dd-mm-aa)
    filepath = buscar_archivo(f'copia_{fecha}.sql', RUTA_COPIA) # Comprobamos si el archivo existe en la ruta indicada

    if  filepath == False: # Si el archivo NO existe, se hace la copia automáticamente
        copia = crear_copia(self, RUTA_COPIA, RUTA_DUMP, fecha)
        return copia

    else: # Si el archivo SI existe, preguntamos si queremos sobreescribir el archivo. Si es así se crea de nuevo la copia
        msg = QMessageBox(self)
        msg.setWindowTitle('El archivo ya existe')
        msg.setText('¿Quiere sobreescribirlo?')
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        res = msg.exec_()

        if res == QMessageBox.Ok:
            copia = crear_copia(self, RUTA_COPIA, RUTA_DUMP, fecha)
            return copia
        
        else:
            return copia

# Función para buscar un arcivo concreto en una ruta concreta.
def buscar_archivo(name, path):
    for dirPath, dirName, filename in os.walk(path):
        if name in filename:
            return True
        else:
            return False
        
# Función para crear la copia de seguridad utilizando el código que nos proporciona 'xampp'
def crear_copia(self, ruta_copia, ruta_dump, fecha):
    try:
        proceso = f'{ruta_dump}/mysqldump --user="root" --password= bdbrot > {ruta_copia}/copia_{fecha}.sql'
        os.popen(proceso)
        size = os.path.getsize(f'{ruta_copia}/copia_{fecha}.sql')
        if  size == 0:
            return False
        else:
            return True

    except:
        return False
