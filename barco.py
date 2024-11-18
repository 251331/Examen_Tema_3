# Clase hija de Motorizado, para Barcos
from motorizado import Motorizado
class Barco(Motorizado):
    def __init__(self):
        super().__init__()
        self._camarotes = 0
        self._equipo_salvavidas = 0
        self._sistema_navegacion = ""
        self._tipo_poniente = ""
        self._sistema_vapor = ""

    def get_camarotes(self):
        return self._camarotes

    def set_camarotes(self, camarotes):
        self._camarotes = camarotes

    def get_equipo_salvavidas(self):
        return self._equipo_salvavidas

    def set_equipo_salvavidas(self, equipo_salvavidas):
        self._equipo_salvavidas = equipo_salvavidas

    def get_sistema_navegacion(self):
        return self._sistema_navegacion

    def set_sistema_navegacion(self, sistema_navegacion):
        self._sistema_navegacion = sistema_navegacion
        return self

    def get_tipo_poniente(self):
        return self._tipo_poniente

    def set_tipo_poniente(self, tipo_poniente):
        self._tipo_poniente = tipo_poniente
        return self

    def get_sistema_vapor(self):
        return self._sistema_vapor

    def set_sistema_vapor(self, sistema_vapor):
        self._sistema_vapor = sistema_vapor
        return self

    def mostrar_Informacion_Barco(self):
        motorizado_info = super().mostrar_Informacion_Motorizado()
        return [
            *motorizado_info,
            f"Total de Camarotes: {self._camarotes}",
            f"Con cuantos Equipos de salvavidas cuenta: {self._equipo_salvavidas}",
            f"Sistema navegacion que integra: {self._sistema_navegacion}",
            f"Tipo de poniente que maneja: {self._tipo_poniente}",
            f"Cuenta con Sistema de vapor?: {self._sistema_vapor}",
        ]