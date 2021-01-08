
def cod_iso(cadena: str) -> str:
    try:
        return cadena.encode('iso-8859-1')
    except:
        print("Error de codificacion ISO")
        return None



def toASCII(cadena)-> str:
    try:
        return cadena.encode('ascii', errors='ignore')
    except:
        print('Error en codificacion ascci')
        return None


def utf(cadena: str) -> str:
    try:
        return cadena.encode()
    except:
        print("Error de codificacion ISO")
        return None
# print('algo no se para probar ñ')
# print(cod_iso('algo no se para probar ñ'))
# print(utf('algo no se para probar ñ'))
print(toASCII('algo no se para probár'))