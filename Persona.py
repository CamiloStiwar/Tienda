
class Persona():
    def __init__(self, nombre, telefono, correo, documento):
        self.nombre = nombre
        self.telefono = telefono       
        self.correo = correo
        self.documento = documento

class Vendedor(Persona):
    def __init__(self, nombre, telefono, correo, documento, objetivoVentas, identificacionEmpresarial):
        super().__init__(nombre,telefono,correo,documento)
        self.objetivoVentas = objetivoVentas
        self.identificacionEmpresarial = identificacionEmpresarial
        self.acumuladoVentas = 0

    def imprimirNombre(self):
        print(self.nombre)

    def acumular(self, monto):
        self.acumuladoVentas = self.acumuladoVentas + monto

    def revisarObjetivo(self):
        if self.acumuladoVentas >= self.objetivoVentas:
            print("Has llegado al objetivo de ventas que tenias")
            print(f"Objetivo: {self.objetivoVentas}")
            print(f"Acumulado: {self.acumuladoVentas}")
            print("Felicitaciones")
        else:
            print(f"Aún no se ha cumplido el objetivo. Faltan {self.objetivoVentas - self.acumuladoVentas}")

        

class Cliente(Persona):
    def __init__(self, nombre, telefono, correo, documento, direccionEnvio, correoFacturacion):
        super().__init__(nombre, telefono, correo, documento)
        self.direccionEnvio = direccionEnvio
        self.correoFacturacion = correoFacturacion
        self.acumuladoCompra = 0