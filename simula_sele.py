from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import re

# Ruta al WebDriver de Chrome
chromedriver_path = "C:/Users/HP/Documents/simulacion_bot/chromedriver.exe"
service = Service(chromedriver_path)
print("Se encontro chromedriver")

# Inicializar el navegador de Chrome
driver = webdriver.Chrome(service=service)
print("Se inicio correctamente chromedriver")

# Abre WhatsApp Web
driver.get("https://web.whatsapp.com")
time.sleep(25)

# Esperar a que el usuario escanee el código QR
input("Escanea el código QR y presiona Enter para continuar...")

# Número de WhatsApp del usuario al que se le enviarán los mensajes (debe estar registrado)
numero_telefono = '+524497274470'

# Crear el enlace de WhatsApp para enviar mensaje a un número no registrado
whatsapp_link = f"https://wa.me/{numero_telefono}"

# Abre la conversación con el número no registrado
driver.get(whatsapp_link)

try:
    driver.get(whatsapp_link)
    print("Se abrió el nuevo link correctamente")
except Exception as e:
    print(f"Ocurrió un error al abrir el link: {str(e)}")

print(f"Enlace generado es: {whatsapp_link}")
time.sleep(10)

try:
    # Buscar el botón utilizando el texto "Ir al chat" o la clase del botón
    ir_al_chat_button = driver.find_element(By.XPATH, '//a[@class="_9vcv _advm _9scb"]')
    ir_al_chat_button.click()
    print("Hicimos clic en el botón 'Ir al chat'")
    time.sleep(8)  # Espera para que WhatsApp Web cargue
except Exception as e:
    print(f"Ocurrió un error al hacer clic en 'Ir al chat': {str(e)}")
    
# Hacer clic en el botón "usar WhatsApp Web"
try:
    usar_whatsapp_web_button = driver.find_element(By.XPATH, '//span[text()="usar WhatsApp Web"]')
    usar_whatsapp_web_button.click()
    print("Hicimos clic en el botón 'usar WhatsApp Web'")
    time.sleep(20)  # Espera para que cargue WhatsApp Web
except Exception as e:
    print(f"Ocurrió un error al hacer clic en 'usar WhatsApp Web': {str(e)}")    


#Buscar el campo de búsqueda de contactos en WhatsApp Web
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
time.sleep(15)
print("Se esta buscando el campo de busqueda")

# Ingresar el número de teléfono del contacto y presionar Enter
search_box.send_keys(numero_telefono)
search_box.send_keys(Keys.ENTER)
time.sleep(15)
print("Se ingresan los datos")

# Opciones del chatbot
def enviar_opciones():
    # Enviar mensaje de bienvenida y opciones
    chat_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    chat_box.send_keys("¡Hola! Bienvenido a ChaCha express. Por favor, selecciona una opción:\n1. Soy empleado\n2. Cotizar servicios\n3. Quiero solicitar empleo")
    chat_box.send_keys(Keys.ENTER)
    time.sleep(10)  # Dar tiempo para que el mensaje se envíe y el usuario responda
print("Se enviaron las opciones")

# Responder según la opción seleccionada
def enviar_respuesta(opcion):
    chat_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
    time.sleep(15)
    if opcion == "1":
        chat_box.send_keys("Redacte el asunto a tratar.")
        chat_box.send_keys(Keys.ENTER)
        time.sleep(15)
    elif opcion == "2":
        chat_box.send_keys("Gracias por tu interes en nuestro servicios, selecciona una de las modalidades")
        chat_box.send_keys(Keys.ENTER)
        time.sleep(15)
    elif opcion == "3":
        chat_box.send_keys("Por favor deje su CV, nos pondremos en contacto lo antes posible.")
        chat_box.send_keys(Keys.ENTER)
        time.sleep(15)
    else:
        chat_box.send_keys("Por favor, selecciona una opción válida: 1, 2 o 3.")
        chat_box.send_keys(Keys.ENTER)

# Simular el flujo del chatbot
enviar_opciones()

def obtener_opcion(texto):
    match = re.search(r'\b[1-3]\b', texto)
    return match.group(0) if match else None


# Aquí simulamos que el gerente responde con una opción
while True:
    # Leer la respuesta del usuario
    mensajes = driver.find_elements(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/div[3]/div[20]/div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span')
    if mensajes:
        ultima_respuesta = mensajes[-1].text.strip()  # Capturar el último mensaje y eliminar espacios en blanco
        print(f"Respuesta del usuario capturada: '{ultima_respuesta}'")

        
          
       # Filtrar la opción numérica
        opcion = obtener_opcion(ultima_respuesta)
        enviar_respuesta(opcion)
        
        time.sleep(15)  # Espera antes de verificar el siguiente mensaje
        break  # Rompe el ciclo después de procesar una opción

