import re
valores=[] #Lista que se almacena todos los valores y resultados para mostrar el resultado de estatico y dinamico



###########################FUNCION PRINCIPAL##################################
def main():
	listalectura=leerSML()
	#imprimir(listalectura)
	procesar(listalectura)
	

######################funcion para leer el archivo SML#####################################
def leerSML():
	listalectura=[] #Lista que va a contener todas las lineas leidas y spliteadas del .sml
	archi=open('test.sml','r')
	linea=archi.readline()
	while linea!="":
		listalectura.append(crearlista(linea)) #Le concatena a listalectura toda las lineas leidas en el .sml
		linea=archi.readline()
	archi.close()
	return crearLineaEvaluacion(listalectura) #retorna el resultado de la funcion crearLineaEvaluacion que devolvia una copia de ListaLectura modificada en sublistas
	

##########################Funcion para crear las sublistas y agregarlas a la listalectura##################################
def crearlista(linea):
	temp=re.split(' |(;)|\n|([()])|(\W)',linea )
	try:
		while True:
			temp.remove(None)
	except ValueError:
		pass
	try:
		while True:
			temp.remove("")
	except ValueError:
		pass
	return temp #Lista que contiene todas las lineas del .sml


#######################################33##########Funcion para procesar las listas################################################	
def procesar(listalectura):
	for i in listalectura:
		if i[0] == 'val':
			procesarVal(i[1:])
				
def procesarVal(asignacion):
	
############################Funcion para crear listas por cada expresion dentro del .sml############################################
def crearLineaEvaluacion(linea):
	copia=[]
	temp=[]
	for i in linea: #recorre cada lista de linea la cual contiene una sublista por linea
		indice=0
		while indice<len(i)-1:#recorrre los valores de una sublista en i para crear una nueva lista independiente
			if i[indice]==";":
				copia.append(temp)
				indice+=1
				temp=[]
			temp.append(i[indice])
			indice+=1
		if i != []:
			copia.append(temp)
			temp=[]
			
	return copia #retorna una lista con una copia de listalectura modificada
	
	
	
	
	
			
def procesarVal2(i,contador):
	temp=[]
	temp2=0 #Valor que almancena los valores temporales de las operaciones aritmeticas hasta que llegue al ;
	temp.append(i[contador])
	contador+=1
	if i[contador] == "=":
		contador+=1
		while i[contador]!=";":
			if tipodato(i[contador])==bool:
				temp2=getValor(i[contador])
				contador+=1
			elif tipodato(i[contador])!=str and tipodato(i[contador])!="signo" and tipodato(i[contador])!="variable":
				temp2=eval(i[contador])
				contador+=1
			elif tipodato(i[contador])=="signo" and tipodato(i[contador+1])!=str:
				if tipodato(i[contador+1])=="variable":
					temp2=evaluarExpresion(temp2,i[contador],getValor(i[contador+1]))
					contador+=2
				else:
					temp2=evaluarExpresion(temp2,i[contador],eval(i[contador+1]))
					contador+=2
			elif tipodato(i[contador])=="variable":
				temp2=getValor(i[contador])
				contador+=1	
			else:
				contador+=1
				
		temp.append(temp2) #guarda el resultado final de la operacion aritmetica en temp
		valores.append(temp)	
	return contador
####################funcion que retorna la evaluacion de la expresion##############################33	
def evaluarExpresion(p1, operador, p2):
	if operador == '+':
		return p1+p2
	elif operador == '~':
		return p1-p2
	elif operador == '*':
		return p1*p2
	elif operador == 'div':
		return p1/p2
	
######################Obterner el valor de la variable##################################
def getValor(variable):
	for i in valores:
		if i[0] == variable:
			return i[1]
			
	return "Variable "+variable+" no definida"
######################Funcion para crear una bandera auxiliar para cuando vienen varios parentesis en un Val###############################
def determinarBandera(i):
        bandera=0
        e=0
        while e<len(i):
                if i[e] == "(":
                        bandera+=1
                        e+=1
                e+=1
        return bandera
	
##########################Funcion que enviara el resultado final a la pagina web y mostrar su resultado#####################################
def resultado():
	contador=0
	while contador<len(listalectura[0]):
		if listalectura[0][contador]=="val":
			print(listalectura[0][contador+3])
			print "* Static Environtment: "+listalectura[0][contador+1] + " : " + tipodato(listalectura[0][contador+3]) + "*"
		contador+=1
	#if cadena.find()
####################################Funcin que analiza el tipo de dato que contiene los elementos dentro de valor##############################
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
			return "variable"
	except SyntaxError:
		return str
####################################Funcion de prueba para estar leyendo el contenido de las listas#####################################			
def imprimir(lista):
	for i in lista:
		print i
######################################Funcion de prueba para leer el tipo de un numero (Funcion no usada)####################################
def numero(strnum):
	try:
		if(float(strnum)%1==0):
			return int(strnum)
		else:
			return float(strnum)	
	except ValueError:
		print "Error"
		
		   
main()
#crearLineaEvaluacion([['val', 'x', '=', '666', ';', 'val', 'y', '=', '[', '2', ',', '3', ']', ';', 'val', 'z', '=', '(', '1', ',', '2', ')', ';', 'val', 'w', '=', 'true', ';']])
#procesar()
#determinarBandera(["val","=","(","2","+","3",")","+","(","3","*",")"])
