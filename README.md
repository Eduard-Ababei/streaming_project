# streaming_project

Analítica de streaming (películas, ratings, plataformas) con pipeline ETL → PostgreSQL (Neon) → BI (Tableau/Power BI) y CI/CD (Jenkins/Docker).

## Día 1 – Presentación y alcance

**Objetivo:** dejar preparado el entorno de trabajo para iniciar el proyecto de datos.

### Alcance
- **Problema:** integrar y analizar datos de películas (TMDB/IMDb/Netflix) para calcular KPIs y hacer predicción ligera.  
- **Arquitectura:** ETL (Python/SQLAlchemy) → Neon (PostgreSQL) → Vistas SQL para BI → Dashboards (Tableau/Power BI).  
- **CI/CD:** Jenkins + Docker.  

### KPIs iniciales
1. Rating medio por género  
2. Top N películas por plataforma  
3. % de estrenos por año  
4. Distribución de títulos por década  
5. Crecimiento del catálogo por plataforma  

**Evidencias:**  
`docs/day1/architecture.png`, `docs/day1/kpis.md`, `docs/day1/scope.md`

---

## Estructura del proyecto

### plaintext 
```
etl/                    # extract, clean, transform, load
sql/                    # DDL/queries/vistas
dashboards/
  ├─ tableau/
  └─ powerbi/
infra/                  # Dockerfile, Jenkinsfile, Ansible
data/
  ├─ raw/
  ├─ clean/
  └─ processed/
docs/

python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
cp .env.example .env        # Rellena DATABASE_URL con tu cadena de Neon

docs: visión, KPIs y arquitectura inicial

```

# Día 2 – Creación y sincronización del repositorio GitHub

## Objetivo
Conectar el entorno local de desarrollo con GitHub para garantizar control de versiones, visibilidad del código y trazabilidad de avances durante la FCT.

---

## Tareas realizadas
1. Crear el repositorio remoto `streaming_project` en GitHub.  
2. Clonar el repositorio mediante **GitHub Desktop** o `git clone`.  
3. Mover la estructura local dentro del repositorio clonado.  
4. Realizar el primer *commit* (`init: estructura base`) y subir los cambios.  
5. Verificar la sincronización local ↔ remoto.  

---

## Comandos utilizados

```bash
git init
git remote add origin https://github.com/<usuario>/streaming_project.git
git add .
git commit -m "init: estructura base del proyecto"
git push -u origin main



---

## 📄 Contenido de `docs/day2/fuentes_datos.md`

```markdown
# Fuentes de datos potenciales (avance Día 3)

## Datasets candidatos
- **TMDB API:** películas, ratings, popularidad.  
- **IMDb (BigQuery):** dataset público con metadatos y ratings.  
- **Netflix Kaggle Dataset:** CSV con catálogo y duración.  

## Notas
- Verificar licencias y términos de uso.  
- Documentar rutas de acceso y claves API en `.env.example`.  
- Guardar ejemplos de respuestas (TMDB API) en `/data/raw/`.


git add docs\day2 data\hello.txt
git commit -m "docs(day2): sincronización GitHub completada y evidencias añadidas"
git push
