from team09 import mainG as g


print("----- ELIMINAR BASE ------------")
print(g.dropDatabase("Base33"))
print(g.showDatabases())

print("----- CAMBIAR MODO  ------------")
print(g.alterDatabaseMode("Base55", "bplus"))

print(g.b.showDatabases())
print(g.bplus.showDatabases())

print("----- CREACION DE TABLAS---------")
print(g.createTable("Base1", "Tabla1", 3))
print(g.createTable("Base1", "Tabla2", 3))
print(g.createTable("Base55", "Tabla1", 3))
print(g.createTable("Base55", "Tabla2", 3))
print(g.createTable("Base4", "Tabla1", 3))
print(g.createTable("Base4", "Tabla2", 3))
print(g.createTable("Base4", "Tabla3", 3))
print(g.createTable("Base4", "Tabla4", 3))

print("----- ASIGNA PK ----------")
print(g.alterAddPK("Base55", "Tabla1", [0]))
print(g.alterAddPK("Base4", "Tabla1", [0]))
print(g.alterAddPK("Base4", "Tabla2", [0]))
print(g.alterAddPK("Base4", "Tabla3", [0]))
print(g.alterAddPK("Base5", "Tabla1", [0]))
print(g.alterTableAddFK("Base4","Tabla2","byron",["0"],"Tabla3",["1"]))

print("----- QUITA PK ----------")
print(g.alterDropPK("Base55", "Tabla1"))

print("----- QUITA COLUMNA ----------")
print(g.alterDropColumn("Base55", "Tabla1", 2))

print("----- AGREGA COLUMNA ----------")
print(g.alterAddColumn("Base55", "Tabla1", 5))
print("------- BLOCK CHAIN --------")
print(g.safeModeOn("Base4", "Tabla2"))

print("----- AGREGA DATOS A TABLAS ----------")
print(g.insert("Base4", "Tabla1", ['1', 'HOLA', 'MUNDO']))
print(g.insert("Base4", "Tabla2", ['2', 'HOLA2', 'MUNDO2']))
print(g.insert("Base4", "Tabla2", ['1', 'HOLA', 'MYNOR']))
print(g.insert("Base4", "Tabla2", ['12', 'MYNOR', 'SABAN']))
print(g.insert("Base55", "Tabla1", ['1', 'HOLA', 'MYNOR']))

print("------- BLOCK CHAIN --------")
print(g.safeModeOff("Base4", "Tabla2"))
# print("----- IMPRIME DATOS DE TABLAS ----------")
# print(extractTable("Base4", "Tabla1"))
# print(extractTable("Base4", "Tabla2"))
# print(extractTable("Base4", "Tabla3"))
# print(extractTable("Base1", "Tabla4"))
# print(extractTable("Base55", "Tabla1"))
#
# print("----- CAMBIAR MODO  ------------")
# print(alterDatabaseMode("Base4", "bplus"))
# print(extractTable("Base4", "Tabla1"))
print(g.extractTable("Base4", "Tabla2"))
#
# print(json.showDatabases())
# print(bplus.showDatabases())
# print(bplus.extractTable("Base4", "Tabla1"))
# print(bplus.extractTable("Base4", "Tabla2"))

print("===IMPRIMO BASES==")
for d in lista_bases:
    print(d)

print("=== IMPRIMO tablas== ")
for d in list_table:
    print("\n" + str(d))


def datosTabla():
    print("=== IMPRIMO datos de tablas== ")
    for tabla in list_table:
        print(f'Tabla: {tabla.tabla} , BD:{tabla.base}')
        cadena = '['
        for _ in tabla.codificado:
            cadena += str(_) + ','
        cadena += ']'
        print(cadena)


datosTabla()
print(g.alterDatabaseEncoding('Base4', 'utf-8'))
datosTabla()
print(g.alterDatabaseCompress("Base4", 5))
print(g.alterDatabaseCompress("Base55", -2))

print(g.alterDatabaseDecompress("Base4"))
print(g.alterDatabaseDecompress("Base55"))

print(g.alterTableDecompress("Base4", "Tabla1"))
print(g.alterTableDecompress("Base55", "Tabla2"))

print(g.alterTableCompress("Base4", "Tabla1", 7))
print(g.alterTableCompress("Base55", "Tabla2", 6))
print(g.alterTableDecompress("Base4", "Tabla1"))
print(g.alterTableDecompress("Base55", "Tabla2"))
print(g.checksumDatabase("Base4","SHA256"))
print(g.checksumTable("Base4","Tabla2","SHA256"))
print(g.encrypt("byron","cul"))
print(g.decrypt(encrypt("byron","cul"),"cul"))
# dejar el ascii como "ascii" en la funcion
print(g.graphDSD("Base4"))