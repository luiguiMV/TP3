valores=[["t",2]]

def mostrarTipo(exp):
    if type(exp)==tuple:
        return obtenertipoTupla(exp)
    elif type(exp)==list:
        return obtenertipoLista(exp)
    else:
        return str(tipodato(str(exp)))

def obtenertipoLista(lista):
    cadena=""
    if tipodato(str(lista[0]))==int:
        cadena+=" int"
    elif tipodato(str(lista[0]))==float:
        cadena+=" float"
    elif tipodato(str(lista[0]))==tuple:
        cadena+=" tuple"
    elif tipodato(str(lista[0]))==list:
        cadena+=obtenertipoLista(lista[0])
    else:
        cadena+=" String"
        
    return cadena +" list "

def obtenertipoTupla(tupla):
    contador=0
    cadena= " "
    while contador!=len(tupla):
        if tipodato(str(tupla[contador]))==int:
            cadena+=" int"
            contador+=1
            cadena+=" *"
        elif tipodato(str(tupla[contador]))==float:
            cadena+=" float "
            contador+=1
            cadena+= " *"
        elif tipodato(str(tupla[contador]))==tuple:
            cadena+="( " + obtenertipoTupla(tupla[contador]) +" ) "
            contador+=1
            cadena+=" *"
        elif tipodato(str(tupla[contador]))==list:
            cadena+=obtenertipoLista(tupla[contador])+ " "
            contador+=1
            cadena+=" *"
        else:
            cadena+=" String "
            contador+=1
            cadena+=" *"
    return cadena
    
def stringOvariable(dato):
    for i in valores:
        if dato in i:
            return "variable"
    return "String"
    
def tipodato(dato):
    try:
        if dato=="+" or dato=="~" or dato=="div" or dato=="*" or dato=="=":
            return "signo"
        elif type(eval(dato))==int:
            return int
        elif type(eval(dato))==float:
            return float
        elif type(eval(dato))==tuple:
            return tuple
        elif type(eval(dato))==list:
            return list
        else:
            return str
    except NameError:
        if dato=="true" or dato=="false":
            return bool
        else:
            return stringOvariable(dato)
    except SyntaxError:
	    return str
    
