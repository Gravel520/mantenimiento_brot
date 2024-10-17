'''
Script en Python donde tenemos las variables globales y perpanentes que necesitamos
    para que funciones la aplicación.
    Una función para poder leer un archivo de texto donde el usuario puede elegir
        el directorio donde desea que se guarden las copias de seguridad, y donde 
        elegir el directorio donde tenemos instalado el 'xampp', concretamente el 
        lugar donde estan los script 'mysqldump' y 'mysql', que utilizaremos para
        crear y restaurar las copias de seguridad.
    Una variable donde se encuentran los nombres de las tablas, menos (servicio y 
        grabacion_general).
    Otra variable donde están los nombres de los campos que componen las tablas
        anteriores.
    Por último otra variable donde estan los nombres de todas las tablas, que usaremos
        para el borrado de todos los datos, y poder dejar la base de datos vacía.
'''
# Función para leer el archivo de texto donde están las variables de las
#   ruta de las copias y donde esta el script para usar mysql
def cargar_variables():
    lineas = []
    with open("variables.txt", "r") as archivo:
        for linea in archivo:
            lineas.append(linea.strip())

    RUTA_COPIA = lineas[0]
    RUTA_DUMP = lineas[1]
    return RUTA_COPIA, RUTA_DUMP

# Función para escribir el contenido de las cajas de texto de la pestaña
#   'configuración' de forma automática
def grabar_variables(ruta_copia, ruta_dump):
    archivo = open("variables.txt", "w")
    archivo.write(f'{ruta_copia}\n')
    archivo.write(ruta_dump)
    archivo.close()

# Variable con las tablas de la base de datos bdbrot
TABLAS = ('categoria', 'cliente', 'factura', 'grabacion_automatica', 'precio', 'productos','ruta')

# Variable de los campos de las tablas
CAMPOS_TABLAS = (
    ('idcategoria', 'nombre', 'iva', 'agrupar'), 
    ('idcliente', 'nombre', 'factura', 'baja', 'fecha_baja', 'bollos', 'idruta'),
    ('direccion', 'razon_social', 'nif', 'codigo_postal', 'provincia', 'idcliente'),
    ('idautomatica', 'numero_dia', 'cantidad_automatica', 'idcliente', 'idproductos'),
    ('idprecio', 'precio_unitario', 'idcliente', 'idproductos'),
    ('idproductos', 'nombre', 'idcategoria'),
    ('idruta', 'nombre')
    )

# Variable donde se encuentran todas las tablas de la base de datos
#   para realizar la carga parcial de los datos
TODAS_TABLAS = ('servicio', 'grabacion_general', 'categoria', 'cliente', 'factura', 'grabacion_automatica', 'precio', 'productos','ruta')