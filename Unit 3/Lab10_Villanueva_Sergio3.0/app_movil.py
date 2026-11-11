class SuscripcionExpiradaError(Exception):
    """Se lanza cuando un usuario intenta usar una función restringida
    sin tener una suscripción activa."""
    pass


class PuntosInsuficientesError(Exception):
    """Se lanza cuando una transacción excede el saldo de gemas disponible."""
    pass


class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50):
        if gemas < 0:
            raise ValueError("las gemas no pueden ser negativas")
        self.username = username
        self.gemas = gemas
        self.racha_dias = 1
        self.notificaciones_activas = True

    def ganar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("la cantidad debe ser mayor a 0")
        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("la cantidad debe ser mayor a 0")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError("No tienes suficientes puntos.")
        self.gemas -= cantidad
        return self.gemas


class PerfilPro(PerfilMovil):
    def __init__(self, username: str, gemas: int = 50, meses_suscripcion: int = 1):
        super().__init__(username, gemas)
        if meses_suscripcion <= 0:
            raise ValueError("los meses de suscripción deben ser mayores a 0")
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0 or not self.es_pro:
            self.meses_suscripcion = max(self.meses_suscripcion, 0)
            self.es_pro = False
            raise SuscripcionExpiradaError("Tu suscripción ha expirado.")
        return "Descarga offline completada con éxito."
