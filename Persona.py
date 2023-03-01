
class Persona():
    def __init__(self, nombre, telefono, correo, documento, objetivoVentas, identificacionEmpresarial):
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

        

class Cliente(Persona):
    def __init__(self, nombre, telefono, correo, documento, direccionEnvio, correoFacturacion):
        super().__init__(nombre, telefono, correo, documento)
        self.direccionEnvio = direccionEnvio
        self.correoFacturacion = correoFacturacion
        self.acumuladoCompra = 0