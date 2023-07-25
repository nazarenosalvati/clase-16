# Creamos clase padre "Persona"
class Persona:
    def __init__(self, nombre, apellido, edad):
         self.nombre = nombre
         self.apellido = apellido
         self.edad = edad

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Creamos clase hija "cliente" mediante herencia.
# Agregamos atributos contacto y condicion frente al iva.
# Agregamos métodos para visualizar y actualizar datos del cliente.
class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, contacto, condiva):
        super().__init__(nombre, apellido, edad)
        self.contacto = contacto
        self.condiva = condiva

    def ver_cliente(self):
         return f"Cliente: {self.nombre} {self.apellido}, Edad: {self.edad}, Contacto: {self.contacto}, Condición frente al IVA: {self.condiva}"

    def actualizar_contacto(self, nuevo_contacto):
        self.contacto = nuevo_contacto
        return "El contacto ha sido actualizado"
