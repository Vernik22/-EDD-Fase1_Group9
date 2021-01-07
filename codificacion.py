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
    return resultado
print('pythön en español')
print(cod_iso('pythön en español'))
print(toASCII('pythön en español'))