'''
Script en Python donde vamos a controlar todas las funciones de la 
    copia selectiva.
    Listar entre una fecha y otra:
    SELECT idservicio FROM `servicio` WHERE fecha >= '2021-05-25' and fecha <= '2021-05-30'

    Listar un mes y un año concreto:
    SELECT idservicio FROM `servicio` WHERE date_format(fecha, '%Y-%m') = '2021-06';

    Listar los registros correspondientes a los id obtenidos con las sentencias anteriores:
    SELECT * FROM `grabacion_general` WHERE idServicio >= '262' and idServicio <= '390';

    PARA QUE NO HAYA ERRORES A LA HORA DE RESTAURAR UNA COPIA, TENDREMOS QUE AÑADIR EN EL
    MISMO ARCHIVO JSON, LOS REGISTROS DE TODAS LAS TABLAS, PARA QUE TENGAMOS ERRORES POR SI 
    HAY ALGUN CAMBIO, EN LOS REGISTROS, DE UNA RESTAURACION A OTRA.

    Borrar los registros que no han sido seleccionados:
    DELETE FROM `servicio`
            WHERE date_format(fecha, '%Y-%m') <> '{gano}-{gmes}

    Borrar los registros que no esten entre dos fechas concretas:
    DELETE FROM `servicio` WHERE fecha 
        NOT BETWEEN '2021-05-25' AND '2021-05-30';

'''

from PySide6.QtWidgets import QMessageBox
from mysql import connector
import numpy as np
import json
from bd_mysql.connection import create_connection
from controllers.DATOS import *

gfe_inicio = None
gfe_final = None
gmes = None
gano = None
gborrar = None

