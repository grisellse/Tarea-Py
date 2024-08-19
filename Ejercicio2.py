# Ejercicio 2

# Definimos la clase Papeleria
class Papeleria:
  # Constructor de la clase, se llama cuando se crea un objeto de la clase
  def __init__(self, producto, tipo, marca, precio):
    # Atributos de la clase
    self.producto = producto  # Nombre del producto
    self.tipo = tipo  # Tipo del producto (Cuaderno o Lápiz)
    self.marca = marca  # Marca del producto (HOJITAS o RAYAS)
    self.precio = precio  # Precio de compra del producto
    # Calculamos el precio de venta multiplicando el precio de compra por 1.3
    self.precio_venta = self.calprecio_venta()

  # Método para calcular el precio de venta
  def calprecio_venta(self):
    # Regresa el precio de venta calculado
    return self.precio * 1.3

  # Método para mostrar información del producto
  def info(self):
    # Imprime el nombre del producto
    print(f"Nombre del producto: {self.producto}")
    # Imprime el tipo del producto
    print(f"Tipo: {self.tipo}")
    # Imprime el precio de compra del producto
    print(f"Precio de Compra: {self.precio} USD")
    # Imprime el precio de venta del producto con dos decimales
    print(f"Precio de Venta: {self.precio_venta:.2f} USD")

# Creamos una lista vacía para almacenar los artículos
articulos = []

# Registramos dos artículos
for i in range(2):
  # Imprime el número del artículo que se está registrando
  print(f"\nArtículo {i + 1}:")
  # Pide el nombre del artículo
  nombre = input("Nombre del artículo: ")
  # Pide el tipo del artículo (Cuaderno o Lápiz)
  tipo = input("Tipo del artículo (Cuaderno/Lápiz): ")
  # Pide el precio de compra del artículo
  precio_compra = float(input("Precio del artículo: "))
  # Crea un objeto de la clase Papeleria con los datos ingresados
  articulo = Papeleria(nombre, tipo, "HOJITAS" if tipo == "Cuaderno" else "RAYAS", precio_compra)
  # Agrega el artículo a la lista
  articulos.append(articulo)

# Muestra la información de cada artículo en la lista
for articulo in articulos:
  articulo.info()