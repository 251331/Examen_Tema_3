# Clase hija de Motorizado, para Barcos
from motorizado import Motorizado
class Barco(Motorizado):
    def __init__(self):
        super().__init__()
        self._tipo_barco = ""
        self._cabinas = 0
        self._tipo_uso = ""
        self._equipo_salvavidas = False
        self._proa = ""
        self._popa = ""
        self._sistema_navegacion = ""
        self._tipo_poniente = ""
        self._sistema_desagote = False
        self._sistema_vapor = False

    def get_tipo_barco(self):
        return self._tipo_barco

    def set_tipo_barco(self, tipo_barco):
        self._tipo_barco = tipo_barco

    def get_cabinas(self):
        return self._cabinas

    def set_cabinas(self, cabinas):
        self._cabinas = cabinas

    def get_tipo_uso(self):
        return self._tipo_uso

    def set_tipo_uso(self, tipo_uso):
        self._tipo_uso = tipo_uso

    def get_equipo_salvavidas(self):
        return self._equipo_salvavidas

    def set_equipo_salvavidas(self, equipo_salvavidas):
        self._equipo_salvavidas = equipo_salvavidas

    def get_proa(self):
        return self._proa

    def set_proa(self, proa):
        self._proa = proa
        return self

    def get_popa(self):
        return self._popa

    def set_popa(self, popa):
        self._popa = popa
        return self

    def get_sistema_navegacion(self):
        return self._sistema_navegacion

    def set_sistema_navegacion(self, sistema_navegacion):
        self._sistema_navegacion = sistema_navegacion
        return self

    def get_tipo_poniente(self):
        return self._tipo_poniente

    def set_tipo_poniente(self, tipo_poniente):
        self._tipo_poniente = tipo_poniente
        return self

    def get_sistema_desagote(self):
        return self._sistema_desagote

    def set_sistema_desagote(self, sistema_desagote):
        self._sistema_desagote = sistema_desagote
        return self

    def get_sistema_vapor(self):
        return self._sistema_vapor

    def set_sistema_vapor(self, sistema_vapor):
        self._sistema_vapor = sistema_vapor
        return self

    def mostrar_Informacion_Barco(self):
        motorizado_info = super().mostrar_Informacion_Motorizado()
        return [
            *motorizado_info,
            f"Tipo de barco: {self._tipo_barco}",
            f"Total de Cabinas: {self._cabinas}",
            f"Tipo uso: {self._tipo_uso}",
            f"Cuenta con Equipo salvavidas: {self._equipo_salvavidas}",
            f"Proa: {self._proa}",
            f"Popa: {self._popa}",
            f"Sistema navegacion: {self._sistema_navegacion}",
            f"Tipo de poniente: {self._tipo_poniente}",
            f"Sistema de dasagote: {self._sistema_desagote}",
            f"Sistema de vapor: {self._sistema_vapor}",
        ]