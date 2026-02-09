// Listado de facturas:
db["facturas"].find()

// Insertar un elemento:
db.facturas.insertOne({
    nombre: "Dominique",
    apellidos: "Farias",
    telefono: "+34 123456789",
    email: "dominique@mail.com"
})

// Asegúrate de estar en la base de datos correcta primero (ej: use miTienda)

db.facturas.insertMany([
    {
        nombre: "Dominique",
        apellidos: "Farias",
        telefono: "+34 123456789",
        email: "dominique@mail.com"
    },
    {
        nombre: "Jose",
        apellidos: "Lopez",
        telefono: "+34 3425325",
        email: "info@jose.com"
    },
    {
        nombre: "Julia",
        apellidos: "Martinez",
        telefono: "+34 234535245",
        email: "info@julia.com"
    }
]);