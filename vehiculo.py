class Vehiculo:
    def __init__(self):
        self._marca = ""
        self._modelo = ""
        self._anio = ""
        self._color = ""
        self._peso = 0
        self._longitud = 0.0
        self._altura = 0
        self._ancho = 0
        self._garantia = ""
        self._asistencia_conductor = ""
        self._tipo_carroceria = ""
        self._material_carroceria = ""
        self._capacidad_carga = 0
        self._capacidad_pasajeros = ""
        self._catidad_llantas = 0



    # Métodos getters y setters
    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_anio(self):
        return self._anio

    def set_anio(self, anio):
        self._anio = anio

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_peso(self):
        return self._peso

    def set_peso(self, peso):
        self._peso = peso

    def get_longitud(self):
        return self._longitud

    def set_longitud(self, longitud):
        self._longitud = longitud

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        self._altura = altura

    def get_ancho(self):
        return self._ancho

    def set_ancho(self, ancho):
        self._ancho = ancho

    def get_garantia(self):
        return self._garantia

    def set_garantia(self, garantia):
        self._garantia = garantia

    def get_asistencia_conductor(self):
        return self._asistencia_conductor

    def set_asistencia_conductor(self, asistencia_conductor):
        self._asistencia_conductor = asistencia_conductor

    def get_tipo_carroceria(self):
        return self._tipo_carroceria

    def set_tipo_carroceria(self, tipo_carroceria):
        self._tipo_carroceria = tipo_carroceria

    def get_material_carroceria(self):
        return self._material_carroceria

    def set_material_carroceria(self, material_carroceria):
        self._material_carroceria = material_carroceria

    def get_capacidad_pasajeros(self):
        return self._capacidad_pasajeros

    def set_capacidad_pasajeros(self, capacidad_pasajeros):
        self._capacidad_pasajeros = capacidad_pasajeros

    def get_capacidad_carga(self):
        return self._capacidad_carga

    def set_capacidad_carga(self, capacidad_carga):
        self._capacidad_carga = capacidad_carga

    def get_catidad_llantas(self):
        return self._catidad_llantas

    def set_catidad_llantas(self, catidad_llantas):
        self._catidad_llantas = catidad_llantas


    def mostrar_Informacion_Vehiculo(self):
        return [
            f"Marca del Vehiculo: {self._marca}",
            f"Modelo del Vehiculo: {self._modelo}",
            f"Año de Fabriacion: {self._anio}",
            f"Color del Vehiculo: {self._color}",
            f"Peso del Vehiculo en Kg: {self._peso}",
            f"Longitud del Vehiculo metros: {self._longitud}",
            f"Altura del Vehiculo en metros: {self._altura}",
            f"Ancho del Vehiculo metros: {self._ancho}",
            f"Garantia del Vehiculo: {self._garantia}",
            f"Tipo Carroceria: {self._tipo_carroceria}",
            f"Material Carroceria: {self._material_carroceria}",
            f"Capacidad Pasajeros: {self._capacidad_pasajeros}",
            f"Capacidad Carga en Kg: {self._capacidad_carga}",
            f"Catidad Llantas: {self._catidad_llantas}"
        ]