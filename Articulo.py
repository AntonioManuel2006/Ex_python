
from abc import ABC, abstractmethod
from datetime import date
from Utilidades.utilidades import formatear_linea


class Articulo(ABC):


    def __init__(self, titulo: str, anio: int, fecha_adquisicion: date, **kwargs) -> None:

        self._titulo = formatear_linea(titulo)
        self._anio = self._validar_anio(anio)
        self._fecha_adquisicion = fecha_adquisicion
        super().__init__(**kwargs)

    def _validar_anio(self, anio: int) -> int:

        anio_actual = date.today().year
        if 1500 <= anio <= anio_actual:
            return anio
        raise ValueError(f"El año debe estar entre 1500 y {anio_actual}")

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:

        self._titulo = formatear_linea(valor)

    @property
    def anio(self) -> int:
        return self._anio

    @anio.setter
    def anio(self, valor: int) -> None:
        self._anio = self._validar_anio(valor)

    @property
    def fecha_adquisicion(self) -> date:
        return self._fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, valor: date) -> None:
        self._fecha_adquisicion = valor

