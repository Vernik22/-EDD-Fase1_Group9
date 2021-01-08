from storage import principal as p
import pickle

class Fks:
    def __init__(self,db,tab,index,columns,tableRef,columnRef,ind):
        self.db=db
        self.table = tab
        self.indexName = index
        self.columns = columns
        self.tableRef = tableRef
        self.columnRef = columnRef
        self.colintab = ind

def __init__():
    global Indices
    Indices = {}
    if os.path.exists("Data/Indices.bin"):
        CargarIndicesBIN()

def CargarIndicesBIN():
    with open("Data/Indices.bin", "rb") as r:
        content = pickle.load( r)
    return Indices = content

def write():
    with open("Data/Indices.bin","bw") as w:
        pickle.dump(Indices, w )

def alterTableAddFK(self, database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list, modo) -> int:
    try:
        lc=len(columns)
        lcr=len(columnsRef)
        if lc==lcr:
            #cantidad exacta entre culumns y columnsRef
            j = p.actualMod(modo).extractTable(database, table) 
            co=len(j[0])
            Indices[indexName]=Fks(database, table,indexName,columns,tableRef,columnsRef,co+1)
            p.actualMod(modo).alterAddColumn(database,table,indexName)
            p.actualMod(modo).createTable(database, indexName, 4)
            p.actualMod(modo).insert(database,indexName,[table,columns,tableRef,columnsRef])
            write()
            return 0
        else:
            return 4
    except:
        return 1


def alterTableDropFK(self, database: str, table: str, indexName: str, modo) -> int:
    try:
        if indexName in Indices:
            #si existe el index
            p.actualMod(modo).alterDropColumn(database, table, Indices[indexName].colintab)
            p.actualMod(modo).dropTable(database, indexName)
            del Indices[indexName]
            write()
            return 0
        else:
            return 4
    except:
        return 1

def alterTableAddUnique(self,database: str, table: str, indexName: str, columns: list, modo) -> int:
    try:
        lc=len(columns)
        lcr=len(columnsRef)
        if lc==lcr:
            #cantidad exacta entre columns y columnsRef
            if not indexName in Indices:
                #restriccion de unicidad
                j = p.actualMod(modo).extractTable(database, table) 
                co=len(j[0])
                Indices[indexName]= Fks(database, table,indexName,columns,tableRef=None,columnsRef=None,co+1)
                p.actualMod(modo).alterAddColumn(database,table,indexName)
                p.actualMod(modo).createTable(database, indexName, 2)
                p.actualMod(modo).insert(database,indexName,[table,columns])
                write()
                return 0
            else:
                return 5
        else:
            return 4
    except:
        return 1

def alterTableDropUnique(self,database: str, table: str, indexName: str, modo) -> int:
    try:
        if indexName in Indices:
            #nombre de indice si existe
            p.actualMod(modo).alterDropColumn(database, table, Indices[indexName].colintab)
            p.actualMod(modo).dropTable(database, indexName)
            del Indices[indexName]
            write()
            return 0
        else:
            return 4
    except:
        return 1

def alterTableAddIndex(self,database: str, table: str, indexName: str, columns: list, modo) -> int:
    try:
        lc=len(columns)
        lcr=len(columnsRef)
        if lc==lcr:
            #cantidad exacta entre columns y columnsRef
            j = p.actualMod(modo).extractTable(database, table) 
            co=len(j[0])
            Indices[indexName]= Fks(database, table,indexName,columns,tableRef=None,columnsRef=None,co+1)
            p.actualMod(modo).alterAddColumn(database,table,indexName)
            p.actualMod(modo).createTable(database, indexName, 2)
            p.actualMod(modo).insert(database,indexName,[table,columns])
            write()
            return 0
        else:
            return 4
    except:
        return 1

def alterTableDropIndex(self,database: str, table: str, indexName: str, modo) -> int:
    try:
        if indexName in Indices:
            #index si existe 
            p.actualMod(modo).alterDropColumn(database, table, Indices[indexName].colintab)
            p.actualMod(modo).dropTable(database, indexName)
            del Indices[indexName]
            write()
            return 0
        else:
            return 4
    except:
        return 1