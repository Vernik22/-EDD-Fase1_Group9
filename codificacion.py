def cod_iso(cadena: str) -> str:
    try:
        return cadena.encode('iso-8859-1')
    except:
        print("Error de codificacion ISO")
        return None



def toASCII(cadena):
    cadena = str(cadena)
    resultado = 0
    for i in cadena:
        i = str(i)
        resultado += ord(i)
    return str(resultado)



def utf(cadena: str) -> str:

    try:
        return cadena.encode()
    except:
        print("Error de codificacion ISO")
        return None



'''print('1')
print(cod_iso('1'))
print(toASCII('1'))
print(utf('español'))
print(utf('palabra'))
'''