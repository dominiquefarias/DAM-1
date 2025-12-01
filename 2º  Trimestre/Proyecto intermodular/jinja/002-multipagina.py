from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")
	
if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/sobremi")
def inicio():
    return render_template("sobremi.html")
	
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/contacto")
def inicio():
    return render_template("contacto.html")
	
if __name__ == "__main__":
    app.run(debug=True)


