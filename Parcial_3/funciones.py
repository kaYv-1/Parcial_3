import json
def agregar_categoria(nombre):
    with open("biblioteca.json","r") as jsonLectura:
        leer_json = json.load(jsonLectura)
        agregar_cat = {
            "CategoriaID": len(leer_json["Categoria"])+1,
            "Nombre": nombre
        }
    leer_json["Categoria"].append(agregar_cat)
    with open ("biblioteca.json","w") as jsonEscritura:
        json.dump(leer_json, jsonEscritura, indent=4)
        print("Categoría agregada correctamente ")

def editar_categoria(id):
    contador = 0
    with open("biblioteca.json","r") as jsonLectura:
        leer_json = json.load(jsonLectura)
        for i in leer_json["Categoria"]:
            if i["CategoriaID"] == id:
                print("Encontrado")
                break
            elif contador == range(leer_json["Categoria"])-1 and i["CategoriaID"] != id: #######
                print("No encontrado")
        contador += 1

    leer_json["Categoria"][contador]["Nombre"] = input("Ingrese nuevo nombre: ")
    with open ("biblioteca.json","w") as jsonEscritura:
        json.dump(leer_json, jsonEscritura, indent=4)
        print("Categoría editada correctamente ")

def eliminar_categoria(id):
    with open("biblioteca.json","r") as jsonLectura:
        leer_json = json.load(jsonLectura)
        print(leer_json["Categoria"])
        id = int(input("Ingrese un ID: "))
        categorias = leer_json["Categoria"]

        for i, categoria in enumerate(categorias):
            if categoria ["CategoriaID"] == id:
                categorias.remove(i)
                print("La categoría ha sido eliminada con éxito ")
                break
            if not categorias:
                print("Categoria no encontrada")
            for id_n, categoria in enumerate(categorias, start=1):### El (start=1) indica que tiene que comenzar a ennumerar clientes desde el 1
                categoria["CategoriaID"] == id_n
                print("La lista se actalizó con éxito")
                break
    with open ("biblioteca.json","w") as jsonEscritura:
        json.dump(leer_json, jsonEscritura, indent=4)

def reportes():
    with open ("reportes.json","w") as jsonEscritura:
        leer_json.append(agregar_categoria)
        json.dump(leer_json, jsonEscritura, indent=4)
    with open("reportes.json","r") as jsonLectura:
        leer_json = json.load(jsonLectura)
    leer_json["Categoria"].append(agregar_categoria)