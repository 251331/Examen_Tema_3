# Clase hija de Motorizado, para Automóviles
from motorizado import Motorizado
from rodaje import Rodaje
class Automovil(Motorizado, Rodaje):
    def __init__(self):
        Motorizado.__init__(self)
        Rodaje.__init__(self)
        self._numero_puertas = 0  # Atributo específico de Automóvil
        self._numero_bolsas_aire = 0
        self._asistencia_seguro = ""
        self._garantia = ""
        self._espejos_retrovisores = ""

    def get_numero_puertas(self):
        return self._numero_puertas

    def set_numero_puertas(self, numero_puertas):
        self._numero_puertas = numero_puertas

    def get_numero_bolsas_aire(self):
        return self._numero_bolsas_aire

    def set_numero_bolsas_aire(self, numero_bolsas_aire):
        self._numero_bolsas_aire = numero_bolsas_aire

    def get_asistencia_seguro(self):
        return self._asistencia_seguro

    def set_asistencia_seguro(self, asistencia_seguro):
        self._asistencia_seguro = asistencia_seguro

    def get_garantia(self):
        return self._garantia

    def set_garantia(self, garantia):
        self._garantia = garantia

    def get_espejos_retrovisores(self):
        return self._espejos_retrovisores

    def set_espejos_retrovisores(self, espejos):
        self._espejos_retrovisores = espejos



    def mostrar_Informacion_Automovil(self):
        motorizado_info = super().mostrar_Informacion_Motorizado()
        rodaje_info = super().mostrar_Informacion_Rodaje()
        return [
            *motorizado_info,
            *rodaje_info,
            f"Número de puertas: {self._numero_puertas}",
            f"Numero de bolsas aire: {self._numero_bolsas_aire}",
            f"Cuenta con Asistencia seguro: {self._asistencia_seguro}",
            f"Garantia del Vehiculo: {self._garantia}",
            f"Espejos retrovisores: {self._espejos_retrovisores}"
        ]
