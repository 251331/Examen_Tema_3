# Clase hija de Motorizado, para Automóviles
from motorizado import Motorizado
from rodaje import Rodaje
class Automovil(Motorizado, Rodaje):
    def __init__(self):
        Motorizado.__init__(self)
        Rodaje.__init__(self)
        self._numero_puertas = 0  # Atributo específico de Automóvil
        self._tipo_vehiculo = ""
        self._techo_solar = False
        self._numero_bolsas_aire = 0
        self._sistema_alarma = False
        self._sistema_frenos = ""
        self._asistencia_seguro = ""
        self._sensores_lluvia = False

    def get_numero_puertas(self):
        return self._numero_puertas

    def set_numero_puertas(self, numero_puertas):
        self._numero_puertas = numero_puertas

    def get_tipo_vehiculo(self):
        return self._tipo_vehiculo

    def set_tipo_vehiculo(self, tipo_vehiculo):
        self._tipo_vehiculo = tipo_vehiculo

    def get_techo_solar(self):
        return self._techo_solar

    def set_techo_solar(self, techo_solar):
        self._techo_solar = techo_solar

    def get_numero_bolsas_aire(self):
        return self._numero_bolsas_aire

    def set_numero_bolsas_aire(self, numero_bolsas_aire):
        self._numero_bolsas_aire = numero_bolsas_aire

    def get_sistema_alarma(self):
        return self._sistema_alarma

    def set_sistema_alarma(self, sistema_alarma):
        self._sistema_alarma = sistema_alarma

    def get_sistema_frenos(self):
        return self._sistema_frenos

    def set_sistema_frenos(self, sistema_frenos):
        self._sistema_frenos = sistema_frenos

    def get_asistencia_seguro(self):
        return self._asistencia_seguro

    def set_asistencia_seguro(self, asistencia_seguro):
        self._asistencia_seguro = asistencia_seguro

    def get_sensores_lluvia(self):
        return self._sensores_lluvia

    def set_sensores_lluvia(self, sensores_lluvia):
        self._sensores_lluvia = sensores_lluvia

    def mostrar_Informacion_Automovil(self):
        motorizado_info = super().mostrar_Informacion_Motorizado()
        rodaje_info = super().mostrar_Informacion_Rodaje()
        return [
            *motorizado_info,
            *rodaje_info,
            f"Número de puertas: {self._numero_puertas}",
            f"Tipo de vehículo: {self._tipo_vehiculo}",
            f"Cuenta con techo solar: {self._techo_solar}",
            f"Numero de bolsas aire: {self._numero_bolsas_aire}",
            f"Cuenta con istencia alarma: {self._sistema_alarma}",
            f"Tipo de sistema de frenos: {self._sistema_frenos}",
            f"Cuenta con Asistencia seguro: {self._sistema_alarma}",
            f"Equipa Sensores lluvia: {self._sensores_lluvia}",
        ]
