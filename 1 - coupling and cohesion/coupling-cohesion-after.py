import string
import random

class Info_vehiculo:
    
    def __init__(self, marca, electrico, precio_catalogo):
        self.marca = marca
        self.electrico = electrico
        self.precio_catalogo = precio_catalogo

    def compute_tax(self):
        porcentaje_impuesto = 0.05
        if self.electrico:
            porcentaje_impuesto = 0.02
        return porcentaje_impuesto * self.precio_catalogo

    def print(self):
        print(f"marca: {self.marca}")
        print(f"Payable tax: {self.compute_tax()}")

class Vehiculo:

    def __init__(self, id, placa, info):
        self.id = id
        self.placa = placa
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.placa}")
        self.info.print()


class Registro_Vehiculo:

    def __init__(self):
        self.Vehiculo_info = { }
        self.add_Vehiculo_info("Tesla Model 3", True, 60000)
        self.add_Vehiculo_info("Volkswagen ID3", True, 35000)
        self.add_Vehiculo_info("BMW 5", False, 45000)
        self.add_Vehiculo_info("Tesla Model Y", True, 75000)

    def add_Vehiculo_info(self, marca, electrico, precio_catalogo):
        self.Vehiculo_info[marca] = Info_vehiculo(marca, electrico, precio_catalogo)

    def generate_Vehiculo_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_Vehiculo_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_Vehiculo(self, marca):
        id = self.generate_Vehiculo_id(12)
        placa = self.generate_Vehiculo_license(id)
        return Vehiculo(id, placa, self.Vehiculo_info[marca])


class Aplicacion:

    def register_Vehiculo(self, marca: string):
        # create a registry instance
        registry = Registro_Vehiculo()

        Vehiculo = registry.create_Vehiculo(marca)

        # print out the Vehiculo information
        Vehiculo.print()

app = Aplicacion()
app.register_Vehiculo("Tesla Model Y")