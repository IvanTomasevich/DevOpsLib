import tkinter as tk
import requests


def obtener_tiempo_respuesta(url):
    try:
        respuesta = requests.get(url)
        tiempo_respuesta = respuesta.elapsed.total_seconds() * 1000  # Tiempo en milisegundos
        return tiempo_respuesta
    except requests.RequestException as e:
        return None


def verificar_tiempo():
    mejor_tiempo = float('inf')
    mejor_url = None

    for url in urls:
        tiempo = obtener_tiempo_respuesta(url)
        if tiempo is not None and tiempo < mejor_tiempo:
            mejor_tiempo = tiempo
            mejor_url = url

    if mejor_url:
        resultado.config(text=f"La mejor opción es: \n"
                              f"{mejor_url} \n Tiempo de respuesta de aprox. \n"
                              f"{mejor_tiempo} milisegundos.")
    else:
        resultado.config(text="No se pudo determinar la URL más rápida.")


# URLs de ejemplo
urls = ['https://ssl1.cabal.coop/', 'https://ssl2.cabal.coop/', 'https://ssl3.cabal.coop/']

# Crear la ventana
root = tk.Tk()
root.title("Verificar Tiempo de Respuesta SSL Cabal Coop")
# Establecer el tamaño de la ventana
root.geometry("600x600")

# Botón para verificar el tiempo de respuesta
verificar_button = tk.Button(root, text="Verificar", command=verificar_tiempo)
verificar_button.pack(pady=10)

# Etiqueta para mostrar el resultado
resultado = tk.Label(root, text="", font=("Arial", 12))
resultado.pack(pady=20)

root.mainloop()
