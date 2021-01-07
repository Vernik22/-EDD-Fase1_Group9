#se copian las tablas de las bases aqui


class Tabla(object):
    def __init__(self, basedatos,nombre,columna,modo):
        self.base=basedatos #nombre base
        self.tabla = nombre   #nombre tabla
        self.columnas = columna  #numero de columnas
        self.modo=modo   #modo en que se guardo la tabla
        self.pk=None  # pk de la tabla
        self.fk=None  # fk de la tabla
        self.datos=[] #las tablas que se guardan  abajo se muestra como se guardo
        
    def __str__(self) -> str:
        return f" MODOTABLA {self.modo} nombreBase {self.base} NOmbreTabla {self.tabla} Ncol {self.columnas}  PK {self.pk}  FK {self.fk} tuplas {self.datos} "


class Base(object):
    def __init__(self, basedatos,modo,encoding):
       self.base=basedatos
       self.modo=modo
       self.encoding=encoding

    def __str__(self) -> str:
        return f" Base {self.base}  modo {self.modo}  encoding {self.encoding} "


''' ASI SE GUARDAN LOS DATOS  DE LAS TABLAS  (TUPLAS)


lista=["base","cero","hola"]
lista1=["base1","uno","hola"]
lista2=["base2","dos","hola"]
lista3=["base3","tres","hola"]
lista4=["base4","cuatro","hola"]


dic={}

dic[lista[0]]=lista
dic[lista1[0]]=lista1
dic[lista2[0]]=lista2
dic[lista3[0]]=lista3
dic[lista4[0]]=lista4

for d in dic.values():
    print(d)

    '''