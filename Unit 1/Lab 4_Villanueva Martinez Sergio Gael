class Producto:
    def __init__(self, nombre, precio, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo


class ServicioEmail:
    def actualizar(self, estado):
        print(f"Email: El estado del pedido es {estado}")


class ServicioSMS:
    def actualizar(self, estado):
        print(f"SMS: Su pedido está {estado}")


class AplicacionMovil:
    def actualizar(self, estado):
        print(f"App: Estado actualizado a {estado}")


class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.productos = []
        self.estado = "CREADO"
        self.observadores = []

    def registrar_observador(self, observador):
        self.observadores.append(observador)

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0

        for producto in self.productos:
            if producto.tipo == "electronico":
                total += producto.precio * 1.16

            elif producto.tipo == "ropa":
                total += producto.precio * 1.08

            elif producto.tipo == "alimento":
                total += producto.precio * 1.00

        return total

    def cambiar_estado(self, nuevo_estado):
        if self.estado != nuevo_estado:
            self.estado = nuevo_estado

            for observador in self.observadores:
                observador.actualizar(self.estado)

    def mostrar_pedido(self):
        print(f"\nPedido #{self.numero}")
        print(f"Cliente: {self.cliente}")
        print(f"Estado: {self.estado}")

        print("\nProductos:")

        for producto in self.productos:
            print(
                f"- {producto.nombre}: "
                f"${producto.precio:.2f}"
            )

        print(f"\nTotal: ${self.calcular_total():.2f}")


# Programa principal
pedido = Pedido(1001, "Ana")

pedido.registrar_observador(ServicioEmail())
pedido.registrar_observador(ServicioSMS())
pedido.registrar_observador(AplicacionMovil())

pedido.agregar_producto(
    Producto("Laptop", 15000, "electronico")
)

pedido.agregar_producto(
    Producto("Playera", 500, "ropa")
)

pedido.agregar_producto(
    Producto("Cereal", 100, "alimento")
)

pedido.mostrar_pedido()

pedido.cambiar_estado("ENVIADO")

print("\nNuevo estado:", pedido.estado)