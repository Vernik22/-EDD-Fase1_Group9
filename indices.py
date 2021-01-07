class Fks:
    def __init__(self):
        self.db=db
        self.table = tab
        self.indexName = index
        self.columns = columns
        self.tableRef = tableRef
        self.columnRef = columnRef

class FksIndex:
    def __init__(self): 
        self.Indices = {}

    def alterTableAddFK(self, database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
        try:
            if condition:
                #DB si existe
                if condition:
                    #table si existe
                    if condition:
                        #table ref si existe
                        if condition:
                            #cantidad exacta entre culumns y columnsRef
                            return 0
                        else:
                            return 4
                    else:
                        return 3
                else:
                    return 3
            else:
                return 2
        except:
            return 1


    def alterTableDropFK(self, database: str, table: str, indexName: str) -> int:
        try:
            if condition:
                #DB si existe
                if condition:
                    #table si existe
                    if indexName in self.Indices:
                        #si existe el index
                        del self.Indices[indexName]
                        return 0
                    else:
                        return 4
                else:
                    return 3
            else:
                return 2
        except:
            return 1

    def alterTableAddUnique(self,database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
        try:
            if condition:
                #Db si existe
                if condition:
                    #tableRef si exixte
                    if condition:
                        #cantidad exacta entre columns y columnsRef
                        if condition:
                            #restriccion de unicidad
                            return 0
                        else:
                            return 5
                    else:
                        return 4
                else:
                    return 3
            else:
                return 2
        except:
            return 1

    def alterTableDropUnique(self,database: str, table: str, indexName: str) -> int:
        try:
            if condition:
                #Db si existe
                if condition:
                    #table si existe
                    if condition:
                        #nombre de indice si existe
                        return 0
                    else:
                        return 4
                else:
                    return 3
            else:
                return 2
        except:
            return 1

    def alterTableAddIndex(self,database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
        try:
            if condition:
                #Db si existe
                if condition:
                    #table or tableRef si existen
                    if condition:
                        #cantidad exacta entre columns y columnsRef
                        return 0
                    else:
                        return 4
                else:
                    return 3
            else:
                return 2
        except:
            return 1

    def alterTableDropIndex(self,database: str, table: str, indexName: str) -> int:
        try:
            if condition:
                #Db si existe
                if condition:
                    #table si existe
                    if condition:
                        #index si existe 
                        return 0
                    else:
                        return 4
                else:
                    return 3
            else:
                return 2
        except:
            return 1