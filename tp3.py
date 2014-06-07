""" Tarea Programa 3,
	Realizado por:  Andres Fernadez,
					Luigui Madrigal,
					Jose Maria Rojas"""

import os
import lecturasml
from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory
from werkzeug import secure_filename

app = Flask("Sml")#instancia de la aplicacion web con Flask
app.config['UPLOAD_FOLDER'] = 'uploads/'#carpeta donde se subira el archivo
app.config['ALLOWED_EXTENSIONS'] = set(['sml','png','jpg', 'pdf'])

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']

#pagina inicial
@app.route('/')
def home():
	return render_template('index.html')
	
#ruta donde se procede el archivo subido
@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['file']#obtiene el nombre del archivo
	if file and allowed_file(file.filename):#verifica que el archivo tenga una extension valida
		filename = secure_filename(file.filename)#convierte el archivo en seguro
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))#guarda el archivo en la carpeta 
		return redirect(url_for('resultado', filename = filename))#redirecciona hacia la pagina para mostrar
		
#ruta para mostrar el resultado
@app.route('/<filename>')
def resultado(filename):
	lecturasml.ejecutar(filename)
	ae = lecturasml.getAmbienteEstatico()
	ad = lecturasml.getAmbienteDinamico()
	return render_template('resultado.html', ae=ae, ad=ad)
		
#ruta que espera un parametro con el nombre del archivo.
#luego lo muestra en el browser	
@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
	
#ejecuta la app
if __name__ == '__main__':
    app.run()#host='192.168.10.103')
