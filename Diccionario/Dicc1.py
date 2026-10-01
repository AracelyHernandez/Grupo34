Diccionario = {"Nombre": "Elizabeth",
    "Edad": 19,
    "Estado de nacimiento": "Nuevo Leon"
}

for i, (clave, valor) in enumerate(Diccionario.items()):
    print(i + 1, clave, ":", valor)