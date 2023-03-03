import random
from Tienda import Tienda
from Producto import Producto
from Persona import Vendedor
from Persona import Cliente

nombreTienda = input("Por favor digite el nombre de su tienda: ")
paginaWebTienda = input("Por favor digite la pagina web de su tienda: ")
direcciónTienda = input("Por favor digite la dirección de su tienda: ")
rangoTienda = input("Por favor dijite el rango que tiene la tienda para aplicar descuentos: ")

tienda = Tienda(nombreTienda, paginaWebTienda, direcciónTienda, rangoTienda)

while True:
    
    operacion = input("Por favor dijite si busca un producto(I), si desea crear uno nuevo (NP), o si desea comprar un producto (V), o si quiere ver el Total de Ventas (TV), o si quiere crear un nuevo vendedor (NV), o para crear nuevo cliente (NC): ")

    if operacion == "NP":
        nombreProducto = input("Por favor dijite el nombre del producto: ")
        precioProducto = int(input("Por favor dijite el precio del producto: "))
        prod1 = Producto(nombreProducto, precioProducto)  
        tienda.agregarProducto(prod1)
        print(tienda.listaDeProductos)
    elif operacion == "I":
        tienda.imprimirProductosEInventarios()
    elif operacion == "V":
        docVendedor = input("Por favor ingerese el documento del vendedor: ")
        vendedorEncontrado = tienda.buscarVendedorPorDocumento(docVendedor)
        docCliente = input("Por favor ingerese el documento del cliente: ")
        clienteEncontrado = tienda.buscarClientePorDocumento(docCliente)
        
        nombreProducto = input("Ingrese el nombre del producto que desea comprar: ")
        productoEncontrado = tienda.buscarProductoPorNombre(nombreProducto)
        if not productoEncontrado:
            print("El producto no fue encontrado.")
        elif not vendedorEncontrado:
            print("Vendedor no se encontró")
        elif not clienteEncontrado:
            print("Cliente no se encontró")
        else:
            cantidadAComprar = int(input("Ingrese la cantidad a comprar: "))
            if productoEncontrado.inventario >= cantidadAComprar:
                total = productoEncontrado.precio * cantidadAComprar
                print(f"Venta exitosa, el total de la venta fue {total} pesos.")           
                productoEncontrado.inventario = productoEncontrado.inventario - cantidadAComprar
                tienda.agregarVenta(total)
                vendedorEncontrado.acumular(total)
                vendedorEncontrado.revisarObjetivo()
                clienteEncontrado.acumular(total)
                aplicaDescuento = clienteEncontrado.revisarDescuento(tienda.rangoDescuento)
                if aplicaDescuento:
                    total = total*90/100
                    print("El cliente obtuvo un descuento del 10%")
                    print(f"Lo que debes pagar es {total}")
            else:
                print("No hay inventario suficiente de la referencia que desea comprar.")
    elif operacion == "TV":
        print(tienda.listaDeVentas)
        sumaDeVentas = sum(tienda.listaDeVentas)
        print(sumaDeVentas)
    elif operacion == "NV":
        nombre = input("Por favor ingrese el nombre del nuevo vendedor: ")
        telefono = input("Por favor ingrese el telefono del nuevo vendedor: ")
        correo = input("Por favor ingrese el correo del nuevo vendedor: ")
        documento = input("Por favor ingrese el documento del nuevo vendedor: ")
        objetivo = input("Por favor ingrese el objetivo de ventas del nuevo vendedor: ")
        docEmpresarial = input("Por favor ingrese el documento empresarial del nuevo vendedor: ")
        nuevoVendedor = Vendedor(nombre, telefono, correo, documento, objetivo, docEmpresarial)
        tienda.agregarVendedor(nuevoVendedor)
    elif operacion == "NC":
        nombre = input("Por favor ingrese el nombre del nuevo cliente: ")
        telefono = input("Por favor ingrese el telefono del nuevo cliente: ")
        correo = input("Por favor ingrese el correo del nuevo cliente: ")
        documento = input("Por favor ingrese el documento del nuevo cliente: ")
        direccionEnvio = input("Por favor ingrese la dirección del envío del nuevo cliente: ")
        correoFacturacion = input("Por favor ingrese el correo de facturación del nuevo cliente: ")
        nuevoCliente = Cliente(nombre, telefono, correo, documento, direccionEnvio, correoFacturacion)
        tienda.agregarCliente(nuevoCliente)


