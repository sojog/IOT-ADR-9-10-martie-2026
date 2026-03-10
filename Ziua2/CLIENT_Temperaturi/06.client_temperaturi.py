## ACEASTA BUCATA DE COD serveste ca SENZOR
import random
import time
import paho.mqtt.client as mqtt
import json

MQTT_BROKER    = "broker.hivemq.com"
MQTT_TOPIC     = "python_vreme_senzor"


MQTT_CLIENT_ID = "cititor_de_la_senzor_iot"


MIN_TEMP = -20
MAX_TEMP = 45

def function_that_executes_on_connect(client, userdata, connect_flags, reason_code): #, properties):
    if reason_code == 0:
        print("Dispozitivul s-a conectat cu succes")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Conexiunea a esuat {reason_code}")

client = mqtt.Client(client_id=MQTT_CLIENT_ID)
client.on_connect = function_that_executes_on_connect


def function_that_executes_on_message(client, userdata, message):
    print("Aceasta functie se apeleaza de fiecare data cand se primeste un mesaj")
    print(f"Topicul mesajului:, {message.topic}")
    mesajul_transmis = message.payload.decode()
    print(f"Mesajul transmis:, {mesajul_transmis}")


client.on_message = function_that_executes_on_message

try:
    client.connect(host=MQTT_BROKER, port=1883, keepalive=60)
    client.loop_forever()
except Exception as e:
    print(f"A aparut o eroare {e}")
