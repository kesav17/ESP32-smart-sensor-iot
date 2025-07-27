import network
import urequests
import time
import dht
from machine import Pin
import json

# Wi-Fi credentials
ssid = 'replace your wifi name'
password = 'replace your wifi password'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)
print("Connected to Wi-Fi:", wlan.ifconfig())

# Setup DHT22 sensor (on GPIO 14)
sensor = dht.DHT22(Pin(14))

# API server endpoint (replace with your PC IP address)
url = 'http://xxx.xxx.xxx.xxx:5000/data' # ← Replace this

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        print("Sending -> Temp: {:.1f}°C, Hum: {:.1f}%".format(temp, hum))

        payload = {
            "temperature": temp,
            "humidity": hum
        }

        # Send data to Flask server
        headers = {"Content-Type": "application/json"}
        response = urequests.post(url, data=json.dumps(payload), headers=headers)
        print("Server response:", response.text)
        response.close()

    except Exception as e:
        print("Error:", e)

    time.sleep(10)  # Send every 10 seconds
