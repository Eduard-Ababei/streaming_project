# Streaming – ETL y Análisis de Datos en la Nube

**Streaming** es un proyecto profesional en curso centrado en la analítica de datos del sector audiovisual.  
El objetivo es construir un pipeline completo que integre información de plataformas como Netflix, TMDB e IMDb, permitiendo análisis avanzados, visualizaciones interactivas y futura integración con modelos predictivos.

---

## 1. Descripción general

El proyecto replica la estructura de un entorno profesional de datos mediante un flujo ETL (Extract – Transform – Load) totalmente documentado y reproducible.  
El trabajo se desarrolla en 50 días organizados por fases: desde la ingesta inicial hasta la automatización y la presentación en herramientas BI.  

Actualmente, el desarrollo se encuentra en la Fase 2 (Limpieza y Transformación de datos, Día 10 de 50).

---

## 2. Objetivos

- Integrar fuentes públicas heterogéneas (APIs y datasets CSV).  
- Procesar, limpiar y normalizar la información.  
- Cargar los datos en una base de datos PostgreSQL en la nube (Neon).  
- Crear consultas SQL y vistas para BI.  
- Conectar Power BI y Tableau para dashboards ejecutivos.  
- Automatizar el flujo con Docker, Jenkins y Ansible.  

---

## 3. Tecnologías principales

| Etapa | Tecnologías |
|-------|--------------|
| Extracción | Python, Requests, Pandas |
| Transformación | Pandas, NumPy |
| Carga | SQLAlchemy, PostgreSQL (Neon Cloud) |
| Visualización | Tableau, Power BI |
| Cloud & Big Data | Google BigQuery, GCS |
| Automatización | Docker, Jenkins, Ansible |
| Control de versiones | Git, GitHub |

---

## 4. Arquitectura de carpetas

streaming/
├─ etl/                    # Scripts ETL: extracción, limpieza, transformación y carga
│  ├─ extract_tmdb.py
│  ├─ extract_tmdb_demo.py
│  ├─ clean_tmdb.py
│  ├─ clean_local_netflix_csv.py
│  ├─ apply_schema.py
│  ├─ reset_schema.py
│  ├─ etl_load_movies.py
│  └─ check_connection_direct.py
│
├─ data/                   # Datasets por etapa del pipeline
│  ├─ raw/
│  ├─ processed/
│  └─ clean/
│
├─ sql/                    # Esquemas y consultas SQL
│  └─ 000_schema.sql
│
├─ dashboards/             # Visualizaciones BI (Tableau / Power BI)
├─ infra/                  # CI/CD · Dockerfile · Jenkinsfile · Ansible
└─ docs/                   # Documentación técnica, diagramas y evidencias

---

## 5. Estado del desarrollo

| Día | Fase | Estado | Descripción |
|-----|------|---------|-------------|
| 1 | Presentación | Completado | Definición del alcance, KPIs y arquitectura general. |
| 2 | Dataset | Completado | Selección de fuentes (Netflix, TMDB, IMDb) y organización inicial. |
| 3 | Entorno | Completado | Creación del entorno virtual y configuración de Neon (PostgreSQL). |
| 4 | Repositorio | Completado | Configuración de GitHub y primer commit del proyecto. |
| 5 | Exploración | Completado | Análisis exploratorio de columnas, nulos y duplicados. |
| 6 | Modelo de datos | Completado | Diseño del modelo entidad–relación (MER). |
| 7 | Esquema SQL | Completado | Implementación de tablas y relaciones en PostgreSQL. |
| 8 | Carga inicial | Completado | Inserción y verificación de datos base. |
| 9 | Extracción (TMDb API) | Completado | Desarrollo de extract_tmdb.py y extract_tmdb_demo.py; obtención de datos reales y demo. |
| 10 | Limpieza de datos | Completado | Creación de clean_tmdb.py y clean_local_netflix_csv.py; depuración de datasets. |
| 11–20 | Transformación | En desarrollo | Unificación de datasets y generación de tablas auxiliares. |
| 21–28 | Visualización | Pendiente | Creación de dashboards Power BI y Tableau. |
| 29–36 | Cloud y BigQuery | Pendiente | Integración con GCP y BigQuery. |
| 37–50 | DevOps y Cierre | Pendiente | Automatización, documentación final y presentación. |

---

## 6. Pipeline ETL

| Etapa | Descripción | Resultado |
|--------|--------------|-----------|
| Extract | Descarga de datasets públicos y consulta de la API de TMDB. | Archivos CSV/JSON en data/processed/. |
| Transform | Limpieza, normalización y creación de columnas derivadas. | Archivos limpios en data/clean/. |
| Load | Inserción en PostgreSQL (Neon) con SQLAlchemy. | Tablas estructuradas y relacionadas. |
| Query | Creación de vistas SQL para BI y KPIs. | Vistas optimizadas para Power BI/Tableau. |
| Visualize | Dashboards interactivos y reportes comparativos. | Indicadores clave (KPIs). |

---

## 7. Ejecución del proyecto

1. **Clonar el repositorio**
   
git clone https://github.com/tuusuario/streaming.git
cd streaming

2. **Configurar entorno virtual e instalar dependencias**

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt


3. **Configurar variables de entorno**

DATABASE_URL=postgresql+psycopg2://user:password@host/dbname?sslmode=require
TMDB_API_KEY=tu_api_key_aqui


4. **Verificar conexión a Neon**

python etl\check_connection_direct.py


5. **Extraer datos desde TMDB**

python etl\extract_tmdb.py


(Si no tienes API key activa, usa la demo)

python etl\extract_tmdb_demo.py


6. **Limpiar datos extraídos**
   
python etl\clean_tmdb.py


7. **(Opcional) Limpieza del dataset demo**
   
python etl\clean_local_netflix_csv.py


---

## 8. Resultados actuales

- Dataset limpio y normalizado (`data/clean/movies_clean.csv`).  
- Conexión establecida entre Python y Neon PostgreSQL.  
- Pipeline funcional de extracción y limpieza totalmente reproducible.  
- Preparación finalizada para iniciar la transformación y carga en base de datos.

---

## 9. Próximos pasos

- Fase 3: Transformación de datos y creación de tablas auxiliares.  
- Fase 4: Dashboards y KPIs en Tableau y Power BI.  
- Fase 5: Integración Cloud (BigQuery y GCS).  
- Fase 6: CI/CD con Docker y Jenkins.  
- Fase 7: Documentación final y entrega.

---

## 10. Autoría
Stefan Eduard Ababei Jorascu
Proyecto en desarrollo como forma de adquirir experiencia para los puestos de trabajo.

Autor: **Stefan Eduard Ababei Jorascu**  
Repositorio: [GitHub](https://github.com/tuusuario/streaming)
