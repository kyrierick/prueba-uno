nombre = "SOY"
apellido = "Dalto"

print (f"Hola, {nombre} {apellido}" +" como estas?")
saludo = "Hola, {nombre} {apellido}"
print(saludo)
html = f"<h1>Hola, {nombre} {apellido}</h1>"print(saludo.format(nombre=nombre, apellido=apellido))
print(saludo.format(nombre=nombre.upper(), apellido=apellido.lower()))
print(saludo.format(nombre=nombre.capitalize(), apellido=apellido.capitalize()))

