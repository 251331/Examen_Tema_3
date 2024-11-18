# Nueva clase que hereda solo de Automovil, de forma independiente a Vehiculo y Motorizado
from automovil import Automovil
class Sedan (Automovil):
    def __init__(self):
        super().__init__()
        self._clasificacion_carro = ""
        self._modelo = ""
        self._sistema_turbo = False
        self._anclaje_asiento_pasajero = ""
        self._sistema_alarma = False

    def get_clasificacion_carro(self):
        return self._clasificacion_carro

    def set_clasificacion_carro(self, carro):
        self._clasificacion_carro = carro

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_sistema_turbo(self):
        return self._sistema_turbo

    def set_sistema_turbo(self, sistema):
        self._sistema_turbo = sistema

    def get_anclaje_asiento_pasajero(self):
        return self._anclaje_asiento_pasajero

    def set_anclaje_asiento_pasajero(self, anclaje):
        self._anclaje_asiento_pasajero = anclaje

    def get_sistema_alarma(self):
        return self._sistema_alarma

    def set_sistema_alarma(self, sistema_alarma):
        self._sistema_alarma = sistema_alarma

    def mostrar_Informacion_Sedan(self):
        automovil_info = super().mostrar_Informacion_Automovil()
        return [
            *automovil_info,
            f"Clasificacion: {self.get_clasificacion_carro()}",
            f"Modelo: {self.get_modelo()}",
            f"Sistema Turbo: {self._sistema_turbo}",
            f"Material de asiento pasajero: {self.get_anclaje_asiento_pasajero}",
            f"Cuenta con alarma antirobo: {self._sistema_alarma}"
        ]
