# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_mantenimiento.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDialog, QLabel, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QWidget)
import recursos

class Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 354)
        Dialog.setStyleSheet(u"background-image:url(:/Fondo/Fondo.png);")
        Dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 481, 291))
        self.tab_copia_seguridad = QWidget()
        self.tab_copia_seguridad.setObjectName(u"tab_copia_seguridad")
        self.tab_copia_seguridad.setAutoFillBackground(False)
        self.label = QLabel(self.tab_copia_seguridad)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 411, 121))
        self.label.setLineWidth(4)
        self.pb_copia_seguridad = QProgressBar(self.tab_copia_seguridad)
        self.pb_copia_seguridad.setObjectName(u"pb_copia_seguridad")
        self.pb_copia_seguridad.setGeometry(QRect(20, 140, 451, 23))
        self.pb_copia_seguridad.setValue(24)
        self.btn_aceptar_co_seg = QPushButton(self.tab_copia_seguridad)
        self.btn_aceptar_co_seg.setObjectName(u"btn_aceptar_co_seg")
        self.btn_aceptar_co_seg.setGeometry(QRect(350, 190, 75, 23))
        self.btn_aceptar_co_seg.setAutoFillBackground(False)
        self.tabWidget.addTab(self.tab_copia_seguridad, "")
        self.tab_copia_selectiva = QWidget()
        self.tab_copia_selectiva.setObjectName(u"tab_copia_selectiva")
        self.label_3 = QLabel(self.tab_copia_selectiva)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, -1, 461, 101))
        self.label_3.setLineWidth(4)
        self.pb_copia_selectiva = QProgressBar(self.tab_copia_selectiva)
        self.pb_copia_selectiva.setObjectName(u"pb_copia_selectiva")
        self.pb_copia_selectiva.setGeometry(QRect(20, 200, 451, 23))
        self.pb_copia_selectiva.setValue(24)
        self.btn_aceptar_co_selec = QPushButton(self.tab_copia_selectiva)
        self.btn_aceptar_co_selec.setObjectName(u"btn_aceptar_co_selec")
        self.btn_aceptar_co_selec.setGeometry(QRect(360, 230, 75, 23))
        self.label_4 = QLabel(self.tab_copia_selectiva)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(157, 100, 70, 13))
        self.label_5 = QLabel(self.tab_copia_selectiva)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(347, 100, 60, 13))
        self.label_6 = QLabel(self.tab_copia_selectiva)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(108, 166, 30, 13))
        self.label_7 = QLabel(self.tab_copia_selectiva)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(337, 166, 30, 13))
        self.cb_borrar_seleccion = QCheckBox(self.tab_copia_selectiva)
        self.cb_borrar_seleccion.setObjectName(u"cb_borrar_seleccion")
        self.cb_borrar_seleccion.setGeometry(QRect(150, 230, 111, 17))
        self.de_fecha_incial = QDateEdit(self.tab_copia_selectiva)
        self.de_fecha_incial.setObjectName(u"de_fecha_incial")
        self.de_fecha_incial.setGeometry(QRect(137, 120, 110, 22))
        self.de_fecha_incial.setCalendarPopup(True)
        self.de_fecha_final = QDateEdit(self.tab_copia_selectiva)
        self.de_fecha_final.setObjectName(u"de_fecha_final")
        self.de_fecha_final.setGeometry(QRect(327, 120, 110, 22))
        self.de_fecha_final.setCalendarPopup(True)
        self.cb_mes = QComboBox(self.tab_copia_selectiva)
        self.cb_mes.setObjectName(u"cb_mes")
        self.cb_mes.setGeometry(QRect(137, 160, 111, 22))
        self.cb_ano = QComboBox(self.tab_copia_selectiva)
        self.cb_ano.setObjectName(u"cb_ano")
        self.cb_ano.setGeometry(QRect(367, 160, 69, 22))
        self.rd_fechas = QRadioButton(self.tab_copia_selectiva)
        self.rd_fechas.setObjectName(u"rd_fechas")
        self.rd_fechas.setGeometry(QRect(70, 120, 31, 17))
        self.rd_mes = QRadioButton(self.tab_copia_selectiva)
        self.rd_mes.setObjectName(u"rd_mes")
        self.rd_mes.setGeometry(QRect(70, 160, 31, 17))
        self.tabWidget.addTab(self.tab_copia_selectiva, "")
        self.tab_liberacion = QWidget()
        self.tab_liberacion.setObjectName(u"tab_liberacion")
        self.label_2 = QLabel(self.tab_liberacion)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 451, 121))
        self.label_2.setLineWidth(4)
        self.pb_liberacion = QProgressBar(self.tab_liberacion)
        self.pb_liberacion.setObjectName(u"pb_liberacion")
        self.pb_liberacion.setGeometry(QRect(20, 190, 451, 23))
        self.pb_liberacion.setValue(24)
        self.btn_aceptar_liberacion = QPushButton(self.tab_liberacion)
        self.btn_aceptar_liberacion.setObjectName(u"btn_aceptar_liberacion")
        self.btn_aceptar_liberacion.setGeometry(QRect(350, 220, 75, 23))
        self.de_fecha_lib = QDateEdit(self.tab_liberacion)
        self.de_fecha_lib.setObjectName(u"de_fecha_lib")
        self.de_fecha_lib.setGeometry(QRect(60, 140, 110, 22))
        self.de_fecha_lib.setCalendarPopup(True)
        self.label_8 = QLabel(self.tab_liberacion)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(19, 145, 40, 13))
        self.tabWidget.addTab(self.tab_liberacion, "")
        self.tab_cargar_copia = QWidget()
        self.tab_cargar_copia.setObjectName(u"tab_cargar_copia")
        self.label_9 = QLabel(self.tab_cargar_copia)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 451, 121))
        self.label_9.setLineWidth(4)
        '''
        self.pb_cargar_copia = QProgressBar(self.tab_cargar_copia)
        self.pb_cargar_copia.setObjectName(u"pb_cargar_copia")
        self.pb_cargar_copia.setGeometry(QRect(20, 190, 451, 23))
        self.pb_cargar_copia.setValue(24)
        '''
        self.label_10 = QLabel(self.tab_cargar_copia)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(300, 130, 115, 13))
        self.btn_seleccionar_archivo = QPushButton(self.tab_cargar_copia)
        self.btn_seleccionar_archivo.setObjectName(u"btn_seleccionar_archivo")
        self.btn_seleccionar_archivo.setGeometry(QRect(270, 150, 160, 23))
        self.btn_cargar_archivo = QPushButton(self.tab_cargar_copia)
        self.btn_cargar_archivo.setObjectName(u"btn_cargar_archivo")
        self.btn_cargar_archivo.setGeometry(QRect(330, 220, 90, 23))
        self.label_11 = QLabel(self.tab_cargar_copia)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 130, 100, 13))
        self.cb_tipo_archivo = QComboBox(self.tab_cargar_copia)
        self.cb_tipo_archivo.setObjectName(u"cb_tipo_archivo")
        self.cb_tipo_archivo.setGeometry(QRect(66, 150, 91, 22))
        self.tabWidget.addTab(self.tab_cargar_copia, "")
        self.btn_salir = QPushButton(Dialog)
        self.btn_salir.setObjectName(u"btn_salir")
        self.btn_salir.setGeometry(QRect(10, 320, 75, 23))

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Con esta opci\u00f3n creamos una copia de seguridad de la base de datos en este<br> preciso momento. Posteriormente podremos recuperarlausando la opci\u00f3n<br> &quot;Cargar Copia&quot;</p></body></html>", None))
        self.btn_aceptar_co_seg.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_copia_seguridad), QCoreApplication.translate("Dialog", u"Copia de Seguridad", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Con esta opci\u00f3n creamos una copia de seguridad de la base de datos, pero<br> de forma selectiva. Podremos fijar la fecha inicial y final, para definir el<br> intervalo de registros que queremos copiar. Otra forma ser\u00eda indicando el<br> mes y el a\u00f1o a realizar la copia. Tenemos la opci\u00f3n de borrar esos datos de la<br> base de datos si de momento no los necesitamos. Posteriormente  podremos<br>                     recuperarla usando la opci\u00f3n &quot;Cargar Copia&quot;</p></body></html>", None))
        self.btn_aceptar_co_selec.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Fecha Inicial", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Fecha Final", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Mes:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"A\u00f1o:", None))
        self.cb_borrar_seleccion.setText(QCoreApplication.translate("Dialog", u"Borrar Selecci\u00f3n", None))
        self.rd_fechas.setText("")
        self.rd_mes.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_copia_selectiva), QCoreApplication.translate("Dialog", u"Copia Selectiva", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Esta opci\u00f3n nos servir\u00e1 para borrar parte del contenido de nuestra<br/>base de datos que ya no nos sea util. Para ello bastar\u00e1 con elegir<br/>la fecha hasta donde queramos borrar los datos. Estos datos<br/>no ser\u00e1n recuperables.</span></p></body></html>", None))
        self.btn_aceptar_liberacion.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Fecha:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_liberacion), QCoreApplication.translate("Dialog", u"Liberaci\u00f3n", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Con esta opci\u00f3n recuperamos, parte o toda la base de datos, que<br/>hayamos copiado anteriormente. Bastar\u00e1 con elegir el archivo que se genera<br/>al hacer la copia, y esta se restaurar\u00e1.</p><p align=\"center\"><span style=\" font-weight:600;\">Al cargar el archivo, el contenido de la base de datos, actual, se perder\u00e1, con<br/>lo cual, para mantenerlo, ser\u00eda necesario hacer una 'Copia de Seguridad'.</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Nombre del archivo:", None))
        self.btn_seleccionar_archivo.setText(QCoreApplication.translate("Dialog", u"Seleccionar archivo", None))
        self.btn_cargar_archivo.setText(QCoreApplication.translate("Dialog", u"Cargar archivo", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Tipo de archivo:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cargar_copia), QCoreApplication.translate("Dialog", u"Cargar Copia", None))
        self.btn_salir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
    # retranslateUi

