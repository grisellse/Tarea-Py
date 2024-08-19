# Una veterinaria atiende solamente perros y los registra en una base de datos. Se requiere un programa que lea la informacion basica del perro.
#En esta veterinaria todos los animales que llegan, entran con el estado inicial de No atendido y cuando se registran se cambia automaticamente a Atendido. 
#Por ahora como la veterinaria solo atiende perros, basado en el peso, los registra como 'Perro grande' o 'Perro pequeño'.

class Perro:
    def __init__(self, nombre, raza, edad, peso, color, dueño, estado="No atendido"):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.dueño = dueño
        self.estado = estado
        self.tamano = "Perro grande" if peso >= 10 else "Perro pequeno"

    def registrar(self):
        self.estado = "Atendido"
        print(f"Registrado : {self}")

    def __str__(self):
     def __str__(self):
        return f"{self.nombre} ({self.raza}), {self.tamano}, Edad: {self.edad:.2f} años, Estado: {self.estado}"

if __name__ == "__main__":
    nombre = input("Nombre del perro: ")
    raza = input("Raza: ")
    edad = int(input("Edad: "))
    mes = input("Edad en meses?  (si/no): ").strip().lower()
    if mes == "si":
        edad >= 12 
    peso = float(input("Peso : "))
    color = input("Color: ")
    dueño = input("Nombre del dueño: ")
    
    perro = Perro(nombre=nombre, raza=raza, edad=edad, peso=peso, color=color, dueño=dueño)
    perro.registrar()




