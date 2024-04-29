from machine import Pin
from time import sleep
import network
from umqtt.simple import MQTTClient


pin_sensor = Pin(5, Pin.IN)  
pin_led = Pin(2, Pin.OUT)  

MQTT_BROKER = "192.168.0.9"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/ro/ky004"
MQTT_PORT = 1883

def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('ElGerasxd', 'xdpapi23')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi Conectada!")

def publicar_mensaje(msg):
    client.publish(MQTT_TOPIC, msg)
def verificar_sensor():
    while True:
        estado_actual = pin_sensor.value()  
        print("Estado del botón:", estado_actual) 
        if estado_actual == 0:
            publicar_mensaje(b'true')
            pin_led.on()  
            sleep(10)  
            
            while pin_sensor.value() == 0:
                sleep(2)
            
            pin_led.off()  
        
        else:
            pin_led.off()
        
        sleep(0.1)  
conectar_wifi()
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
client.connect()

verificar_sensor()
