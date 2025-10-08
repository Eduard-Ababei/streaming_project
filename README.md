# streaming_project

Analítica de streaming (películas, ratings, plataformas) con pipeline ETL → PostgreSQL (Neon) → BI (Tableau/Power BI) y CI/CD (Jenkins/Docker).

## Día 1 – Presentación y alcance
- **Problema**: integrar y analizar datos de películas (TMDB/IMDb/Netflix) para calcular KPIs y hacer predicción ligera.
- **KPIs iniciales**: rating medio por género, top N por plataforma, % estrenos por año, distribución de títulos por década, etc.
- **Arquitectura**: ETL (Python/SQLAlchemy) → Neon (PostgreSQL) → Vistas SQL para BI → Dashboards (Tableau/Power BI). CI/CD con Jenkins + Docker.
- **Evidencias**: `docs/day1/architecture.png`, `docs/day1/kpis.md`, `docs/day1/scope.md`.

## Estructura
