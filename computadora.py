import time
import random
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Ruta al driver de Microsoft Edge
EDGE_DRIVER_PATH = "msedgedriver.exe"  # Cambia esto por la ruta donde tengas el WebDriver

# Lista de palabras o frases para realizar búsquedas aleatorias
search_terms = [
    "¿Cuál es el mejor alimento para gatos?",
    "¿Qué novedades hay en el mundo de la tecnología?",
    "¿Cómo funciona la inteligencia artificial en la vida cotidiana?",
    "¿Puedes recomendarme recetas de cocina vegetariana?",
    "¿Cuál es el equipo de fútbol más popular de Argentina?",
    "¿Qué noticias recientes hay sobre el cambio climático?",
    "¿Dónde puedo aprender programación en Python para principiantes?",
    "¿Cuál es la teoría más aceptada sobre el origen del universo?",
    "¿Quién es el compositor de música clásica más influyente de todos los tiempos?",
    "¿Puedes proporcionarme una receta para hacer pizza en casa?",
    "¿Cuáles son los mejores juegos online para jugar con amigos?",
    "¿Quién es el artista más importante del Renacimiento?",
    "¿Cuál es la mejor película de ciencia ficción de todos los tiempos?",
    "¿Dónde puedo encontrar ofertas para viajes baratos a Europa?",
    "¿Quién es el autor de ciencia ficción más leído en Argentina?",
    "¿Puedes recomendarme libros de historia para leer este verano?",
    "¿Cuál es el mejor lugar para visitar en Argentina para disfrutar de la naturaleza?",
    "¿Qué es el turismo sostenible y cómo puedo practicarlo?",
    "¿Cuál es la mejor aplicación para aprender idiomas en línea?",
    "¿Puedes proporcionarme consejos para mejorar mi productividad en el trabajo?",
    
]

# Configurar el navegador Edge
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")  # Abrir el navegador maximizado

# Inicializar el servicio del navegador
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service, options=options)

try:
    # Abrir el navegador en la página de inicio
    driver.get("https://www.bing.com")  # Bing es el buscador predeterminado de Edge

    while True:
        # Elegir un término de búsqueda aleatorio
        search_query = random.choice(search_terms)
        print(f"Buscando: {search_query}")

        # Encontrar la barra de búsqueda y realizar la búsqueda
        search_box = driver.find_element(By.NAME, "q")  # El campo de búsqueda en Bing tiene el atributo "name=q"
        search_box.clear()  # Limpiar la barra de búsqueda
        search_box.send_keys(search_query)  # Escribir el término de búsqueda
        search_box.send_keys(Keys.RETURN)  # Presionar "Enter"

        # Esperar 3 segundos antes de realizar la siguiente búsqueda
        time.sleep(9)

except Exception as e:
    print(f"Ha ocurrido un error: {e}")
finally:
    # Cerrar el navegador
    driver.quit()