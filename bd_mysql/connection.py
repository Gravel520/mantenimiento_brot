'''
Script en Python.
Contiene la función para conectarnos con la base de datos mysql
'''

from mysql import connector
from PySide6.QtWidgets import QMessageBox

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'bdbrot'
}

def create_connection(self):
    conn = None
    try:
        conn = connector.connect(**config)

    except:
        msg = QMessageBox.critical(self, 'Base de datos', 'Error al conectar con la base de\ndatos, compruebe conexión.')

    return conn