import network
import urequests
from machine import ADC
import time

# Configuracion Wi-Fi
ssid = "ROSCAPUMPA"
password = "tommy2209"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

print("Conexión exitosa. IP: " + wifi.ifconfig()[0])

potentiometer_pin = ADC(34)

thingspeak_url = "https://api.thingspeak.com/update?api_key=D22T9B5Q3OCKO9HL&field1="

while True:

    potentiometer_value = potentiometer_pin.read()

    print("Valor del potenciómetro:", potentiometer_value)

    url = thingspeak_url + str(potentiometer_value)
    response = urequests.get(url)
    print("Respuesta de ThingSpeak:", response.text)
    response.close()
    time.sleep(15)
