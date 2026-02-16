

from datetime import date
from typing import Optional
from Modelo.Articulo import Articulo
from Modelo.Prestable import Prestable


class Libro(Articulo, Prestable):


    def __init__(self, titulo: str, anio: int, fecha_adquisicion: date, isbn_10: str,
                 prestado: bool = False, numero_usuario: Optional[int] = None,
                 fecha_prestamo: Optional[date] = None, id_libro: Optional[int] = None) -> None:

        # Constructor cooperativo - llama a los padres
        super().__init__(
            titulo=titulo,
            anio=anio,
            fecha_adquisicion=fecha_adquisicion,
            prestado=prestado,
            numero_usuario=numero_usuario,
            fecha_prestamo=fecha_prestamo
        )
        self._isbn_10 = self._validar_isbn_10(isbn_10)
        self._id_libro = id_libro

    def _validar_isbn(self, isbn: str) -> str:

        # Limpiar el ISBN (eliminar guiones y espacios)
        isbn_limpio = isbn.replace("-", "").replace(" ", "")

        # Verificar que tenga exactamente 10 caracteres
        if len(isbn_limpio) != 10:
            raise ValueError("El ISBN-10 debe tener exactamente 10 dígitos")

        # Verificar que todos sean dígitos (excepto el último que puede ser X)
        if not isbn_limpio[:-1].isdigit():
            raise ValueError("El ISBN-10 debe contener solo dígitos")

        # El último carácter puede ser X (representa 10)
        if not (isbn_limpio[-1].isdigit() or isbn_limpio[-1].upper() == 'X'):
            raise ValueError("El último carácter del ISBN-10 debe ser un dígito o X")

        # Calcular la suma de validación
        suma = 0
        multiplicadores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        for i, digito in enumerate(isbn_limpio):
            if digito.upper() == 'X':
                valor = 10
            else:
                valor = int(digito)
            suma += valor * multiplicadores[i]

        # Verificar que la suma sea múltiplo de 11
        if suma % 11 != 0:
            raise ValueError("El ISBN no es válido (la suma no es múltiplo de 11)")

        return isbn_limpio

    @property
    def isbn(self) -> str:
        return self._isbn_10

    @isbn.setter
    def isbn(self, valor: str) -> None:
        self._isbn_10 = self._validar_isbn_10(valor)

    @property
    def id_libro(self) -> Optional[int]:
        return self._id_libro

    @id_libro.setter
    def id_libro(self, valor: Optional[int]) -> None:
        self._id_libro = valor

    def __str__(self) -> str:
        return f"Libro: {self.titulo} ({self.anio}) - ISBN: {self.isbn_10}"

    def __repr__(self) -> str:
        return f"Libro(titulo='{self.titulo}', anio={self.anio}, isbn_10='{self.isbn_10}')"