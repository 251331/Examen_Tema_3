class Rodaje:
    def __init__(self):
        self._tipo_llantas = ""
        self._tamano_llantas = ""
        self._presion_llantas = 0.0
        self._material_llantas = ""
        self._diferencial = ""
        self._material_rines = ""

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

    def get_material_llantas(self):
        return self._material_llantas

    def set_material_llantas(self, material_llantas):
        self._material_llantas = material_llantas

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
            f"Material rines: {self._material_rines}"
        ]
