import re
listalectura=[]#Lista que almacena todas las lineas leidas en el archivo SML en sublistas
valores=[] #Lista que se almacena todos los valores y resultados para mostrar el resultado de estatico y dinamico

######################funcion para leer el archivo SML#####################################
def leerSML():
	archi=open('test.sml','r')
	linea=archi.readline()
	while linea!="":
		crearlista(linea)
		linea=archi.readline()
	archi.close()

##########################Funcion para crear las sublistas y agregarlas a la listalectura##################################
def crearlista(linea):
	temp=re.split(' |(;)|\n|([()])|(=)',linea )
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
	listalectura.append(temp)


##############################Funcion para procesar las listas#######################	
def procesar():
	for i in listalectura:
		indice=0
		while indice<len(i):
			bandera=determinarBandera(i)
			if i[indice] == 'val':
				indice=procesarVal(i,indice+1)
			
						
			indice+=1
			
#def asociarvalor():
def procesarVal(i,contador):
	temp=[]
	temp.append(i[contador])
	contador+=1
	if i[contador] == "=":
		contador+=1
		if tipodato(i[contador]) != "string":
			temp.append(i[contador])
			valores.append(temp)
			if i[contador]=="(":
				contador+=1
				temp=[]
				while i[contador]!=")":
					temp.append(i[contador])
					contador+=1
				contador+=1
	return contador

######################Funcion para crear una bandera auxiliar para cuando vienen varios parentesis en un Val###############################
def determinarBandera(i):
        bandera=0
        e=0
        while e<len(i):
                if i[e] == "(":
                        bandera+=1
                        e+=1
                e+=1
        print bandera
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
		if type(eval(dato))==int:
			return "int"
		elif type(eval(dato))==float:
			return "float"
		elif type(eval(dato))==tuple:
			return "tuple"
		elif type(eval(dato))==list:
			return "list"
		elif type(eval(dato))==bool:
			return "bool"
		else:
			return "string"
	except NameError:
		return "string"
	except SyntaxError:
		return "string"
####################################Funcion de prueba para estar leyendo el contenido de las listas#####################################			
def imprimir():
	for i in listalectura:
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
		
		   
leerSML()
procesar()
imprimir()
#determinarBandera(["val","=","(","2","+","3",")","+","(","3","*",")"])
