import os
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
    "¿Cuál es el mejor lugar para visitar en Europa?",
    "¿Qué es la teoría de la relatividad de Einstein?",
    "¿Cómo puedo aprender a tocar la guitarra?",
    "¿Cuál es el mejor libro de ciencia ficción de todos los tiempos?",
    "¿Qué es el efecto invernadero y cómo afecta el medio ambiente?",
    "¿Cómo puedo mejorar mi memoria?",
    "¿Cuál es el mejor método para aprender un nuevo idioma?",
    "¿Qué es la inteligencia emocional y cómo puedo desarrollarla?",
    "¿Cómo puedo crear un presupuesto personal efectivo?",
    "¿Cuál es el mejor lugar para visitar en América del Sur?",
    "¿Qué es la teoría del caos y cómo se aplica en la vida real?",
    "¿Cómo puedo aprender a programar en Python?",
    "¿Cuál es el mejor libro de historia de todos los tiempos?",
    "¿Qué es el marketing digital y cómo puedo aplicarlo en mi negocio?",
    "¿Cómo puedo mejorar mi salud mental?",
    "¿Cuál es el mejor método para aprender a jugar ajedrez?",
    "¿Qué es la física cuántica y cómo funciona?",
    "¿Cómo puedo crear un plan de estudios efectivo?",
    "¿Cuál es el mejor lugar para visitar en Asia?",
    "¿Qué es la teoría de la evolución de Darwin y cómo se aplica en la vida real?",
    "¿Cómo puedo aprender a tocar el piano?",
    "¿Cuál es el mejor libro de filosofía de todos los tiempos?",
    "¿Qué es la ética y cómo se aplica en la vida real?",
    "¿Cómo puedo mejorar mi productividad en el trabajo?",
    "¿Cuál es el mejor método para aprender a nadar?",
    "¿Qué es la química y cómo funciona?",
    "¿Cómo puedo crear un presupuesto para un proyecto?",
    "¿Cuál es el mejor lugar para visitar en África?",
    "¿Qué es la teoría de la gravedad de Newton y cómo se aplica en la vida real?",
    "¿Cómo puedo aprender a hablar en público?",
    "¿Cuál es el mejor libro de psicología de todos los tiempos?",
    "¿Qué es la sociología y cómo se aplica en la vida real?",
    "¿Cuál es el mejor método para aprender a jugar tenis?",
    "¿Qué es la teoría de la relatividad general de Einstein?",
    "¿Cómo puedo mejorar mi habilidad para tomar decisiones?",
    "¿Cuál es el mejor libro de economía de todos los tiempos?",
    "¿Qué es la teoría de la evolución molecular?",
    "¿Cómo puedo aprender a programar en Java?",
    "¿Cuál es el mejor lugar para visitar en Oceanía?",
    "¿Qué es la teoría de la complejidad?",
    "¿Cómo puedo mejorar mi habilidad para trabajar en equipo?",
    "¿Cuál es el mejor libro de filosofía política de todos los tiempos?",
    "¿Qué es la teoría de la justicia?",
    "¿Cómo puedo aprender a tocar el violín?",
    "¿Cuál es el mejor lugar para visitar en el Medio Oriente?",
    "¿Qué es la teoría de la guerra?",
    "¿Cómo puedo mejorar mi habilidad para negociar?",
    "¿Cuál es el mejor libro de historia militar de todos los tiempos?",
    "¿Qué es la teoría de la estrategia?",
    "¿Cómo puedo aprender a programar en C++?",
    "¿Cuál es el mejor lugar para visitar en el Caribe?",
    "¿Quién es el personaje principal de la saga original de Star Wars?",
    "¿Cuál es el nombre del planeta natal de Luke Skywalker?",
    "¿Qué es el poder de la Fuerza en el universo de Star Wars?",
    "¿Quién es el villano principal de la saga original de Star Wars?",
    "¿Cuál es el nombre de la nave espacial de Han Solo?",
    "¿Qué es el Consejo Jedi y cuál es su propósito?",
    "¿Quién es el personaje principal de la trilogía prequel de Star Wars?",
    "¿Cuál es el nombre del planeta donde se encuentra la ciudad de Coruscant?",
    "¿Qué es el lado oscuro de la Fuerza y cómo se relaciona con los Sith?",
    "¿Quién es el personaje principal de la trilogía secuela de Star Wars?",
    "¿Cuál es el nombre de la organización rebelde que lucha contra el Imperio Galáctico?",
    "¿Qué es el holocron y cuál es su importancia en el universo de Star Wars?",
    "¿Quién es el personaje principal de la serie de televisión The Mandalorian?",
    "¿Cuál es el nombre del planeta donde se encuentra la ciudad de Mandalore?",
    "¿Qué es el Día de la Independencia Galáctica y cuál es su importancia en el universo de Star Wars?",
    "¿Quién es el personaje principal de la serie de televisión Obi-Wan Kenobi?",
    "¿Cuál es el nombre del planeta donde se encuentra el Templo Jedi?",
    "¿Qué es el Código Jedi y cuál es su importancia en el universo de Star Wars?"

]

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
        time.sleep(7)

except Exception as e:
    print(f"Ha ocurrido un error: {e}")
finally:
    # Cerrar el navegador
    driver.quit()

os.system("pause")