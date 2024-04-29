import dht
import machine
import time
import ssd1306
from umqtt.simple import MQTTClient
import network  


dht_pin = 4 

MQTT_BROKER = "192.168.1.81"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC_TEMP = "utng/ro/temperatura"
MQTT_TOPIC_HUM = "utng/ro/humedad"
MQTT_PORT = 1883

d = dht.DHT11(machine.Pin(dht_pin))

# Configurar la pantalla OLED
i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(16)) 
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def publicar_mensaje(client, topic, msg):
    client.publish(topic, msg)

def conectar_mqtt():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.connect()
    return client

def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('INFINITUMF17B', 'tPZfxHS3g3')
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.3)
    print("WiFi Conectada!")

conectar_wifi()
client = conectar_mqtt()

while True:
    try:
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        
        publicar_mensaje(client, MQTT_TOPIC_TEMP, str(temp))
        publicar_mensaje(client, MQTT_TOPIC_HUM, str(hum))
        
        oled.fill(0)  
        oled.text("Temp: {}C".format(temp), 0, 0)
        oled.text("Humedad: {}%".format(hum), 0, 16)
        oled.show()
        
    except OSError as e:
        print("Error al leer el sensor:", e)
    
    time.sleep(10)
