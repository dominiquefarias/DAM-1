from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return '''
        <!doctype html>
        <html>
            <head>
                <title>Mi pagina</title>
                <style>
                    h1{color:purple;}
                </style>
            </head>
            <body>
                <h1>Esto es HTML a tope</h1>
            </body>
        </html>
    '''

if __name__=="__main__":
    aplicacion.run(debug=True)
