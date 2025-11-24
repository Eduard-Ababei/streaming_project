# Streaming – ETL y Análisis de Datos en la Nube

**Streaming** es un proyecto profesional centrado en la analítica de datos del sector audiovisual.  
El objetivo de este proyecto es construir un pipeline **ETL completo y funcional** utilizando un **dataset local**, replicando un flujo real de trabajo en ingeniería de datos sin depender de APIs externas.

Este proyecto queda **completamente finalizado en el Día 10**, con un ETL 100% operativo:  
limpieza del dataset, creación del esquema SQL y carga final en PostgreSQL (Neon).

---

## 1. Descripción general

El proyecto implementa un flujo ETL profesional formado por:

- Lectura del dataset original (Netflix demo)  
- Limpieza y normalización con Pandas  
- Creación del modelo relacional y el esquema SQL  
- Carga final en Neon mediante SQLAlchemy  
- Verificación completa del pipeline

Todo el proceso es reproducible desde cero.

---

## 2. Objetivos

- Procesar y limpiar un dataset local.  
- Definir un esquema SQL coherente para la tabla `movies`.  
- Cargar los datos limpios en Neon PostgreSQL.  
- Construir un pipeline ETL estructurado y modular.  
- Documentar la arquitectura y la ejecución del proyecto.

---

## 3. Tecnologías principales

| Etapa | Tecnologías |
|-------|--------------|
| Extracción | CSV local |
| Transformación | Python, Pandas |
| Carga | SQLAlchemy, PostgreSQL (Neon Cloud) |
| Validación | SQL, Python |
| Control de versiones | Git, GitHub |

---

## 4. Arquitectura de carpetas

streaming/
├─ etl/ # Scripts ETL
│ ├─ clean_local_netflix_csv.py
│ ├─ apply_schema.py
│ ├─ reset_schema.py
│ ├─ etl_load_movies.py
│ └─ check_connection_direct.py
│
├─ data/ # Datasets
│ ├─ raw/
│ ├─ clean/
│ └─ processed/
│
├─ sql/ # Esquema SQL
│ └─ 000_schema.sql
│
├─ dashboards/ # (Preparado para visualización)
├─ infra/ # (Estructura de CI/CD)
└─ docs/ # Documentación y diagramas


---

## 5. Estado del desarrollo (Proyecto cerrado en Día 10)

| Día | Fase | Estado | Descripción |
|-----|------|---------|-------------|
| 1 | Presentación | Completado | Definición del alcance y arquitectura general. |
| 2 | Dataset | Completado | Importación y organización del dataset local. |
| 3 | Entorno | Completado | Creación del entorno virtual y conexión Neon. |
| 4 | Repositorio | Completado | Estructura inicial y control de versiones. |
| 5 | Exploración | Completado | Análisis preliminar del dataset. |
| 6 | Modelo de datos | Completado | Diseño del MER y estructura de la tabla `movies`. |
| 7 | Esquema SQL | Completado | Implementación del DDL en PostgreSQL. |
| 8 | Limpieza | Completado | Limpieza y normalización (`movies_clean.csv`). |
| 9 | Carga | Completado | Carga final en Neon mediante SQLAlchemy. |
| 10 | ETL completo | Completado | Pipeline funcional y validado end-to-end. |

Este proyecto finaliza oficialmente en el Día 10.

---

## 6. Pipeline ETL

| Etapa | Descripción | Resultado |
|--------|--------------|-----------|
| Extract | Lectura del dataset local (`movies_raw.csv`). | Datos crudos en `data/raw/`. |
| Transform | Limpieza, selección de columnas y normalización. | `movies_clean.csv` en `data/clean/`. |
| Load | Ejecución del esquema SQL y carga en Neon. | Tabla `movies` con 7.973 filas. |
| Validate | Consultas de prueba y verificación. | Proceso ETL validado de inicio a fin. |

---

## 7. Ejecución del proyecto

1. **Activar entorno e instalar dependencias**

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt


2. **Limpiar el dataset local**

python etl/clean_local_netflix_csv.py


3. **Reiniciar el esquema en Neon**

python etl/reset_schema.py


4. **Aplicar el esquema SQL**

python etl/apply_schema.py


5. **Cargar los datos limpios**

python etl/etl_load_movies.py


---

## 8. Resultados finales

- Dataset limpio y normalizado (`movies_clean.csv`).  
- Esquema SQL aplicado en Neon.  
- Tabla `movies` creada y poblada correctamente.  
- Pipeline ETL **completo, modular y reproducible**.  
- Proyecto **cerrado y finalizado** en el Día 10.

---

## 9. Autoría

Proyecto desarrollado por  
**Stefan Eduard Ababei Jorascu**  
Repositorio GitHub: https://github.com/Eduard-Ababei/streaming_project
