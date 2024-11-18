# Clase hija de Motorizado, para Aviones
from motorizado import Motorizado
class Avion(Motorizado):
    def __init__(self):
        super().__init__()
        self._envergadura = 0.0
        self._altitud_maxima = 0.0
        self._sistema_oxigeno = 0
        self._pista_minima_despegue = 0.0
        self._pista_minima_aterrizaje = 0.0

    def get_envergadura(self):
        return self._envergadura

    def set_envergadura(self, envergadura):
        self._envergadura = envergadura

    def get_altitud_maxima(self):
        return self._altitud_maxima

    def set_altitud_maxima(self, altitud_maxima):
        self._altitud_maxima = altitud_maxima

    def get_sistema_oxigeno(self):
        return self._sistema_oxigeno

    def set_sistema_oxigeno(self, sistema_oxigeno):
        self._sistema_oxigeno = sistema_oxigeno

    def get_pista_minima_despegue(self):
        return self._pista_minima_despegue

    def set_pista_minima_despegue(self, peso):
        self._pista_minima_despegue = peso

    def get_pista_minima_aterrizaje(self):
        return self._pista_minima_aterrizaje

    def set_pista_minima_aterrizaje(self, pista_minima_aterrizaje):
        self._pista_minima_aterrizaje = pista_minima_aterrizaje


    def mostrar_Informacion_Avion(self):
        motorizado_info = super().mostrar_Informacion_Motorizado()
        return [
            *motorizado_info,
            f"Envergadura en mts: {self._envergadura}",
            f"Altitud maxima en mts sobre nivel del mar: {self._altitud_maxima}",
            f"Cuantos Sistemas oxigeno maneja: {self._sistema_oxigeno}",
            f"Pista Minima Despegue: {self._pista_minima_despegue}",
            f"Pista Minima Aterrizaje: {self._pista_minima_aterrizaje}",
        ]