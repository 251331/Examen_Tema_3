from vehiculo import Vehiculo

class Motorizado(Vehiculo):
    def __init__(self):
        super().__init__()
        self._numero_cilindros = 0
        self._potencia_motor = 0  # En HP o kW
        self._torque = 0  # En Nm o lb-ft
        self._aceleracion_0_100 = 0  # En segundos
        self._tipo_combustible = ""
        self._numero_marchas = 0
        self._consumo_combustible_motor = 0.0  # En L/100 km
        self._tipo_transmision_motor = ""
        self._grado_anticongelante = 0.0
        self._numero_serie_motor = ""
        self._tipo_direccion = ""
        self._sistema_suspension = ""
        self._frecuencia_aceite = 0

    # Métodos getters y setters para cada atributo

    def get_numero_cilindros(self):
        return self._numero_cilindros

    def set_numero_cilindros(self, numero_cilindros):
        self._numero_cilindros = numero_cilindros

    def get_potencia_motor(self):
        return self._potencia_motor

    def set_potencia_motor(self, potencia_motor):
        self._potencia_motor = potencia_motor

    def get_torque(self):
        return self._torque

    def set_torque(self, torque):
        self._torque = torque

    def get_aceleracion_0_100(self):
        return self._aceleracion_0_100

    def set_aceleracion_0_100(self, aceleracion_0_100):
        self._aceleracion_0_100 = aceleracion_0_100

    def get_tipo_combustible(self):
        return self._tipo_combustible

    def set_tipo_combustible(self, tipo_combustible):
        self._tipo_combustible = tipo_combustible

    def get_numero_marchas(self):
        return self._numero_marchas

    def set_numero_marchas(self, numero_marchas):
        self._numero_marchas = numero_marchas

    def get_consumo_combustible_motor(self):
        return self._consumo_combustible_motor

    def set_consumo_combustible_motor(self, consumo_combustible_motor):
        self._consumo_combustible_motor = consumo_combustible_motor

    def get_tipo_transmision_motor(self):
        return self._tipo_transmision_motor

    def set_tipo_transmision_motor(self, tipo_transmision_motor):
        self._tipo_transmision_motor = tipo_transmision_motor

    def get_grado_anticongelante(self):
        return self._grado_anticongelante

    def set_grado_anticongelante(self, grado_anticongelante):
        self._grado_anticongelante = grado_anticongelante

    def get_numero_serie_motor(self):
        return self._numero_serie_motor

    def set_numero_serie_motor(self, numero_serie_motor):
        self._numero_serie_motor = numero_serie_motor

    def get_tipo_direccion(self):
        return self._tipo_direccion

    def set_tipo_direccion(self, tipo_direccion):
        self._tipo_direccion = tipo_direccion

    def get_sistema_suspension(self):
        return self._sistema_suspension

    def set_sistema_suspension(self, sistema_suspension):
        self._sistema_suspension = sistema_suspension

    def get_frecuencia_aceite(self):
        return self._frecuencia_aceite

    def set_frecuencia_aceite(self, frecuencia_aceite):
        self._frecuencia_aceite = frecuencia_aceite


    def mostrar_Informacion_Motorizado(self):
        parent_info = super().mostrar_Informacion_Vehiculo()
        return [
            *parent_info,
            f"Numero de cilindros: {self._numero_cilindros}",
            f"Potencia motor: {self._potencia_motor}",
            f"Torque: {self._torque}",
            f"Aceleracia motor: {self._aceleracion_0_100}",
            f"Tipo de combustible que maneja: {self._tipo_combustible}",
            f"Numero marchas: {self._numero_marchas}",
            f"Consumo combustible em litros: {self._consumo_combustible_motor}",
            f"Tipo de transmision: {self._tipo_transmision_motor}",
            f"Grado del anticongelante que utiliza: {self._grado_anticongelante}",
            f"Numero de serie: {self._numero_serie_motor}",
            f"Tipo de direccion: {self._tipo_direccion}",
            f"Sistema de Suspencion: {self._sistema_suspension}",
            f"Frecuencia del tipo de Aceite: {self._frecuencia_aceite}"
        ]