# Nueva clase que hereda solo de Automovil, de forma independiente a Vehiculo y Motorizado
from automovil import Automovil
class Motocicleta(Automovil):
    def __init__(self):
        super().__init__()
        self._tamano_respaldo = ""
        self._indicadores_fluorescentes = False
        self._capacidad_baul = 0.0
        self._tipo_guardabarros = ""
        self._anclaje_asiento_pasajero = ""
        self._tipo_estriberas = ""
        self._proteccion_codo = False
        self._sistema_deteccion_caida = False
        self._soporte_manos = ""
        self._sistema_turbo = False
        self._espejos_retrovisores = ""


    def get_tamano_respaldo(self):
        return self._capacidad_baul

    def set_tamano_respaldo(self, tamano_respaldo):
        self._capacidad_baul = tamano_respaldo

    def get_indicadores_fluorescentes(self):
        return self._indicadores_fluorescentes

    def set_indicadores_fluorescentes(self, indicadores):
        self._indicadores_fluorescentes = indicadores

    def get_capacidad_baul(self):
        return self._capacidad_baul

    def set_capacidad_baul(self, capacidad_baul):
        self._capacidad_baul = capacidad_baul

    def get_tipo_guardabarros(self):
        return self._tipo_guardabarros

    def set_tipo_guardabarros(self, tipo_guardabarros):
        self._tipo_guardabarros = tipo_guardabarros

    def get_anclaje_asiento_pasajero(self):
        return self._anclaje_asiento_pasajero

    def set_anclaje_asiento_pasajero(self, anclaje):
        self._anclaje_asiento_pasajero = anclaje

    def get_tipo_estriberas(self):
        return self._tipo_estriberas

    def set_tipo_estriberas(self, tipo_estriberas):
        self._tipo_estriberas = tipo_estriberas

    def get_proteccion_codo(self):
        return self._proteccion_codo

    def set_proteccion_codo(self, proteccion_codo):
        self._proteccion_codo = proteccion_codo

    def get_sistema_deteccion_caida(self):
        return self._sistema_deteccion_caida

    def set_sistema_deteccion_caida(self, sistema):
        self._sistema_deteccion_caida = sistema

    def get_soporte_manos(self):
        return self._soporte_manos

    def set_soporte_manos(self, soporte_manos):
        self._soporte_manos = soporte_manos

    def get_sistema_turbo(self):
        return self._sistema_turbo

    def set_sistema_turbo(self, sistema):
        self._sistema_turbo = sistema

    def get_espejos_retrovisores(self):
        return self._espejos_retrovisores

    def set_espejos_retrovisores(self, espejos):
        self._espejos_retrovisores = espejos

    def mostrar_Informacion_Motocicleta(self):
        automovil_info = super().mostrar_Informacion_Automovil()
        return [
            *automovil_info,
            f"Tamaño del respaldo en cm: {self._tamano_respaldo}"
            f"Indicadores Fluorescentes: {self._indicadores_fluorescentes}",
            f"Capacidad Baul en kl: {self._capacidad_baul}",
            f"Tipo guardabarros: {self._tipo_guardabarros}",
            f"Anclaje del asiento del pasajero: {self._anclaje_asiento_pasajero}",
            f"Tipo estriberas: {self._tipo_estriberas}",
            f"Proteccion codo: {self._proteccion_codo}",
            f"Sistema de detencion caida: {self._sistema_deteccion_caida}",
            f"Soporte manos: {self._soporte_manos}",
            f"Sistema Turbo: {self._sistema_turbo}",
            f"Espejos retrovisores: {self._espejos_retrovisores}"
        ]
