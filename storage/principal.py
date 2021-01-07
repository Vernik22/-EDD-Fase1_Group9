from storage.b import BMode as b
from storage.hash import HashMode as hash
from storage.isam import ISAMMode as isam
from storage.bplus import BPlusMode as bplus
from storage.avl import avlMode as avl
from storage.json import jsonMode as json
from storage.dict import DictMode as dict
from storage import serealizar as actualizar
import os

path = os.getcwd() + "\\data"

# database:
# {
#   nombre: str,
#   modo: str,
#   encoding: str
# }
def __init__():
    global datos
    datos = []
    if not os.path.isfile(path + "\\data"):
        actualizar.commit(datos, path)
    else:
        datos = actualizar.rollback(path)

__init__()


# ----------funcion unificacion de modo 1 #------------------------
def createDatabase(database: str, mode: str, encoding: str) -> int:
    # try:
        if encoding not in ["utf8", "ascii", "iso-8859-1"]:
            return 4
        if mode not in ["avl", "b", "bplus", "dict", "isam", "hash","json"]:
            return 3
        db = get_database(database)
        if db is not False:  # significa que ya existe esa base de datos
            return 2
        respuesta = modoCreateDatabase(database, mode, encoding)
        return respuesta
    # except:
    #     return 1


def dropDatabase(database: str):
    baseDatos = get_database(database)
    mode = baseDatos["modo"]
    if mode == "avl":
        val = avl.dropDatabase(database)

    elif mode == "b":
        val = b.dropDatabase(database)

    elif mode == "bplus":
        val = bplus.dropDatabase(database)

    elif mode == "dict":
        val = hash.dropDatabase(database)

    elif mode == "isam":
        val = isam.dropDatabase(database)

    elif mode == "json":
        val = json.dropDatabase(database)

    elif mode == "hash":
        val = dict.dropDatabase(database)

    datos.remove(BaseDatos)
    Guardar()

# --------------funciones extras de utilidad----------------

def modoCreateDatabase(database: str, mode: str, encoding: str) -> int:
    if mode == "avl":
        respuesta = avl.createDatabase(database)
    elif mode == "b":
        respuesta = b.createDatabase(database)
    elif mode == "bplus":
        respuesta = bplus.createDatabase(database)
    elif mode == "dict":
        respuesta = dict.createDatabase(database)
    elif mode == "isam":
        respuesta = isam.createDatabase(database)
    elif mode == "json":
        respuesta = json.createDatabase(database)
    elif mode == "hash":
        respuesta = hash.createDatabase(database)
    if respuesta == 0:
        datos.append({"nombre": database, "modo": mode, "encoding": encoding})
        Guardar()
    return respuesta

def Guardar():
    actualizar.commit(datos, path)


def get_database(database):
    for db in datos:
        if db["nombre"] == database:
            return db

    return False

