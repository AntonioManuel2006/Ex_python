from abc import ABC
from datetime import date
from typing import Optional


class Prestable(ABC):

    # Atributo de clase
    dias_maximos_prestamo: int = 31

    def __init__(self, prestado: bool = False, numero_usuario: Optional[int] = None,
                 fecha_prestamo: Optional[date] = None, **kwargs) -> None:

        self._prestado = prestado
        self._numero_usuario = numero_usuario
        self._fecha_prestamo = fecha_prestamo
        super().__init__(**kwargs)

    @property
    def prestado(self) -> bool:
        """Obtiene si está prestado"""
        return self._prestado

    @prestado.setter
    def prestado(self, valor: bool) -> None:
        self._prestado = valor

    @property
    def numero_usuario(self) -> Optional[int]:
        return self._numero_usuario

    @numero_usuario.setter
    def numero_usuario(self, valor: Optional[int]) -> None:
        self._numero_usuario = valor

    @property
    def fecha_prestamo(self) -> Optional[date]:
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, valor: Optional[date]) -> None:
        self._fecha_prestamo = valor

    @property
    def plazo_vencido(self) -> bool:

        if not self._prestado or self._fecha_prestamo is None:
            return False

        hoy = date.today()
        diferencia = abs((hoy - self._fecha_prestamo).days)
        return diferencia > Prestable.dias_maximos_prestamo