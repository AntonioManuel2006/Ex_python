import sqlite3

conexion = sqlite3.connect("Libros.db")

cursor = conexion.cursor()


cursor.execute("""
            -- Crear la tabla libros
CREATE TABLE IF NOT EXISTS libros (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn              TEXT    NOT NULL UNIQUE CHECK(length(isbn) = 10),
    titulo            TEXT    NOT NULL,
    anio              INTEGER NOT NULL CHECK(anio BETWEEN 1500 AND 2026),
    fecha_adquisicion DATE    NOT NULL,
    prestado          INTEGER NOT NULL DEFAULT 0 CHECK(prestado IN (0, 1)),
    numero_usuario    INTEGER,
    fecha_prestamo    DATE
)
""")

cursor.execute("""
-- 1. El Quijote (disponible)
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('8433503400', 'El Quijote De La Mancha', 1605, '2023-03-15', 0, NULL, NULL);
""")


cursor.execute("""
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0140157451', 'Cien Años De Soledad', 1967, '2023-05-20', 1, 1001, '2026-02-10');

""")

cursor.execute("""
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0143034490', 'La Sombra Del Viento', 2001, '2023-07-10', 0, NULL, NULL);""")

cursor.execute("""
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0451524493', '1984', 1949, '2022-11-01', 1, 1002, '2025-12-01');
""")

cursor.execute("""INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0156014297', 'El Principito', 1943, '2024-01-20', 0, NULL, NULL);""")

cursor.execute("""
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0394752488', 'Rayuela', 1963, '2023-09-05', 1, 1003, '2025-11-15');
""")


cursor.execute("""
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0552739414', 'La Casa De Los Espiritus', 1982, '2024-06-12', 0, NULL, NULL);

""")

cursor.execute("""
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0802410305', 'Ficciones', 1944, '2024-03-28', 1, 1004, '2026-02-05');
""")

conexion.commit()

conexion.execute("select * from libros")

resultados = cursor.fetchall()

for libros in resultados:
    print(libros)









