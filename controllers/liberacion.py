'''
Scrip en Python donde vamos a controlar todas la funciones de la opción
    de liberación, que consiste en borrar el contenido de las tablas
    'Servicio', primero, y 'Grabación_general', después, hasta una fecha
    especificada por el usuario. Este borrado será irrecuperable.

Para ello tendremos que utilizar varias sentencias sql.
    1º. Para seleccionar el idServicio, de la tabla 'servicio', desde el 
        principio de la tabla hasta la fecha seleccionada.
        SELECT idServicio FROM `servicio`
        WHERE fecha <= '{fe_final}'
    
    2º. Para borrar los registros, de la tabla 'grabacion_general', cuyos
        idServicio esten contenidos los idServicio de la consulta anterior.
        DELETE * FROM `grabacion_general` 
        WHERE idServicio >= '{np.min(records)}' and idServicio <= '{np.max(records)}'

    3º. Por último para borrar los registros obtenidos en la consulta 1º.
        DELETE idServicio FROM `servicio`
        WHERE fecha <= '{fe_final}'
'''

from mysql import connector
import numpy as np
from bd_mysql.connection import create_connection

gfecha_final = None

# Obtenemos los id de la tabla 'Servicio' desde el principio de la tabla hasta
#   la fecha establecida.
def obtener_id_liberacion(self, fe_final):
    conn = create_connection(self)
    sql = f'''
        SELECT idServicio FROM `servicio`
        WHERE fecha <= '{fe_final}'
        '''

    try:
        cur = conn.cursor()
        cur.execute(sql)
        records = cur.fetchall()
        return records
    
    except connector.Error as e:
        print('Error al obtener los id de Servicios para borrarlos:' + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

# Borramos los registros de la tabla 'grabacion_general', que corresponde con los
#   el intervalo de los idServicio obtenidos en la consulta anterior.
def borrar_registros(self, records):
    conn = create_connection(self)
    sql = f'''
        DELETE FROM `grabacion_general` 
        WHERE idServicio >= "{np.min(records)}" and idServicio <= "{np.max(records)}"
        '''
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

    except connector.Error as e:
        print('Error al borrar los registros de la tabla (grabacion_general):' + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

def borrar_id_liberacion(self, fecha_final):
    conn = create_connection(self)
    sql = f'''
        DELETE FROM `servicio`
        WHERE fecha <= '{fecha_final}'        
        '''
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

    except connector.Error as e:
        print('Error al borrar los id de la tabla (servicio):' + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()
