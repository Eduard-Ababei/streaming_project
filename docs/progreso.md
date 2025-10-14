# Progreso del Proyecto – Semana 1 (Días 1–8)

Este documento recoge el trabajo realizado durante la primera semana del proyecto **Streaming**, desde la definición inicial hasta la carga de datos en la base de datos en la nube. Cada día se detallan los objetivos, tareas realizadas y resultados obtenidos.

---

##  Día 1 – Definición del proyecto y KPIs

**Objetivo:**  
Definir el alcance general del proyecto, sus objetivos principales y los indicadores clave de rendimiento (KPIs).

**Acciones realizadas:**  
- Planteamiento del problema de negocio: análisis de datos audiovisuales de plataformas de streaming.  
- Diseño de la arquitectura general: ETL con Python → PostgreSQL (Neon) → Vistas SQL → Dashboards BI.  
- Selección de KPIs iniciales, incluyendo:
  - Rating medio por género  
  - Top N películas por plataforma  
  - Porcentaje de estrenos por año  
  - Distribución de títulos por década  
  - Crecimiento del catálogo por plataforma  

**Resultado:**  
El proyecto quedó definido con un objetivo claro, una arquitectura conceptual y una hoja de ruta técnica inicial.

---

##  Día 2 – Selección y evaluación de datasets

**Objetivo:**  
Identificar y preparar las principales fuentes de datos para el proyecto.

**Acciones realizadas:**  
- Selección de datasets relevantes: Netflix (Kaggle), IMDb (BigQuery) y TMDB (API).  
- Evaluación de calidad, volumen, formato y licencias de uso.  
- Organización inicial de los datos en carpetas `/data/raw/`.

**Resultado:**  
Fuentes de datos seleccionadas y documentadas, listas para ser integradas en el pipeline ETL.

---

##  Día 3 – Configuración del entorno y conexión con Neon

**Objetivo:**  
Preparar el entorno de desarrollo y establecer conexión con la base de datos en la nube.

**Acciones realizadas:**  
- Creación y activación de entorno virtual `.venv`.  
- Instalación de dependencias principales (`pandas`, `sqlalchemy`, `psycopg2`, etc.).  
- Configuración del archivo `.env` con la cadena de conexión a Neon.  
- Verificación de conexión mediante script `etl/check_connection_direct.py`.  
- Aplicación del esquema SQL con `etl/apply_schema_direct.py`.  
- Comprobación de tablas creadas con `etl/check_tables_direct.py`.

**Resultado:**  
Entorno de trabajo completamente operativo y conexión establecida con la base de datos en Neon.

---

##  Día 4 – Control de versiones con GitHub

**Objetivo:**  
Iniciar el control de versiones del proyecto y sincronizarlo con un repositorio remoto.

**Acciones realizadas:**  
- Inicialización del repositorio local con `git init`.  
- Creación del repositorio remoto en GitHub.  
- Configuración de `.gitignore` para excluir archivos sensibles y temporales.  
- Primer commit con estructura base del proyecto.  
- Verificación de sincronización local ↔ remoto.

**Resultado:**  
Proyecto versionado y sincronizado correctamente en GitHub, garantizando trazabilidad y colaboración futura.

---

##  Día 5 – Exploración inicial de datos

**Objetivo:**  
Realizar un análisis exploratorio inicial de los datasets seleccionados.

**Acciones realizadas:**  
- Carga de datos con `pandas` y revisión de estructura, columnas y tipos de datos.  
- Detección de valores nulos, duplicados y problemas de calidad.  
- Primer análisis de relaciones entre entidades (películas, géneros, plataformas).

**Resultado:**  
Datos comprendidos a nivel general y plan de limpieza y transformación inicial definido.

---

##  Día 6 – Diseño del modelo entidad-relación (MER)

**Objetivo:**  
Definir el diseño lógico de la base de datos.

**Acciones realizadas:**  
- Creación de un modelo entidad-relación con las tablas principales:  
  - `movies`, `genres`, `platforms`, `ratings`, `movie_genre`, `movie_platform`  
- Definición de claves primarias, relaciones y cardinalidades.  
- Documentación del diagrama MER en `/docs/day6/`.

**Resultado:**  
Modelo de datos estructurado y validado, listo para ser implementado en la base de datos.

---

##  Día 7 – Implementación del esquema SQL

**Objetivo:**  
Implementar físicamente el modelo de datos en la base de datos Neon.

**Acciones realizadas:**  
- Desarrollo del archivo `sql/000_schema.sql` con tablas y constraints.  
- Ejecución del esquema con el script `etl/apply_schema.py`.  
- Validación de estructura mediante consultas y verificación de relaciones.

**Resultado:**  
Base de datos creada en Neon con el esquema completo implementado.

---

##  Día 8 – Carga inicial de datos

**Objetivo:**  
Insertar datos iniciales y validar el correcto funcionamiento del modelo.

**Acciones realizadas:**  
- Carga de datos iniciales en tablas `movies`, `genres`, `platforms`.  
- Establecimiento de relaciones entre películas, géneros y plataformas.  
- Validación de la carga mediante consultas SQL y revisión de integridad.

**Resultado:**  
Base de datos inicial poblada y validada, lista para la siguiente fase del pipeline ETL.

---

**Resumen de la semana:**  
Durante estos ocho primeros días se han definido los objetivos del proyecto, seleccionado y analizado las fuentes de datos, configurado el entorno de trabajo, diseñado e implementado el modelo de base de datos y realizado la carga inicial. El proyecto está ahora preparado para avanzar hacia la automatización del pipeline ETL, análisis avanzado con SQL y visualización en herramientas de BI.
