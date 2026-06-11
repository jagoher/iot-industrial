# Industrial IoT Streaming Pipeline

Proyecto de arquitectura IoT industrial con ingesta MQTT, procesamiento en Kafka/Spark y almacenamiento en MinIO y MongoDB.

## Architecture

```text
┌─────────────────┐
│ ESP32 / Wokwi   │
└────────┬────────┘
         │ MQTT
         ▼
┌─────────────────┐
│ MQTT Broker     │
│ Mosquitto       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ MQTT → Kafka    │
│ Python Bridge   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Apache Kafka    │
└──────┬─────┬────┘
       │     │
       │     │
       ▼     ▼
┌──────────┐ ┌──────────────────┐
│ Spark    │ │ Kafka Connect    │
│ Streaming│ │ MongoDB Sink     │
└────┬─────┘ └────────┬─────────┘
     │                │
     ▼                ▼
┌──────────┐    ┌──────────┐
│ MinIO    │    │ MongoDB  │
│ DataLake │    │          │
└──────────┘    └──────────┘
```

## Components

* ESP32 / Wokwi simulator generates telemetry.
* Mosquitto receives MQTT messages.
* Python bridge forwards MQTT events to Kafka.
* Apache Kafka acts as the event backbone.
* Spark Structured Streaming stores raw events in MinIO.
* Kafka Connect persists events into MongoDB.
* MongoDB Compass provides data exploration.
* Kafka UI provides topic monitoring.

