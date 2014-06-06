valores=[["x",7],["y",6],["t",[1,2,3,4,5]]]

#Funcion que realiza las operaciones hasta llegar al ultimo parentesis
def recorrerexpresion(operacion):
    indice=0
    valortemp=0
    operando=""
    bandera=False
    resultado=0
    while indice!=len(operacion):
        if tipodato(operacion[indice])=="variable":
            operacion[indice]=str(getValor(operacion[indice]))
            
        if tipodato(operacion[indice])=="num":

            if bandera==False:
                if resultado!=0:
                    valortemp=resultado
                    bandera=True
                else:
                    resultado=eval(operacion[indice])
                    
                    indice+=1
                    bandera=True
                
            else:
                resultado=operar(resultado, operando, eval(operacion[indice]))
                bandera=False
                indice+=1
                
        elif tipodato(operacion[indice])=="signo":
            operando=operacion[indice]
            indice+=1

        elif tipodato(operacion[indice])=="#":
            resultado = numeral(operacion[1:])
            
          
        else:
            return resultado
            
    return resultado
        
def numeral(lista):
    
            

def tipodato(dato):
    try:
        if dato=="+" or dato=="-" or dato=="div" or dato=="*":
            return "signo"
        if isinstance(eval(dato), (int, long, float, complex))==True:
            return "num"
        elif type(eval(dato))==list:
            return list
        else:
            return str
    except NameError:
        if dato=="true" or dato=="false":
            return bool
        else:
            return "variable"
    except SyntaxError:
        return str
    
def getValor(variable):
	for i in valores:
		if i[0] == variable:
			return i[1]
			
	return "Variable "+variable+" no definida"


def operar(num1, op, num2):
    resultado=0
    if op=="+":
        resultado=num1+num2
        return resultado
    elif op=="*":
        resultado=num1*num2
        return resultado
    elif op=="div":
        resultado=num1/num2
        return resultado
    elif op=="-":
        resultado=num1-num2
        return resultado
    else:
        return resultado
    
