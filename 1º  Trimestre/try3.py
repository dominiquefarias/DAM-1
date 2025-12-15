from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena = '''
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
    '''
    # bucle que añade los días
    for dia in range(1, 32):
        cadena += '<div>'+str(dia)+'</div>'
        
    cadena += '''
            </body>
        </html>
    '''
    return cadena   

if __name__=="__main__":
    aplicacion.run(debug=True)

