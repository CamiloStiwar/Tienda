import random

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.referencia = "REF: "+str(random.randint(1000, 10000))
        self.inventario = random.randint(0,100)
    def consultarProducto(self):
        print("_____________")
        print("Cuenta: ",self.nombre)
        print("Inventario: ",self.inventario)
        print("_____________")

        

