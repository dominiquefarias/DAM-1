from flask import Flask

aplicacion = Flask(__name__)
@aplicacion.route("/")
def raiz():
    return'''
    <!DOCTYPE html>
<html lang="es">
    <head>
        <title>DOMASAblog</title>
        <meta charset="utf-8">
        <style>
            body{background-color: aliceblue;font-family: sans-serif;}
            header,main,footer{background: white;padding:20px;margin: auto;width: 600px;}
            header,footer{text-align: center;}
            main{color: violet;}
        </style>
    </head>
    <body>
        <header><h1>DOMASAblog</h1></header>
        <main>
            <article>
                <h3>Titulo del articulo</h3>
                <time datetime="2025-10-16"></time>
                <p>DominiqueFarías</p>
                <p>Este es el contenido de un articulo ficticio</p>
            </article>
        </main>
        <footer>(@)2025 DominiqueFarías</footer>
    </body>
</html>
    '''
    
if __name__ == "__main__":
    aplicacion.run(debug=True)
