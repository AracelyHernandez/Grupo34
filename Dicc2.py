Compras = {"cliente1":["Harina","Huevo","Leche"],
           "cliente2":["Sandia","Manzana","Uvas"],
           "cliente3":["Jamon","Queso","Pan"]}

Compras["cliente2"] = "Pera","Melon","Fresa"

for i, (clave, valor) in enumerate(Compras.items()):
    print(i + 1, clave, ":", valor)