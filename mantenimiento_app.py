'''
Script en Python. Este script servirá de apoyo a la aplicación 'KtBrot' para
hacer copias de seguridad y gestionar los archivos creados.

Para hacer la restauración de la copia a la base mysql:
mysql --user=****** --password=****** db_nom < /Ruta/Hacia/archivo_dump.SQL
proceso = f'{ruta_dump}/mysql --user="root" --password= bdbrot < {ruta_copia}\copia.sql'

Convertir archivo ui a py, y grabarlo después a UTF-8:
pyside6-uic nombre.ui > nombre.py

convertir archivo de recursos qrc a py, y grabarlo después UTF-8:
pyside6-rcc nombre.qrc > nombre.py (hay que moverlo al directorio raiz de la aplicación)

'''

import sys
from PySide6.QtWidgets import QApplication
from controllers.MainWindow import Mantenimiento

if __name__ == '__main__':
    app = QApplication()
    window = Mantenimiento()
    window.show()

    sys.exit(app.exec())