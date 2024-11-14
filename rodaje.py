class Rodaje:
    def __init__(self):
        self._tipo_llantas = ""
        self._tamano_llantas = ""
        self._presion_llantas = 0.0
        self._material_llantas = ""
        self._diferencial = ""
        self._velocidad_maxima_llantas = 0.0
        self._durabilidad_llantas = 0.0
        self._alineacion = True
        self._rueda_reserva = False
        self._material_rines = ""
        self._peso_llanta = 0.0

    def get_tipo_llantas(self):
        return self._tipo_llantas

    def set_tipo_llantas(self, tipo_llantas):
        self._tipo_llantas = tipo_llantas

    def get_tamano_llantas(self):
        return self._tamano_llantas

    def set_tamano_llantas(self, tamano_llantas):
        self._tamano_llantas = tamano_llantas

    def get_presion_llantas(self):
        return self._presion_llantas

    def set_presion_llantas(self, presion_llantas):
        self._presion_llantas = presion_llantas

    def get_diferencial_llantas(self):
        return self._diferencial

    def set_diferencial_llantas(self, diferencial_llantas):
        self._diferencial = diferencial_llantas

    def get_velocidad_maxima_llantas(self):
        return self._velocidad_maxima_llantas

    def set_velocidad_maxima_llantas(self, diferencial_llantas):
        self._velocidad_maxima_llantas = diferencial_llantas

    def get_durabilidad_llantas(self):
        return self._durabilidad_llantas

    def set_durabilidad_llantas(self, durabilidad_llantas):
        self._durabilidad_llantas = durabilidad_llantas

    def get_alineacion(self):
        return self._alineacion

    def set_alineacion(self, alineacion):
        self._alineacion = alineacion

    def get_rueda_reserva(self):
        return self._rueda_reserva

    def set_rueda_reserva(self, rueda_reserva):
        self._rueda_reserva = rueda_reserva

    def get_material_llantas(self):
        return self._material_llantas

    def set_material_llantas(self, material_llantas):
        self._material_llantas = material_llantas

    def get_peso_llanta(self):
        return self._peso_llanta

    def set_peso_llanta(self, peso_llanta):
        self._peso_llanta = peso_llanta

    def get_material_rines(self):
        return self._material_rines

    def set_material_rines(self, material_rines):
        self._material_rines = material_rines

    def mostrar_Informacion_Rodaje(self):
        return [
            f"Tipo de llantas: {self._tipo_llantas}",
            f"Tamaño de llantas: {self._tamano_llantas}",
            f"Presion llantas: {self._presion_llantas}",
            f"Material llantas: {self._material_llantas}",
            f"Diferencial llantas: {self._diferencial}",
            f"Velocidad maxima: {self._velocidad_maxima_llantas}",
            f"Durabilidad llantas en Klm: {self._durabilidad_llantas}",
            f"Alineacion de las llantas en mm: {self._alineacion}",
            f"Equipa Rueda reserva: {self._rueda_reserva}",
            f"Material rines: {self._material_rines}",
            f"Peso llantas en Kg: {self._peso_llanta}",
        ]
