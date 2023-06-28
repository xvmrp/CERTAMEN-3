import os
os.system("cls")

listacodigo = []
listaNombre = []
listaCategoria = []
listaPrecio = []
listaStock = []

nombre = input("Ingrese nombre usuario: ")
apellido = input("Ingrese nombre su apellido: ")


Menu = """
Selecione una opcion
1) Registrar producto
2) Buscar producto
3) Listar producto
4) Salir
Digite opcion: """

def registrarproducto():
    while True:
            try:
                if opc == 1:
                    while True:
                        try:
                            cod = int(input("Ingrese codigo: "))
                            if cod == 6:
                                listacodigo.append(cod)
                                break
                            else:
                                print("Error de codigo")
                        except:
                            print("Excepcion de codigo")
                    while True:
                        try:
                            nom = input("Ingrese nombre: ")
                            if len(str(nom)) < 2 or len(str(nom)) > 50:
                                listaNombre.append(nom)
                                break
                            else:
                                print("Error de nombre")
                        except:
                            print("Excepcion de nombre")
                    while True:
                        try:
                            categoria = input("Ingrese categoria: ")
                            listaCategoria.append(categoria)
                            break
                        except:
                            print("Excepcion de categoia")
                    while True:
                        try:
                            precio = int(input("Ingrese precio: "))
                            if precio < 0:
                                listaPrecio.append(precio)
                                break
                            else:
                                print("Error de precio")
                        except:
                            print("Excepcion de precio")
                    while True:
                        try:
                            stock = int(input("Ingrese stock: "))
                            if stock < 0:
                                print("Hay stock")
                            else:
                                print("Stock no disponible")
                            listaStock.append(stock)
                            break
                        except:
                            print("Excepcion de stock")
            except:
               print("Excepcion de registro de producto")
            break

def buscarproducto():
                    cat_producto = input("Categoria a mostrar")
                    print(f"Lista de producto: {cat_producto} ")
                    print(f"Codigo, Nombre, Categoria, Precio, Stock, Stockbajo")
                    print("----------------------------------------------------")
                    for i in range (len(listacodigo)):
                        if cat_producto.lower() == listacodigo[i].lower():
                            print(f"{i+1} | {listacodigo[i]:6d}|{listaNombre[i]:50s}|{listaCategoria[i]:40s}|{listaPrecio[i]:10d}|{listaStock[i]:6d}|")
                            print("----------------------------------------------------")

def listarpoducto():
                    print("|COD| NOMBRE | CATEGORIA | PRECIO | STOCK|")
                    total_stock = 0
                    for i in range(len(listacodigo)):
                        if total_stock[1] <5:
                            stock = "SI"
                            total_stock += 1
                        else:
                            stock = "NO"
                    print("No hay stock")
                    print("--------------------")
                    print(f"{listacodigo[i]:6d}{listaNombre[i]:50s}{listaCategoria[i]:40s}{listaPrecio[i]:10d}{listaStock[i]:6d}")
                    print("--------------------")

           
while True:
    try:
        opc = int(input(Menu))
        if opc == 4:
            print("Adios", nombre, apellido)
            break
        while True:
            try:
                if opc == 1:
                    def registrarproducto():
                        break
            except:
                print("Excepcion de registro")
                break           
        while True:
            try:
                if opc == 2:
                    def buscarproducto():
                        break
            except:
                print("Excepcion de buscar producto")
                break
        while True:
            try:
                if opc == 3:
                     def listarpoducto():
                          break
            except:
                print("Excepcion de listar producto")
    except:
        print("Excepcion de menu")