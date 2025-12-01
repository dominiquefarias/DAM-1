persona = {
	"nombre":"Dominique",
  "apellidos":"Farias",
  "correo":"domi@mail.com",
  "edad":19,
  "telefonos":[
  	{	
      "tipo":"fijo",
    	"número":96123455
    },
    {	
      "tipo":"movil",
    	"número":65456546
    }
  ]
}

print(persona)
print(persona["telefonos"][0]["número"])
