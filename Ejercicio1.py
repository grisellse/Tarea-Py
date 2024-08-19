# Una veterinaria atiende solamente perros y los registra en una base de datos. Se requiere un programa que lea la informacion basica del perro.
#En esta veterinaria todos los animales que llegan, entran con el estado inicial de No atendido y cuando se registran se cambia automaticamente a Atendido. 
#Por ahora como la veterinaria solo atiende perros, basado en el peso, los registra como 'Perro grande' o 'Perro pequeño'.


#defonimos la clase
class Perro:
    #Constructor de la clase y sus atributos de la clase perro
    def __init__(self, nombre, raza, edad, peso, color, dueño, estado="No atendido", edad_n="años"):
        self.nombre = nombre # el nombre del perro
        self.raza = raza # raza del perro
        self.edad = edad # edad del perro
        self.peso = peso # peso del perro
        self.color = color # color del perrito
        self.dueño = dueño # el nombre del dueno
        self.estado = estado # el estado del perro, si esta atendido o no
        self.edad_n = edad_n # edad en meses o en años
        self.tamano = "Perro grande" if peso >= 10 else "Perro pequeño"
        # el perro es grande o pequeno segun el peso

    #Metodo para regstrar al perro
    def registrar(self):
        self.estado = "Atendido"
        print(f"Registrado: {self}")
    # Camba el estado a Atendido

    #Metodo para devolver la representacion en texto
    def __str__(self):
        #Muestra la informacion completa del perro
        return f"{self.nombre} ({self.raza}), {self.tamano}, Edad: {self.edad:.2f} {self.edad_n}, Estado: {self.estado}"
    
    #Datos de entrada 
if __name__ == "__main__":
    #Pide la informacion del perro
    nombre = input("Nombre del perro: ")
    raza = input("Raza: ")
    edad = int(input("Edad: "))
    mes = input("¿Edad en meses? (si/no): ").strip().lower()#Convierte la respuesta a minúsculas y quita espacios en blanco
    #Pregunta la edad si esta en meses

    if mes == "si":
        edad_n = "meses"
    else:
        edad_n = "años"
        edad = edad  # Mantenede la edad en años como se ingresó
    
    peso = float(input("Peso (kg): "))
    color = input("Color: ")
    dueño = input("Nombre del dueño: ")
    
    #Instanca de la clase perro 
    perro = Perro(nombre=nombre, raza=raza, edad=edad, peso=peso, color=color, dueño=dueño, edad_unidad=edad_n)
    perro.registrar()








