import string
import random

class Registro_Vehiculo:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Aplicacion:

    def register_vehicle(self, marca: string):
        # create a registry instance
        registry = Registro_Vehiculo()

        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        placa = registry.generate_vehicle_license(vehicle_id)

        # compute the catalogue price
        precio_catalogo = 0
        if marca == "Tesla Model 3":
            precio_catalogo = 60000
        elif marca == "Volkswagen ID3":
            precio_catalogo = 35000
        elif marca == "BMW 5":
            precio_catalogo = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        porcentaje_impuesto = 0.05
        if marca == "Tesla Model 3" or marca == "Volkswagen ID3":
            porcentaje_impuesto = 0.02

        # compute the payable tax
        impuesto = porcentaje_impuesto * precio_catalogo

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"marca: {marca}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {placa}")
        print(f"Payable tax: {impuesto}")

app = Aplicacion()
app.register_vehicle("Tesla Model 3")