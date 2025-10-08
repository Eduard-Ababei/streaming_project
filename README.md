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

## Día 2 – Creación y sincronización del repositorio GitHub

**Objetivo:** conectar el proyecto local con GitHub para control de versiones y visibilidad pública.

### Pasos realizados
1. Creé el repositorio remoto **`streaming_project`** en GitHub.  
2. Cloné el repositorio mediante **GitHub Desktop**.  
3. Moví la estructura local dentro del repositorio clonado.  
4. Realicé el primer *commit* y subí los cambios.  
5. Verifiqué la sincronización local ↔ remoto.

### Evidencias
- Captura del repositorio online  
- Captura del primer commit en GitHub Desktop  
- Carpeta `data/hello.txt` subida correctamente

### Commit sugerido
```bash
git add .
git commit -m "docs: sincronización GitHub completada"
git push

```

