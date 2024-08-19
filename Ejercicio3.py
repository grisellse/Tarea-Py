#Ejercicio 3 Concesionario de Automóviles

class Autos:
    def __init__(self, marca, modelo, año, precio, nacionalidad):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.nacionalidad = nacionalidad
        self.ruedas =  4
        self.capacidad_p = 5
        self.precio_v = self.c_precio_v()

    def seleccionar_nacionalidad(self, nacionalidad):
        if nacionalidad == "1":
            return "Nacional"
        elif nacionalidad == "2":
            return "Importado"

def c_precio_v(self):
    return self.precio * 1.4

def info(self):
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"Año: {self.año}")
    print(f"Precio: {self.precio}")
    print(f"Nacionalidad: {self.nacionalidad}")
    print(f"Ruedas: {self.ruedas}")
    print(f"Capacidad para pasajeros: {self.capacidad_p}")
    print(f"Precio de venta: {self.precio_v}")
    print(f"Precio de compra: {self.precio_compra} USD")
    print(f"Precio de venta: {self.precio_venta:.2f} USD")

# Creamos una lista vacía para almacenar los vehículos
vehiculos = []

# Registramos 10 vehículos
for i in range(10):
  print(f"\nVehículo {i + 1}:")
  marca = input("Marca: ")
  modelo = input("Modelo: ")
  año = input("Año: ")
  precio_compra = float(input("Precio de compra: "))
  nacionalidad = input("Nacionalidad (Nacional(1)/Importado(2)): ")
  vehiculo = Autos(marca, modelo, año, precio_compra, nacionalidad)
 

