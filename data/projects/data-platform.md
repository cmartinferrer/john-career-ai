
# Data Processing Platform

## Contexto del proyecto

Proyecto desarrollado en Northstar Digital Solutions
para una empresa ficticia del sector logístico.

La compañía necesitaba consolidar información
procedente de diferentes sistemas de pedidos,
almacenes y transporte.

El procesamiento anterior dependía de tareas
batch y generaba retrasos en la actualización
de la información.

## Objetivos

- Procesar eventos de pedidos casi en tiempo real.
- Integrar información de diferentes sistemas.
- Mejorar la trazabilidad de las operaciones.
- Reducir el acoplamiento entre aplicaciones.
- Facilitar el escalado de los componentes.

## Rol y responsabilidades

John Doe participó como Senior Backend Engineer.

Sus principales responsabilidades fueron:

- Diseñar e implementar servicios backend con Python.
- Desarrollar APIs REST utilizando FastAPI.
- Implementar consumidores y productores de Kafka.
- Definir mecanismos de validación de eventos.
- Desarrollar pruebas unitarias y de integración.
- Investigar problemas de rendimiento.
- Participar en revisiones de arquitectura.
- Colaborar en el despliegue sobre Kubernetes.

## Arquitectura

La plataforma utilizaba una arquitectura
orientada a eventos.

Los sistemas de origen publicaban eventos
en diferentes topics de Apache Kafka.

Los servicios consumidores procesaban
los mensajes, validaban su contenido
y almacenaban la información consolidada
en PostgreSQL.

Redis se utilizaba como caché para
determinadas consultas frecuentes.

Las APIs REST permitían consultar el estado
de las operaciones procesadas.

## Tecnologías utilizadas

- Python
- FastAPI
- Apache Kafka
- PostgreSQL
- Redis
- Docker
- Kubernetes
- AWS
- pytest

## Retos técnicos

### Procesamiento de eventos duplicados

Algunos eventos podían recibirse más de una vez.

Se implementaron mecanismos de idempotencia
para evitar que una misma operación generase
actualizaciones duplicadas.

### Gestión de errores

Se diferenciaron los errores recuperables
de los errores de validación.

Los errores transitorios podían procesarse
mediante reintentos controlados.

Los eventos que no podían procesarse
se enviaban a un flujo de revisión.

### Escalabilidad

Se realizaron pruebas de carga para analizar
el comportamiento de los consumidores.

Se ajustaron parámetros de concurrencia
y recursos de los contenedores para
mejorar la capacidad de procesamiento.

## Resultados

El equipo consiguió reducir la latencia
de actualización de información de varios
minutos a menos de 30 segundos en los
escenarios medidos durante las pruebas.

También mejoró la trazabilidad de los eventos
y la capacidad de recuperación ante errores.

Estos resultados corresponden a un caso
completamente ficticio creado para este tutorial.

## Aprendizajes

El proyecto permitió profundizar en:

- Arquitecturas orientadas a eventos.
- Diseño de consumidores idempotentes.
- Procesamiento distribuido.
- Observabilidad y diagnóstico.
- Pruebas de carga.
- Escalado de microservicios.
