# Streaming – ETL y Análisis de Datos en la Nube

**Streaming** es un proyecto profesional de análisis de datos enfocado en la industria audiovisual. Su objetivo es construir un **pipeline completo de datos** para extraer, transformar y cargar información sobre películas y plataformas de streaming (Netflix, TMDB, IMDb) en una base de datos en la nube, habilitando análisis en herramientas de **Business Intelligence** y preparando el terreno para futuros modelos de predicción.

---

## Objetivo del proyecto

El proyecto desarrolla un flujo **ETL (Extract – Transform – Load)** moderno y reproducible que permite:

- Integrar datos de distintas fuentes públicas relacionadas con películas y plataformas.
- Limpiar, transformar y almacenar la información en una base de datos SQL en la nube.
- Exponer vistas optimizadas para análisis y dashboards en herramientas BI.
- Preparar la arquitectura para procesos de machine learning y despliegue automatizado.

---

## Tecnologías utilizadas

| Capa | Tecnologías principales |
|------|---------------------------|
| Extracción y transformación | Python, Pandas, SQLAlchemy |
| Almacenamiento | PostgreSQL (Neon Cloud) |
| Infraestructura y despliegue | GitHub, Docker, Jenkins |
| Business Intelligence | Tableau, Power BI |
| Cloud & Big Data | Google BigQuery, GCS |

---

## ⚙️ Arquitectura del proyecto

streaming/
├─ etl/ # Scripts de extracción, limpieza y carga (clean_csv, reset_schema, apply_schema, etc.)
├─ sql/ # Definición de esquemas, consultas y vistas
├─ data/ # Datos brutos, limpios y procesados
│ ├─ raw/
│ ├─ clean/
│ └─ processed/
├─ dashboards/ # Dashboards de Tableau y Power BI
├─ infra/ # CI/CD, Dockerfile, Jenkinsfile, Ansible
└─ docs/ # Documentación técnica, diagramas, evidencias


---

## Pipeline ETL

1. **Extract:** descarga de datasets (Netflix, TMDB, IMDb) y carga en formato CSV o JSON.  
2. **Transform:** limpieza, normalización, creación de columnas derivadas y validación de datos.  
3. **Load:** almacenamiento en PostgreSQL (Neon) mediante scripts Python (`apply_schema.py`, `reset_schema.py`, etc.).  
4. **Query:** creación de vistas y consultas SQL optimizadas para análisis.  
5. **Visualize:** conexión de Power BI y Tableau a las vistas para generar dashboards dinámicos.

---

## Estructura de carpetas

| Carpeta | Contenido principal |
|--------|-----------------------|
| `etl/` | Scripts Python para extracción, limpieza, transformación y carga |
| `sql/` | Archivos `.sql` con el esquema y las consultas |
| `data/` | Archivos CSV/JSON en diferentes etapas del pipeline |
| `dashboards/` | Dashboards desarrollados en Tableau y Power BI |
| `infra/` | Configuración de CI/CD, Dockerfile, Jenkinsfile |
| `docs/` | Diagramas, capturas y documentación de cada fase |

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
git clone https://github.com/tuusuario/streaming.git
cd streaming

2. Crear entorno virtual e instalar dependencias:
python -m venv .venv
.venv\Scripts\activate   # (Windows)
pip install -r requirements.txt

3. Configurar variables de entorno:
cp .env.example .env
Editar DATABASE_URL con la cadena de conexión de Neon

4. Ejecutar el pipeline:
python etl/clean_csv.py
python etl/apply_schema.py
python etl/reset_schema.py


Resultados esperados

Base de datos limpia y normalizada con información de películas, géneros, plataformas y ratings.

Vistas SQL listas para análisis exploratorio.

Dashboards con KPIs como rating medio, estrenos por año, crecimiento del catálogo o top películas por plataforma.















