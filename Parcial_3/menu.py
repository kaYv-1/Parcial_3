import funciones, os, time

while True:
    print("*****************************")
    print("*        MUNDO LIBRO        *")
    print("*****************************")
    time.sleep(1)
    print("[1] - Mantenedor de categorias")
    print("[2] - Reportes")
    print("[3] - Salir")
    opc = int(input("Ingrese opción: "))
    
    if opc == 1:
        while True:
            print("[1] - Agregar categoría")
            print("[2] - Editar categoría")
            print("[3] - Eliminar categoría")
            print("[4] - Buscar categoría")
            print("[5] - Volver")
            opc2 = int(input("Ingrese opción válida: "))
            if opc2 == 1:
                nombrecat = input("Ingrese el nombre de la nueva categoria: ")
                funciones.agregar_categoria(nombre=nombrecat)
            elif opc2 == 2:
                funciones.editar_categoria(int(input("Ingrese el ID que quiere editar: ")))
            elif opc2 == 3:
                funciones.eliminar_categoria(int(input("Ingresa el id de la categoria que desea borrar: ")))
            elif opc2 == 4:
                break
            elif opc2 == 5:
                os.system("cls")
                break
    if opc ==2:
        funciones.reportes()
    if opc == 3:
        os.system("cls")
        break