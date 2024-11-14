# Clase hija de Motorizado, para Aviones
from motorizado import Motorizado
class Avion(Motorizado):
    def __init__(self):
        super().__init__()
        self._tipo_avion = ""
        self._peso_maximo_despegue = 0.0
        self._envergadura = 0.0
        self._altitud_maxima = 0.0
        self._sistema_oxigeno = ""
        self._sistemas_safety = ""
        self._sistemas_autopiloto = ""
        self._pista_minima_despegue = 0.0
        self._pista_minima_aterrizaje = 0.0
        self._tipo_vuelo = ""
        self._antena_comunicaciones = ""
        self._clase_servicio = ""

    def get_tipo_avion(self):
        return self._tipo_avion

    def set_tipo_avion(self, tipo_avion):
        self._tipo_avion = tipo_avion

    def get_peso_maximo_despegue(self):
        return self._peso_maximo_despegue

    def set_peso_maximo_despegue(self, peso):
        self._peso_maximo_despegue = peso

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

    def get_sistemas_safety(self):
        return self._sistemas_safety

    def set_sistemas_safety(self, sistemas_safety):
        self._sistemas_safety = sistemas_safety

    def get_sistemas_autopiloto(self):
        return self._sistemas_autopiloto

    def set_sistemas_autopiloto(self, sistemas_autopiloto):
        self._sistemas_autopiloto = sistemas_autopiloto

    def get_pista_minima_despegue(self):
        return self._pista_minima_despegue

    def set_pista_minima_despegue(self, peso):
        self._pista_minima_despegue = peso

    def get_pista_minima_aterrizaje(self):
        return self._pista_minima_aterrizaje

    def set_pista_minima_aterrizaje(self, pista_minima_aterrizaje):
        self._pista_minima_aterrizaje = pista_minima_aterrizaje

    def get_tipo_vuelo(self):
        return self._tipo_vuelo

    def set_tipo_vuelo(self, tipo_vuelo):
        self._tipo_vuelo = tipo_vuelo

    def get_antena_comunicaciones(self):
        return self._antena_comunicaciones

    def set_antena_comunicaciones(self, antena_comunicaciones):
        self._antena_comunicaciones = antena_comunicaciones

    def get_clase_servicios(self):
        return self._clase_servicio

    def set_clase_servicios(self, clase_servicio):
        self._clase_servicio = clase_servicio


    def mostrar_Informacion_Avion(self):
        motorizado_info = super().mostrar_Informacion_Motorizado()
        return [
            *motorizado_info,
            f"Tipo de avión: {self._tipo_avion}",
            f"Peso maximo de Despegue en Kg: {self._peso_maximo_despegue}",
            f"Envergadura en mts: {self._envergadura}",
            f"Altitud maxima em mts: {self._altitud_maxima}",
            f"Maneja Sistema oxigeno: {self._sistema_oxigeno}",
            f"Sistema Safety: {self._sistemas_safety}",
            f"Sistema autopiloto: {self._sistemas_autopiloto}",
            f"Pista Minima Despegue: {self._pista_minima_despegue}",
            f"Pista Minima Aterrizaje: {self._pista_minima_aterrizaje}",
            f"Tipo Vuelo: {self._tipo_vuelo}",
            f"Antena comunicaciones: {self._antena_comunicaciones}",
            f"Clases servicios: {self._clase_servicio}"
        ]