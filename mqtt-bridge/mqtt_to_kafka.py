import json
import paho.mqtt.client as mqtt
from kafka import KafkaProducer

# MQTT (Wokwi publicará aquí)
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "gorritxo/industrial/machines/test99"

# Kafka local Docker
KAFKA_BOOTSTRAP = "localhost:9092"
KAFKA_TOPIC = "industrial.machines.raw"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def on_connect(client, userdata, flags, rc):
    print("MQTT conectado. Código:", rc)
    client.subscribe(MQTT_TOPIC)
    print("Suscrito a:", MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")

    print("\nMQTT recibido:")
    print(payload)

    try:
        data = json.loads(payload)

        producer.send(KAFKA_TOPIC, data)
        producer.flush()

        print("Enviado a Kafka")
    except Exception as e:
        print("Error:", e)

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

print("Conectando a MQTT...")
client.connect(MQTT_BROKER, MQTT_PORT, 60)

client.loop_forever()