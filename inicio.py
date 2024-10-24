import requests
import tkinter as tk
from tkinter import messagebox
# URL de MockAPI
url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

# Realizar la solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Convertir la respuesta a formato JSON (lista de registros)
    data = response.json()

    # Comprobar si la lista tiene elementos
    if data:
        # Obtener el último registro
        ultimo_registro = data[-1]
        registro_completo = f"Nombre: {ultimo_registro['nombre']}\n"f"Apellido: {ultimo_registro['apellido']}\n"f"Ciudad: {ultimo_registro['ciudad']}\n"f"Calle: {ultimo_registro['calle']}\n"f"ID: {ultimo_registro['id']}"
        # Mostrar el último registro
        print("Último registro:", ultimo_registro)
        # crear ventana  y mostrar datos
        # Crear la ventana principal de Tkinter
        ventana = tk.Tk()
        ventana.title("Último Registro de API")
        ventana.geometry("400x300")

        # Crear un área de texto para mostrar los datos
        text_area = tk.Text(ventana, height=10, width=50,font=("Helvetica", 20))

        text_area.insert('1.0', registro_completo)
        text_area.pack(pady=20)


        # Ejecutar el bucle principal de Tkinter
        ventana.mainloop()
    else:
        print("No hay registros disponibles.")
else:
    print(f"Error en la solicitud: {response.status_code}")

