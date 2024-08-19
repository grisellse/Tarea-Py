class Libro:
    def __init__(self, titulo, autor, isbn, anio):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Libro prestado")
        else:
            print("Libro no disponible")

    def devolver(self):
        self.disponible = True
        print("Libro devuelto")

class Usuario:
    def __init__(self, nombre, apellido, numero_socio):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_socio = numero_socio
        self.libros_prestados = []

    def pedirPrestado(self, libro):
        if libro.disponible:
            self.libros_prestados.append(libro)
            libro.prestar()
        else:
            print("Libro no disponible")

    def devolverLibro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            libro.devolver()
        else:
            print("Usuario no tiene este libro prestado")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    # ... (métodos agregarLibro, agregarUsuario, buscarLibro, prestarLibro, devolverLibro)

# Instanciación y uso
biblioteca = Biblioteca()

# Agregar libros y usuarios
libro1 = Libro("Don Quijote", "Cervantes", "978-84-206-3597-5", 1605)
biblioteca.agregarLibro(libro1)

usuario1 = Usuario("Juan", "Pérez", 123)
biblioteca.agregarUsuario(usuario1)

# Prestar un libro
usuario1.pedirPrestado(libro1)

# Buscar un libro
libro_buscado = biblioteca.buscarLibro("Don Quijote")  # Implementar la búsqueda

