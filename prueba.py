import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Ruta al driver de Microsoft Edge (Asegúrate de descargar y configurar el Edge WebDriver)
EDGE_DRIVER_PATH = "msedgedriver.exe"  # Cambia esto por la ruta de tu Edge WebDriver

# Configurar el navegador Edge
options = webdriver.EdgeOptions()
options.add_experimental_option("mobileEmulation", {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, como Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
})

# Inicializar el servicio del navegador
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service, options=options)

try:
    # Abrir el navegador en la página de inicio
    driver.get("https://www.bing.com")  # Bing es el buscador predeterminado de Edge

    # URL de la API de Wikipedia
    url = "https://en.wikipedia.org/w/api.php"

    # Parámetros de la llamada a la API
    params = {
        "action": "query",
        "list": "mostviewed",
        "format": "json",
        "mvprop": "title|views",
        "mvlimit": "20"
    }

    # Realizar la llamada a la API
    response = requests.get(url, params=params)

    # Obtener los datos de la respuesta
    data = json.loads(response.text)

    # Realizar búsquedas con las páginas más visitadas
    for page in data["query"]["mostviewed"]:
        print(f"Buscando: {page['title']}")

        # Encontrar la barra de búsqueda y realizar la búsqueda
        search_box = driver.find_element(By.NAME, "q")  # El campo de búsqueda en Bing tiene el atributo "name=q"
        search_box.clear()  # Limpiar la barra de búsqueda
        search_box.send_keys(page["title"])  # Escribir el término de búsqueda
        search_box.send_keys(Keys.RETURN)  # Presionar "Enter"

        # Esperar 5 segundos antes de realizar la siguiente búsqueda
        time.sleep(5)

except Exception as e:
    print(f"Ha ocurrido un error: {e}")
finally:
    # Cerrar el navegador
    driver.quit()