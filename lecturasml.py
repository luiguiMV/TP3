import re
valores=[] #Lista que se almacena todos los valores y resultados para mostrar el resultado de estatico y dinamico
listalectura=[]
aE = []
aD = []

def ejecutar(nombre):
	listalectura=leerSML(nombre)
	procesar(listalectura)
	clasificacion(valores)
	
def getAmbienteEstatico():
	return aE

def getAmbienteDinamico():
	return aD

def clasificacion(valores): 
	cont=0 
	while cont<len(valores): 
		x=valores[cont][0] 
		y=valores[cont][1] 
		if y=="true": 
			y=True 
		elif y=="false": 
			y=False 
		z=type(y)
		aE.append(str(x)+" "+str(z))
		aD.append(str(x)+"="+str(y)) 
		cont+=1

	
######################funcion para leer el archivo SML#####################################
#Funcion para leer el archivo SML y procesarlo en listas para su interpretacion desde python:
#Salida: una lista de listas por linea del SML
def leerSML(nombrearchivo):
	listalectura=[] #Lista que va a contener todas las lineas leidas y spliteadas del .sml
	archi=open('uploads/'+nombrearchivo,'r')
	linea=archi.readline()
	while linea!="":
		listalectura.append(crearlista(linea)) #Le concatena a listalectura toda las lineas leidas en el .sml
		linea=archi.readline()
	archi.close()
	return crearLineaEvaluacion(listalectura) #retorna el resultado de la funcion crearLineaEvaluacion que devolvia una copia de ListaLectura modificada en sublistas
		
##########################Funcion para crear las sublistas y agregarlas a la listalectura##################################
###Funcion para splitear una cadena de string
###Entrada: Una linea de string
###Retorna una lista con los string spliteados
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
	
#################################################Funcion para procesar las listas################################################	
### Funcion que recibe la lista ya ordenada para procesar cada linea de codigo en SML
def procesar(listalectura):
	for i in listalectura:
		if i[0] == 'val':
			variable=i[1]
			res=procesarVal(i[3:])
			if estaEnValores(variable)==False:
				valores.append([variable,res])
			else:
				for l in valores:
					if variable in l:
						l[1]=res
				
			
def estaEnValores(variable):
	for lista in valores:
		if variable in lista:
			return True
	return False
	
#######################################################Funcion para procesar los Val###############################
###Funcion encargada de llamar a otras funciones para realizarle una operacion que sea necesaria a la asociacion
###Entrada: Una lista a evaluar para asociar
###Salida: Una llamada a otra funcion	
def procesarVal(asignacion):
	if asignacion[0]=="#":
		return procesarNumeral(asignacion)
	elif asignacion[0]=='if':
		return procesarIf(asignacion)
	else:
		res= concatenar(asignacion)
		if stringOvariable(res)!="String":
			return res
		else:
			return eval(res)

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
	
	
################################################Funcion para procesar Numeral#############################################
###Entrada:
###Salida: 
def procesarNumeral(lista):
   temp=getValor(lista[2])
   return temp[eval((lista[1]))-1]
 
####################################Funcion de prueba para estar leyendo el contenido de las listas#####################################		
def imprimir(lista):
	for i in lista:
		print i
		
#######################################FUNCION CONCATENAR
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
                elif i == "=":
					temp+="=="
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
	
	
###FUNCION PROCESAR IF
##Recibe: lista que empieza con 'if'
##Salida: retorna el resultado del if
def procesarIf(lista):
	i=1;
	condicion = []
	caso1=[]
	caso2=[]
	while lista[i] != 'then':
		condicion.append(lista[i])
		i+=1
	i+=1
	while lista[i] != 'else':
		caso1.append(lista[i])
		i+=1
	i+=1
	while i < len(lista):
		caso2.append(lista[i])
		i+=1
		
	if eval(concatenar(condicion)):
		return eval(concatenar(caso1))
	else:
		return eval(concatenar(caso2))

