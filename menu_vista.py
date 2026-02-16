import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import date, datetime
from typing import Optional


class PantallaPrincipal:

    def __init__(self) -> None:

        # Crear ventana principal
        self.libros = None
        self.ventana = tk.CTk()
        self.ventana.title("Sistema de Gestión de Biblioteca")
        self.ventana.geometry("1200x700")

        self._crear_interfaz()
        self._cargar_datos()

    def _crear_interfaz(self) -> None:

        # Frame central con TreeView
        frame_treeview = tk.Frame(self.ventana)
        frame_treeview.pack(fill="both", expand=True, padx=10, pady=10)

        # Crear Treeview
        columnas = ("ID", "isbn", "titulo", "anio", "fecha_adquisicon", "prestado", "numero_usuario", "fecha_prestamo")
        self.tree = ttk.Treeview(frame_treeview, columns=columnas, show="tree headings", height=15)

        # Configurar columnas
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("isbn", width=250)
        self.tree.column("tituto", width=70, anchor="center")
        self.tree.column("anio", width=100, anchor="center")
        self.tree.column("fecha_adquisicion", width=100, anchor="center")
        self.tree.column("numero_usuario", width=80, anchor="center")
        self.tree.column("fecha_préstamo", width=120, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_treeview, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Frame de botones
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(fill="x", padx=10, pady=10)

        # Botones de operaciones
        tk.TkButton(
            frame_botones,
            text="Crear Libro",
            command=self._crear_libro,
        ).pack(side="left", padx=5)

        tk.TkButton(
            frame_botones,
            text="Editar Libro",
            command=self._editar_libro,
        ).pack(side="left", padx=5)

        tk.TkButton(
            frame_botones,
            text="Eliminar Libro",
            command=self._eliminar_libro,
        ).pack(side="left", padx=5)

        tk.TkButton(
            frame_botones,
            text="Prestar Libro",
            command=self._prestar_libro,
        ).pack(side="left", padx=5)

        tk.TkButton(
            frame_botones,
            text="Exportar Vencidos CSV",
            command=lambda: self.exportar_csv,
        ).pack(side="left", padx=5)

        tk.TkButton(
            frame_botones,
            text="Actualizar",
            command=self._cargar_datos
        ).pack(side="right", padx=5)

    def _cargar_datos(self, libros=None) -> None:

        # Limpiar árbol
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obtener libros
        if libros is None:
            libros = self.controlador.obtener_todos_libros()

        # Insertar libros
        for libro in libros:
            estado = "Prestado" if libro.prestado else "Disponible"
            usuario = libro.numero_usuario if libro.numero_usuario else "-"
            fecha_prestamo = libro.fecha_prestamo.strftime("%Y-%m-%d") if libro.fecha_prestamo else "-"
            vencido = "SÍ" if libro.plazo_vencido else "NO"

            valores = (
                libro.id,libro.isbn,libro.titulo,libro.anio,
                libro.fecha_adquisicion.strftime("%Y-%m-%d"),
                libro.prestado,
                libro.numero_usuario,
                fecha_prestamo,
            )

            # Colorear filas de libros vencidos
            if libro.plazo_vencido:
                self.tree.insert("", "end", values=valores, tags=("vencido",))
            else:
                self.tree.insert("", "end", values=valores)

        # Configurar colores
        self.tree.tag_configure("vencido", background="#ffcccc")

    def _crear_libro(self) -> None:
        """Abre ventana para crear un nuevo libro"""
        ventana_crear = tk.Toplevel(self.ventana)
        ventana_crear.title("Crear Nuevo Libro")
        ventana_crear.geometry("500x400")
        ventana_crear.grab_set()

        # Título
        tk.Label(ventana_crear, text="Título:").pack(pady=(20, 5))
        entrada_titulo = tk.Entry(ventana_crear, width=400)
        entrada_titulo.pack(pady=5)

        # Año
        tk.Label(ventana_crear, text="Año:").pack(pady=5)
        entrada_anio = tk.Entry(ventana_crear, width=400)
        entrada_anio.pack(pady=5)

        # Fecha de adquisición
        tk.Label(ventana_crear, text="Fecha de Adquisición (YYYY-MM-DD):").pack(pady=5)
        entrada_fecha = tk.Entry(ventana_crear, width=400)
        entrada_fecha.insert(0, date.today().strftime("%Y-%m-%d"))
        entrada_fecha.pack(pady=5)

        tk.Label(ventana_crear, text="ISBN:").pack(pady=5)
        entrada_isbn = tk.Entry(ventana_crear, width=400)
        entrada_isbn.pack(pady=5)

    def _eliminar_libro(self) -> None:
        """Elimina el libro seleccionado"""
        datos = self._obtener_libro_seleccionado()
        if not datos:
            return

        id_libro = datos[0]
        titulo = datos[1]

        respuesta = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Está seguro de eliminar el libro '{titulo}'?"
        )

        if respuesta:
            exito, mensaje = self.controlador.eliminar_libro(id_libro)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self._cargar_datos()
            else:
                messagebox.showerror("Error", mensaje)

    def exportar_csv(self):
        try:
            if not self.libros:
                messagebox.showwarning("Sin datos", "No hay libros para exportar")
                return

            # Abrir diálogo para guardar archivo
            archivo = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Guardar archivo CSV",
                initialfile="libros.csv"
            )

            if not archivo:  # Usuario canceló
                return

            # Escribir CSV
            with open(archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)

                # Encabezados
                writer.writerow(['id','isbn','titulo','anio','fecha_adquisicion','prestado','numero_usuario','fecha_prestamo'])
        except ValueError:
            print('No se exporto a CSV')

    def ejecutar(self) -> None:
        """Ejecuta la aplicación"""
        self.ventana.mainloop()