'''
    Con esta función vamos a obtener los datos de la tabla 'servicio'. Para ello recibimos
        los parámetros de fechas, mes y año, de la consulta que queremos crear.
        También recibimos el parámetro 'borrar', por si queremos borrar los datos de los que
        hemos creado la copia.
    Creamos una variables globales para poder utilizarlas en todas las funciones del script.

'''
def obtener_id(self, fe_inicio, fe_final, mes, ano):
    global RUTA_COPIA
    global RUTA_DUMP
    RUTA_COPIA, RUTA_DUMP = cargar_variables()
    
    global gfe_inicio, gfe_final, gmes, gano,gid_records
    gfe_inicio, gfe_final, gano = fe_inicio, fe_final, ano

    # Añadir un cero a la izquierda cuando el mes esta entre Enero y Septiembre
    gmes = str(mes)
    if len(gmes) == 1: gmes = gmes.zfill(2) # Añadimos los ceros necesarios para que tenga 2 caracteres

    # Obtenemos los registros de los servicios para obtener después los datos de la tabla
    #   'grabacion_general', mediante el id
    conn = create_connection(self)
    # Montamos la consulta sql según la opción
    if gmes == 'None':
        sql = f'''
            SELECT * FROM `servicio` 
            WHERE fecha >= '{gfe_inicio}' AND fecha <='{gfe_final}'
            '''
    else:
        sql = f'''
            SELECT * FROM `servicio`
            WHERE date_format(fecha, '%Y-%m') = '{gano}-{gmes}'
            '''

    try:
        cur = conn.cursor()
        cur.execute(sql)
        gid_records = cur.fetchall()
        # Creamos una variable con los id obtenidos de la consulta que los usaremos
        #   para hacer la consulta en la tabla 'grabacion_general'
        idservicio = [row[0] for row in gid_records] # Los id estan en la primera columna [0]
        return(idservicio)
    
    except connector.Error as e:
        print('Error al obtener los id de los Servicios: ' + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

# Función para obtener los registros de la tabla 'grabacion_general', a través de los
#   id recogidos en la tabla 'servicio', entre los valores mínimo y máximo.
def obtener_registros(self, records):
    consulta_sql = []
    tablas_records = []
    conn = create_connection(self)
    gg_sql = f'''
        SELECT * FROM `grabacion_general` 
        WHERE idServicio >= '{np.min(records)}' and idServicio <= '{np.max(records)}'
        '''
    
    # Creamos una lista con cada una de las consultas de todas las tablas
    for tabla in TABLAS:
        consulta_sql.append(f'SELECT * FROM `{tabla}`')

    # Obtenemos los registros de todas las tablas    
    try:
        cur = conn.cursor()
        cur.execute(gg_sql)
        gg_records = cur.fetchall() # Grabacion_general
        for consulta in consulta_sql: # Resto de las tablas
            cur.execute(consulta)
            tablas_records.append(cur.fetchall()) # Guardamos los registros de cada consulta en otra lista

        grabar_registros(self, gg_records, tablas_records)

    except connector.Error as e:
        print('Error al obtener el listado final de las tablas: ' + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

'''
    Función para crear un archivo .json con todos los datos obtenidos de las consultas,
        tanto los datos obtenidos de la tabla 'servicio', a través de la variable global
        'grecords', como los obtenidos de la tabla 'grabacion_general', a través del 
        parámetro 'records'
'''
def grabar_registros(self, gg_records, tablas_records):
    data = []
    parcial_data = []
    # Primero disponemos los datos de la tabla 'servicio'
    for row in gid_records:
        # Transformamos el dato la fecha en una cadena con formato (yy-mm-aa)
        grecord = {
            "idservicio" : row[0],
            "fecha" : row[1].strftime("%Y-%m-%d"),
            "semana" : row[2],
            "idcliente" : row[3]
        }
        parcial_data.append(grecord)
    data.append(parcial_data)
    
    parcial_data = []
    # Después los datos de la tabla 'grabacion_general'
    for row in gg_records:
        record = { 
            "cantidad_general" : row[0],
            "idservicio" : row[1],
            "idproductos" : row[2]
        }
        parcial_data.append(record)
    data.append(parcial_data)

    '''
    Tres bucles:
        1º Las tablas, 2.
            2º Los datos recuperados de las tablas de arriba.
                3º Los campos de cada tabla.
    Con la función 'zip', emparejamos los campos de las tablas, con los datos
        de cada registro, que deben ser del mismo tamaño.
    Después lo añadimos a un diccionario, con la clave como nombre del campo,
        y el valor con el dato del campo.
    No se pueden grabar datos que sean del tipo 'Decimal', para saber si es 
        decimal, convertimos el dato en string y comprobamos que tenga el '.' del
        decimal, si es así transformamos el dato en string.
    '''
    for i, nombre in enumerate(TABLAS):
        parcial_data = []        
        for dato in tablas_records[i]:
            record = {}
            for campo, dat in zip(CAMPOS_TABLAS[i], dato):
                if '.' in str(dat): # Comprobamos si hay un punto en el dato
                    dat = str(dat) # Si es así convertimos el dato en string
                record[campo] = dat
            parcial_data.append(record)
        data.append(parcial_data)

    # Convertir la lista de diccionarios en una cadena json
    json_data = json.dumps(data)

    # Crear el nombre del archivo con los datos de las fechas
    if gmes == 'None':
        nombre_file = f'{gfe_inicio}_{gfe_final}'

    else:
        nombre_file = f'{gmes}_{gano}'
    nombre_file = f'copia_{nombre_file}.json'
    # Crear o abrir un archivo json y escribir los datos en el
    file = open(f'{RUTA_COPIA}/{nombre_file}', 'w')
    file.write(json_data)
    file.close()
    
# Función para borrar los datos, si así lo elige el usuario
def borrar_datos(self, records):
    conn = create_connection(self) # Creamos la conexión
    # Comprobamos la opción elegida; tramo de fecha o mes y año,
    #   y creamos la consulta sql para borrar los id de Servicio
    if gmes == 'None':
        sql = f'''
            DELETE FROM `servicio`
            WHERE fecha >= '{gfe_inicio}' AND fecha <='{gfe_final}'
            '''
        
    else:
        sql = f'''
            DELETE FROM `servicio`
            WHERE date_format(fecha, '%Y-%m') = '{gano}-{gmes}'
            '''
        
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

    except connector.Error as e:
        print('Error al borrar los id de los Servicios: ' + str(e))

    finally:
        if conn:
            cur.close()
            
    # Ahora creamos la consulta sql para borrar los datos de Grabacion_general
    sql = f'''
        DELETE FROM `grabacion_general`
        WHERE idServicio >= '{np.min(records)}' and idServicio <= '{np.max(records)}'
        '''
        
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

    except connector.Error as e:
        print('Error al borrar los datos de Grabacion_general: ' + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()