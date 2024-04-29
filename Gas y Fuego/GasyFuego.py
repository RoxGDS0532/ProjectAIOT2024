import network
import urequests as requests
import time
from machine import ADC, Pin, PWM
from umqtt.simple import MQTTClient

firePin = ADC(35)  # KY-026 Fuego
gasPin = ADC(34)   # MQ-02 Gas
firePin.atten(ADC.ATTN_11DB)
gasPin.atten(ADC.ATTN_11DB)

buzzer_pin = 23  # Buzzer
buzzer_pwm = PWM(Pin(buzzer_pin))
buzzer_pwm.duty(0)

# Configuración MQTT
MQTT_BROKER = "192.168.0.21"
MQTT_TOPIC_FIRE = "utng/ro/ky026"  
MQTT_TOPIC_GAS = "utng/ro/mq02"    
MQTT_TOPIC_BUZZER = "utng/ro/buzzer"  
MQTT_CLIENT_ID = ""


token = "EAALUvwZBaZAbYBOyx7lGdy6mMFuVIotzUMCIvbMvKHaTXJTZCIl2JDRvF4fz2Bg28q9JMILJeCJcdC5vm9j0v5EJbL1CeVW7jB2SL1cX5h4tz5MFSRzcuuvA5C4VaV8o1XNUg15CBPw2p9gmcTOTtZCN9MuPehRE7l0xAZCZAtuJyIy1QVyncvyJlZBEpoEyZApzLPM40qcbToHFMvjZBJmMZD"
server_url = "https://graph.facebook.com/v19.0/269598009578222/messages"
phone_number = "524181529071"


buzzer_status = "deactivate"

def conectar_wifi():
    print("Conectando a la red WiFi...", end="")
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectando...", end="")
        sta_if.active(True)
        sta_if.connect('ElGerasxd', 'xdpapi23')
        while not sta_if.isconnected():
            time.sleep(1)
    print("Conexión WiFi establecida:", sta_if.ifconfig())

def publicar_mensaje(topic, msg):
    client.publish(topic, str(msg))  


def callback_buzzer(topic, msg):
    global buzzer_status
    print("Mensaje recibido:", msg.decode())  
    if msg == b'deactivate':
        buzzer_status = "deactivate"
        buzzer_pwm.duty(0)
    elif msg == b'activate':
        buzzer_status = "activate"
        buzzer_pwm.freq(200)  
        buzzer_pwm.duty(512)  


# Función para enviar mensajes de WhatsApp
def send_whatsapp_message(message):
    payload = {"messaging_product": "whatsapp", "to": phone_number, "type": "text", "text": {"body": message}}
    try:
        response = requests.post(server_url, json=payload, headers={"Authorization": "Bearer " + token})
        print("HTTP Response code:", response.status_code)
        print("Response:", response.text)
    except Exception as e:
        print("Error:", e)

conectar_wifi()
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
client.set_callback(callback_buzzer)
client.connect()
client.subscribe(MQTT_TOPIC_BUZZER)

while True:
    client.check_msg()  
    time.sleep(0.5)
    
    fireValor = firePin.read()
    gasValor = gasPin.read()
    print("Sensor fuego:", fireValor)
    print("Sensor gas:", gasValor)

    publicar_mensaje(MQTT_TOPIC_FIRE, fireValor)
    publicar_mensaje(MQTT_TOPIC_GAS, gasValor)

    if fireValor <= 1000 and buzzer_status == "activate":
        buzzer_pwm.freq(200)  
        buzzer_pwm.duty(512)  
        send_whatsapp_message("Fuego detectado")
    elif gasValor >= 1000 and buzzer_status == "activate":
        buzzer_pwm.freq(200)  
        buzzer_pwm.duty(512)  
        send_whatsapp_message("Fuga de gas detectada")
    else:
        buzzer_pwm.duty(0)
