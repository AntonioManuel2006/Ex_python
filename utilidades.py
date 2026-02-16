def formatear_linea(texto: str) -> str:

    texto_limpio = texto.strip()
    if texto_limpio:
        return texto_limpio[0].capitalize() + texto_limpio[1:]
    return texto_limpio