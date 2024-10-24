import requests
import tkinter as tk

class GetRecord:
    # URL de MockAPI
    __url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    def get_last_record(self):
        try:
            # Realizar la solicitud GET a la API
            response = requests.get(self.__url)

            print("\n mostrar datos de la consulta original: ",response)

            # Verificar si la solicitud fue exitosa (código 200)
            if response.status_code == 200:

                # Convertir la respuesta a formato JSON (lista de registros)
                data = response.json()

                print("\n la consulta convertida a JSON: ", data)

                # Obtener el último registro
                ultimo_registro = data[-1]
                registro_completo = f"Nombre: {ultimo_registro['nombre']}\n"f"Apellido: {ultimo_registro['apellido']}\n"f"Ciudad: {ultimo_registro['ciudad']}\n"f"Calle: {ultimo_registro['calle']}\n"f"ID: {ultimo_registro['id']}"

                print("\n la consulta formateada: ",registro_completo)

                self.__registro_completo = registro_completo

        finally: print("")

    def view_last_record(self):

        # crear ventana  y mostrar datos
        ventana = tk.Tk()
        ventana.title("Último Registro de API")
        ventana.geometry("400x300")

        # Crear un área de texto para mostrar los datos
        text_area = tk.Text(ventana, height=10, width=50, font=("Helvetica", 20))
        text_area.insert('1.0', self.__registro_completo)
        text_area.pack(pady=20)
        # Ejecutar el bucle principal de Tkinter
        ventana.mainloop()


