'''
Script en Python donde vamos a controlar todas la funciones de la
    carga de una copia, ya sea mediante archivo '.json' ó '.sql'.
    Si fuese un archivo '.json', sería una copia de un mes y año en concreto, 
        o del período entre dos fechas.
    Si fuese un archivo '.sql', sería una copia completa de toda la
        base de datos.
'''

from PySide6.QtWidgets import QMessageBox
import json
import os
from bd_mysql.connection import create_connection
from controllers.DATOS import *

# Función para desviar el flujo a la carga completa o parcial
def cargar_copia(self, file, tipo):
    global RUTA_COPIA
    global RUTA_DUMP
    RUTA_COPIA, RUTA_DUMP = cargar_variables() # Cargamos las variables del fichero
    if tipo == 'sql': # Carga completa
        carga = carga_completa(self, file)
        return carga

    else: # Carga parcial, primero tenemos que borrar los datos de las tablas
        carga = borrado_base_datos(self)
        if carga == True:
            carga_parcial(self, file)
            return carga
        else:
            return carga

# Función para cargar un archivo sql. Lo primero que hacemos es comprobar que
#   el archivo que queremos cargar tiene información, es decir, el tamaño mayor a 0
def carga_completa(self, file):
    size = os.path.getsize(f'{RUTA_COPIA}/{file}')
    if size == 0:
        return False
    else:
        try: # Es necesario para poder crear una conexión
            # Comprobamos si hay conexión con la base de datos para continuar con el
            #   proceso o abortarlo
            conn = create_connection(self)
            if conn:
                # Cargamos el fichero elegido
                proceso = f'{RUTA_DUMP}/mysql --user="root" --password= bdbrot < {RUTA_COPIA}/{file}'
                os.popen(proceso)
                conn.close()                
                return True
            else: return False

        except:
            return False

# Función para borrar el contenido de todas las tablas, para que no halla
#   duplicados en el KEYID, y de error.
def borrado_base_datos(self):
    conn = create_connection(self)
    try:
        cur = conn.cursor()
        # Creamos la sentencia sql con un bucle con todas las tablas de la base de
        #   datos, y la sentencia TRUNCATE, para borrar su contenido
        sql = 'SET FOREIGN_KEY_CHECKS = 0;'
        for tabla in TODAS_TABLAS:
            sql += f'TRUNCATE {tabla};'
        sql += 'SET FOREIGN_KEY_CHECKS = 1;'
        cur.execute(sql)
        return True

    except:
        return False

    finally:
        if conn:
            cur.close()
            conn.close()

# Función para hacer una carga parcial, desde un archivo json, de la base de datos
def carga_parcial(self, file):
    # Abrimos, leemos y creamos un diccionario con los datos de archivo .json
    with open(f'{RUTA_COPIA}/{file}', 'r') as archivo:
        datos = json.load(archivo)
    conn = create_connection(self)
    '''
    Creamos un bucle para grabar los datos registro a registro, de todos los campos.
    1º Separamos las tablas del archivo 'datos' y las enumeramos, para utilizar ese índice.
    2º Creamos un bucle con los registros de cada tabla, que corresponde a un diccionario.
        - Formamos los campos con los .keys del registro.
        - En 'valores' componemos '%s' por cada campo del registro, que luego se sustituirá
            por los valores, reales, que queremos grabar.
        - Creamos la sentencia sql, con la tabla, los campos y '%s' correspondientes a cada
            registro.
        - Por último, ejecutamos la sentencia sql con la tupla de los valores de cada registro.
    '''
    try:
        for n, tabla in enumerate(datos):
            cur = conn.cursor()
            for registro in tabla:
                columnas = ','.join(registro.keys())
                valores = ','.join(['%s'] * len(registro))
                sentencia_sql = f"INSERT INTO {TODAS_TABLAS[n]} ({columnas}) VALUES ({valores})"
                cur.execute(sentencia_sql, tuple(registro.values()))
                conn.commit()
        msg = QMessageBox.information(self, 'Carga parcial', 'Proceso completado...')            
        return True

    except:
        return False

    finally:
        if conn:
            cur.close()
            conn.close()