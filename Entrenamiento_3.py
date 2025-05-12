el_almacen = {} #el diccionario :)

#Funcion de añadir producto

def añadir_producto():
    try:
        nombre = input("\nIngrese el nombre del producto: ").lower().strip()
        if nombre in el_almacen:
            print("\nEl producto ya existe :0")
        else:
            precio = float(input("\nIngrese el precio del producto: "))
            if precio > 0:
                cantidad = int(input("\nIngrese la cantidad del producto: "))
                el_almacen[nombre] = (precio,cantidad)
                print("\nEl produccto se a añadido correctamente")
            else:
                print("\nEl producto no se encuentra en el almacen :(")
    except ValueError:
        print("\nPor favor ingrese solo valores validos")

#Fucion buscar producto
def consultar_producto():
    try:
        nombre = input("\nIngrese el producto que quiere buscar: ").strip().lower()

        if nombre in el_almacen:
            precio, cantidad = el_almacen[nombre]
            print("\nEl producto se encuentra en el almacen :0")
            print("\nEl precio es: ",precio)
            print("Y hay una cantidad de:",cantidad)
        else:
            print("\nEl producto no se encuentra en el almacen :(")
    except ValueError:
        print("\nPor favor ingrese solo valores validos")

#funcion cambiar el precio de producto         
def actualizar_precios():
    try:
        nombre = input("\nIngrese el nombre del producto que desea cambiar el precio: ").lower().strip()
        if nombre in el_almacen:
            new_price = float(input("\nIngrese el nuevo precio que quieres asignar al producto: "))
            if new_price > 0:
                cantidad = el_almacen[nombre][1]
                el_almacen[nombre] = (new_price,cantidad)
                print("\nEl precio del producto",nombre,"se ha actualizado a:",new_price)
            else:
                print("\nPor favor solo ingresa numero positivos -_-")
        else:
            print("\nEl producto no se encuentra en el almacen :(")
    except ValueError:
        print("\nAsegurece de ingresar los valores validos")

#Funcion Eliminar Productos :0

def eliminar_producto():
    try:
        nombre = input("Ingrese el nombre del producto que quiere eliminar: ").lower().strip()
        if nombre in el_almacen:
            del el_almacen[nombre]
            print("\nEl poducto se h eliminado exitosamente :)")
        else:
            print("\nEl producto no se encuentra en el almacen :(")
    except ValueError:
        print("\nPor favor asegurece de estar ingresando datos validos")

#Funcion calcular valor total del inventario
def Valor_total_almacen():
    try:
        pregunta = input("\n¿Quiere saber el valor total del almacen? (Si/No): ").lower().strip()
        if pregunta == "si":
            calcular_valor = lambda producto: producto[0] * producto[1]
            total_alm = sum(calcular_valor(p) for p in el_almacen.values())
            print("\nEl valor total del almacén es:", total_alm)

        elif pregunta == "no":
            print("\nA bueno ._.")
        else:
            print("Por favor solo ingresa 'Si' o 'No'")
    except ValueError:
        print("Por favor ingrese solo valores validos")

#Mostrar los productos del inventario
def mostrar_todos_productos():
    if len(el_almacen) == 0:
        print("No hay productos en el inventario.")
    else:
        for nombre in el_almacen:
            precio, cantidad = el_almacen[nombre]
            print() #no me dio para hacerlo con "\n" :)
            print(nombre,": Precio =",precio,"Cantidad =",cantidad)

#Funcion para el menu
def menu():
    while True:
        print("\n--------MENU--------")
        print("1. Agregar producto")
        print("2. Ver producto")
        print("3. Cambiar precio")
        print("4. Eliminar producto")
        print("5. Ver valor total del inventario")
        print("6. Mostrar todos los productos")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            añadir_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            actualizar_precios()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            Valor_total_almacen()
        elif opcion == "6":
            mostrar_todos_productos()
        elif opcion == "0":
            print("Gracias por usar el programa :)")
            break
        else:
            print("\nOpción no válida. Intenta otra vez.")
#Inicia (Por eso no funcionaba -_-)
menu()