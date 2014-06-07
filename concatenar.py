valores=[["t",2]]

def concatenar(lista):
    tipo=""
    temp=""
    for i in lista:
        tipo=tipodato(i)
        if tipo != "variable" and tipo != "signo":
            temp+=i
        else:
            if tipo =="signo":
                if tipo == "~":
                    temp+="-"
                elif i == "div":
                    temp+="/"
                else:
                    temp+=i
            else:
                if tipo == "variable":
                    temp+=str(getValor(i))
                else:
                    temp+=i
    return temp
                    
            
            


def tipodato(dato):
    try:
        if dato=="+" or dato=="~" or dato=="div" or dato=="*":
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

def stringOvariable(dato): 
    for i in valores:
        if dato in i:
            return "variable"
    return "String"

def getValor(variable):
	for i in valores:
		if i[0] == variable:
			return i[1]
			
	return "Variable "+variable+" no definida"










