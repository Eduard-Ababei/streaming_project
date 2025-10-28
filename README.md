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

3. Configurar variables de entorno:
cp .env.example .env
Editar DATABASE_URL con la cadena de conexión de Neon

4. Ejecutar el pipeline:
Primera ejecución del proyecto (desde cero)

Si nunca has corrido el proyecto o acabas de crear una base de datos vacía en Neon, este es el orden:

check_connection_direct.py
→ Verifica que Python se conecta correctamente a Neon.
(Comprobación previa obligatoria)

clean_csv.py
→ Limpia el dataset crudo (CSV) y genera uno limpio (movies_clean.csv).
(Necesario antes de cargar datos)

apply_schema.py
→ Crea las tablas base en la base de datos (movies, genres, ratings, etc.).
(Primero se crean las tablas vacías)

etl_load_movies.py
→ Carga los datos limpios desde el CSV en la tabla movies.
(Aquí es cuando realmente se insertan datos)

check_tables.py
→ Muestra las tablas y un preview de los datos para confirmar que todo salió bien.



Resultados esperados

Base de datos limpia y normalizada con información de películas, géneros, plataformas y ratings.

Vistas SQL listas para análisis exploratorio.

Dashboards con KPIs como rating medio, estrenos por año, crecimiento del catálogo o top películas por plataforma.















