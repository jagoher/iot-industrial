\# Industrial IoT Streaming Pipeline



Proyecto de arquitectura IoT industrial con ingesta MQTT, procesamiento en Kafka/Spark y almacenamiento en MinIO y MongoDB.



\## Arquitectura



```text

ESP32 / Wokwi

&#x20;     ↓

MQTT Broker

&#x20;     ↓

Python MQTT → Kafka Bridge

&#x20;     ↓

Apache Kafka

&#x20;  ├── Spark Structured Streaming → MinIO Data Lake

&#x20;  └── Kafka Connect → MongoDB

