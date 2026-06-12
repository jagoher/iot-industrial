# Arquitectura actual y mejoras futuras

## Arquitectura actual

Este proyecto implementa una plataforma Industrial IoT de extremo a extremo basada en una arquitectura orientada a eventos (*Event-Driven Architecture*).

La telemetría generada por un dispositivo ESP32 simulado en Wokwi se publica mediante MQTT y es enviada a Apache Kafka a través de un bridge desarrollado en Python. Kafka actúa como eje central de la plataforma y distribuye los eventos a distintos consumidores.

Actualmente se han implementado dos flujos de procesamiento:

### 1. Ingesta en tiempo real hacia un Data Lake

* Apache Spark Structured Streaming consume los eventos desde Kafka.
* Los datos son almacenados en MinIO, que actúa como Data Lake compatible con Amazon S3.

### 2. Almacenamiento operacional

* Kafka Connect consume los eventos desde Kafka.
* Los datos se almacenan automáticamente en MongoDB para consultas operacionales y aplicaciones de negocio.

La arquitectura implementada sigue los principios de una **Kappa Architecture**, donde Kafka actúa como fuente única de verdad (*Single Source of Truth*) y todos los consumidores leen los mismos eventos.

```text
ESP32 / Wokwi
      ↓
MQTT
      ↓
Mosquitto
      ↓
Bridge MQTT → Kafka
      ↓
Apache Kafka
   ├── Spark Streaming → MinIO
   └── Kafka Connect → MongoDB
```

---

## Formatos de datos utilizados

Actualmente el pipeline utiliza:

* **JSON** para los mensajes MQTT.
* **JSON** para los eventos almacenados en Kafka.
* **BSON** internamente en MongoDB.
* **JSON** para los ficheros almacenados en MinIO.

JSON ha sido seleccionado por su simplicidad, legibilidad y compatibilidad con la mayoría de tecnologías utilizadas en IoT y streaming.

---

## Mejoras futuras

### Apache Parquet

Actualmente los datos almacenados en MinIO se guardan en formato JSON.

Una mejora importante sería utilizar **Apache Parquet** como formato de almacenamiento.

Ventajas:

* Formato columnar.
* Mayor compresión.
* Menor consumo de almacenamiento.
* Mejor rendimiento en consultas analíticas.
* Integración nativa con Spark.

Evolución propuesta:

```text
Kafka
   ↓
Spark
   ↓
Parquet
   ↓
MinIO
```

---

### Delta Lake

Una evolución natural del Data Lake sería incorporar **Delta Lake**.

Ventajas:

* Transacciones ACID.
* Evolución de esquemas.
* Versionado de datos.
* Time Travel.
* Procesamiento incremental más eficiente.

Arquitectura futura:

```text
Spark
   ↓
Delta Lake
   ↓
MinIO
```

---

### Arquitectura Medallion

El Data Lake podría organizarse mediante una arquitectura Medallion:

* **Bronze**: datos crudos procedentes de Kafka.
* **Silver**: datos limpios y validados.
* **Gold**: indicadores y métricas de negocio.

Ejemplo:

```text
Bronze
   ↓
Silver
   ↓
Gold
```

Esta aproximación facilita el gobierno del dato y la construcción de pipelines analíticos escalables.

---

### Apache NiFi

Actualmente el bridge MQTT → Kafka está desarrollado en Python.

Una mejora posible sería sustituirlo por **Apache NiFi**.

Ventajas:

* Diseño visual de flujos.
* Monitorización integrada.
* Gestión de errores.
* Escalabilidad empresarial.
* Menor desarrollo manual.

Arquitectura propuesta:

```text
MQTT
   ↓
NiFi
   ↓
Kafka
```

---

### Bases de datos para grandes volúmenes

MongoDB funciona correctamente para este caso de uso, pero para escenarios industriales de gran escala podrían evaluarse alternativas como:

* Apache HBase
* Apache Cassandra
* InfluxDB
* TimescaleDB

Estas tecnologías están especialmente optimizadas para datos de telemetría y series temporales.

---

### Despliegue Cloud Native

La arquitectura actual se ejecuta localmente mediante Docker Compose.

Una evolución futura podría migrar los componentes a la nube:

| Componente actual | Alternativa Cloud       |
| ----------------- | ----------------------- |
| MinIO             | Amazon S3               |
| Kafka             | Amazon MSK              |
| MongoDB           | MongoDB Atlas           |
| Docker Compose    | Kubernetes              |
| Spark Local       | Databricks / Amazon EMR |

---

### Observabilidad y analítica avanzada

Otras mejoras potenciales:

* Grafana para dashboards en tiempo real.
* OpenSearch / Elasticsearch para búsqueda y observabilidad.
* Prometheus para monitorización.
* Machine Learning para detección de anomalías.
* Modelos de mantenimiento predictivo.

---

## Evolución arquitectónica

Arquitectura actual:

```text
Event-Driven Architecture
+
Kappa Architecture
```

Arquitectura objetivo:

```text
Event-Driven Architecture
+
Kappa Architecture
+
Medallion Architecture
+
Delta Lake
+
Cloud Native Analytics Platform
```

Esta evolución permitiría transformar la solución actual en una plataforma Industrial IoT preparada para entornos productivos, capaz de soportar grandes volúmenes de datos, analítica avanzada y modelos de inteligencia artificial.

