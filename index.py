from flask import Flask, render_template

app = Flask(__name__) # Indicar que es el archivo principal y guardarlo en app para guardar las rutas 

# Crear una ruta para la página principal
@app.route('/')
def home():
    # return 'Home Page'
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Validar si es la página principal
if __name__ == '__main__':
    app.run(debug=True)

 
