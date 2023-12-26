import requests


def obtener_tiempo_respuesta(url):
    try:
        respuesta = requests.get(url)
        tiempo_respuesta = respuesta.elapsed.total_seconds() * 1000  # Tiempo en milisegundos
        return tiempo_respuesta
    except requests.RequestException as e:
        print(f"No se pudo obtener el tiempo de respuesta de la URL {url}: {e}")
        return None


urls = ['https://ssl1.cabal.coop/', 'https://ssl2.cabal.coop/', 'https://ssl3.cabal.coop/']


mejor_tiempo = float('inf')
mejor_url = None

for url in urls:
    tiempo = obtener_tiempo_respuesta(url)
    print(url, tiempo)
    if tiempo is not None and tiempo < mejor_tiempo:
        mejor_tiempo = tiempo
        mejor_url = url

if mejor_url:
    print(f"La mejor opcion es {mejor_url} con un tiempo de respuesta de aproximadamente {mejor_tiempo} milisegundos.")
else:
    print("No se pudo determinar la URL más rápida.")
