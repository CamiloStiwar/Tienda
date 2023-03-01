import random
from tienda import Tienda
from producto import Producto

nombreTienda = input("Por favor digite el nombre de su tienda: ")
paginaWebTienda = input("Por favor digite la pagina web de su tienda: ")
direcciónTienda = input("Por favor digite la dirección de su tienda: ")

tienda = Tienda(nombreTienda, paginaWebTienda, direcciónTienda)

while True:
    
    operacion = input("Por favor dijite si busca un producto(I), si desea crear uno nuevo (NP), o si desea comprar un producto (V), o si quiere ver el Total de Ventas (TV): ")

    if operacion == "NP":
        nombreProducto = input("Por favor dijite el nombre del producto: ")
        precioProducto = int(input("Por favor dijite el precio del producto: "))
        prod1 = Producto(nombreProducto, precioProducto)  
        tienda.agregarProducto(prod1)
        print(tienda.listaDeProductos)
    elif operacion == "I":
        tienda.imprimirProductosEInventarios()
    elif operacion == "V":
        nombreProducto = input("Ingrese el nombre del producto que desea comprar: ")
        productoEncontrado = tienda.buscarProductoPorNombre(nombreProducto)
        if not productoEncontrado:
            print("El producto no fue encontrado.")
        else:
            cantidadAComprar = int(input("Ingrese la cantidad a comprar: "))
            if productoEncontrado.inventario >= cantidadAComprar:
                total = productoEncontrado.precio * cantidadAComprar
                print(f"Venta exitosa, el total de la venta fue {total} pesos.")
                productoEncontrado.inventario = productoEncontrado.inventario - cantidadAComprar
                tienda.agregarVenta(total)
            else:
                print("No hay inventario suficiente de la referencia que desea comprar.")
    elif operacion == "TV":
        print(tienda.listaDeVentas)
        sumaDeVentas = sum(tienda.listaDeVentas)
        print(sumaDeVentas)
