// Actualizacion de un elemento
db.facturas.updateOne(
    { nombre: 'Dominique' },
    {
        $set:
            { email: "prueba@prueba.com" }
    }
)