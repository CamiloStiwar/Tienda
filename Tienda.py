import random

class Tienda:
    def __init__(self, nombre, paginaWeb, direccion, rangoDescuento):
        self.nombre = nombre
        self.paginaWeb = paginaWeb
        self.direccion = direccion
        self.listaDeProductos = []
        self.listaDeVendedores = []
        self.listaDeClientes = []
        self.rangoDescuento = rangoDescuento
        self.listaDeVentas = []
    def agregarProducto(self, productoAAgregar):
        self.listaDeProductos.append(productoAAgregar)
    def imprimirProductosEInventarios(self):
        for producto in self.listaDeProductos:
            print("________")
            print("Producto: ",producto.nombre)
            print("Inventario: ",producto.inventario)
            print("________")
    def buscarProductoPorNombre(self,nombreProductoABuscar):
        for producto in self.listaDeProductos:
            if producto.nombre == nombreProductoABuscar:
                return producto
    def agregarVenta(self, ventaAAgregar):
        self.listaDeVentas.append(ventaAAgregar)
    def agregarVendedor(self, vendedor):
        self.listaDeVendedores.append(vendedor)
    def buscarVendedorPorDocumento(self, documento):
        for vendedor in self.listaDeVendedores:
            if vendedor.documento == documento:
                return vendedor
            return False
    def agregarCliente(self, cliente):
        self.listaDeClientes.append(cliente)
    def buscarClientePorDocumento(self, documento):
        for cliente in self.listaDeClientes:
            if cliente.documento == documento:
                return cliente
            return False
