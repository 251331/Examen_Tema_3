from vehiculo import Vehiculo

class Motorizado(Vehiculo):
    def __init__(self):
        super().__init__()
        self._numero_cilindros = 0
        self._potencia_motor = 0  # En HP o kW
        self._aceleracion_0_100 = 0  # En segundos
        self._tipo_combustible = ""
        self._consumo_combustible_motor = 0.0  # En L/100 km
        self._grado_anticongelante = 0.0
        self._numero_serie_motor = ""
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

    def get_aceleracion_0_100(self):
        return self._aceleracion_0_100

    def set_aceleracion_0_100(self, aceleracion_0_100):
        self._aceleracion_0_100 = aceleracion_0_100

    def get_tipo_combustible(self):
        return self._tipo_combustible

    def set_tipo_combustible(self, tipo_combustible):
        self._tipo_combustible = tipo_combustible

    def get_consumo_combustible_motor(self):
        return self._consumo_combustible_motor

    def set_consumo_combustible_motor(self, consumo_combustible_motor):
        self._consumo_combustible_motor = consumo_combustible_motor

    def get_grado_anticongelante(self):
        return self._grado_anticongelante

    def set_grado_anticongelante(self, grado_anticongelante):
        self._grado_anticongelante = grado_anticongelante

    def get_numero_serie_motor(self):
        return self._numero_serie_motor

    def set_numero_serie_motor(self, numero_serie_motor):
        self._numero_serie_motor = numero_serie_motor


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
            f"Aceleracia motor: {self._aceleracion_0_100}",
            f"Tipo de combustible que maneja: {self._tipo_combustible}",
            f"Consumo combustible em litros: {self._consumo_combustible_motor}",
            f"Grado del anticongelante que utiliza: {self._grado_anticongelante}",
            f"Numero de serie: {self._numero_serie_motor}",
            f"Frecuencia del tipo de Aceite: {self._frecuencia_aceite}"
        ]