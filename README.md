# Streaming – ETL and Cloud Data Analysis (Demo Project)

**Streaming** is a professional data engineering demo project focused on analytics in the audiovisual sector.  
The objective is to build a **fully functional ETL pipeline** using a **local dataset**, replicating a realistic data engineering workflow without relying on external APIs.

This project is **officially completed on Day 10**, delivering a 100% operational ETL pipeline:  
dataset cleaning, SQL schema creation, and final loading into Neon PostgreSQL.

---

## 1. Overview

The project implements a complete ETL workflow consisting of:

- Reading the original dataset (Netflix demo).  
- Cleaning and normalizing data using Pandas.  
- Designing a relational model and SQL schema.  
- Loading final data into Neon PostgreSQL using SQLAlchemy.  
- Full pipeline validation.

The entire workflow is reproducible from scratch.

---

## 2. Objectives

- Process and clean a local dataset.  
- Define a structured SQL schema for the `movies` table.  
- Load the cleaned dataset into Neon PostgreSQL.  
- Build a modular and maintainable ETL pipeline.  
- Document the project architecture and execution.

---

## 3. Technologies Used

| Stage | Tools / Technologies |
|--------|-----------------------|
| Extraction | Local CSV |
| Transformation | Python, Pandas |
| Load | SQLAlchemy, PostgreSQL (Neon Cloud) |
| Validation | SQL, Python |
| Version Control | Git, GitHub |

---

## 4. Project Structure

```
streaming_project/
│
├── data/
│   ├── raw/
│   │   └── movies_raw.csv
│   ├── clean/
│   │   └── movies_clean.csv
│   └── processed/
│       └── movies_from_tmdb_demo.csv   (si lo quieres quitar, lo quitamos)
│
├── dashboards/
│   └── README.md
│
├── docs/
│   ├── kpis.md
│   ├── progreso.md
│   ├── scope.md
│   └── setup.md
│
├── etl/
│   ├── clean_local_netflix_csv.py
│   ├── reset_schema.py
│   ├── apply_schema.py
│   ├── etl_load_movies.py
│   ├── test_connection.py
│   ├── check_tables.py
│   └── check_connection_direct.py
│
├── sql/
│   └── 000_schema.sql
│
├── .env
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt

```

---

## 5. Development Status (Project Closed on Day 10)

| Day | Phase | Status | Description |
|-----|--------|---------|-------------|
| 1 | Planning | Completed | Scope definition and system architecture. |
| 2 | Dataset | Completed | Import and initial organization of the local dataset. |
| 3 | Environment | Completed | Virtual environment setup and Neon connection. |
| 4 | Repository | Completed | Initial folder structure and version control. |
| 5 | Exploration | Completed | Preliminary dataset exploration. |
| 6 | Data Model | Completed | MER design and `movies` table structure. |
| 7 | SQL Schema | Completed | DDL implementation in Neon PostgreSQL. |
| 8 | Cleaning | Completed | Dataset cleaning and normalization (`movies_clean.csv`). |
| 9 | Load | Completed | Final load into Neon using SQLAlchemy. |
| 10 | ETL Pipeline | Completed | Fully validated end-to-end ETL. |

This project is officially closed on **Day 10**.

---

## 6. ETL Pipeline

| Stage | Description | Output |
|--------|-------------|---------|
| Extract | Read local dataset (`movies_raw.csv`). | Raw data in `data/raw/`. |
| Transform | Cleaning, column selection, normalization. | `movies_clean.csv` in `data/clean/`. |
| Load | Apply SQL schema and load into Neon. | `movies` table with 7,973 rows. |
| Validate | Test queries and verification. | ETL pipeline validated end-to-end. |

---

## 7. How to Run the Project

### 1. Create environment and install dependencies

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Clean local dataset

```
python etl/clean_local_netflix_csv.py
```

### 3. Reset Neon schema

```
python etl/reset_schema.py
```

### 4. Apply SQL schema

```
python etl/apply_schema.py
```

### 5. Load cleaned data

```
python etl/etl_load_movies.py
```

---

## 8. Final Results

- Clean and normalized dataset (`movies_clean.csv`).  
- SQL schema applied successfully in Neon.  
- `movies` table created and populated.  
- Fully modular and reproducible ETL pipeline.  
- Project officially **completed and closed on Day 10**.

---

## 9. Author

Developed by  
**Stefan Eduard Ababei Jorascu**  
GitHub Repository: https://github.com/Eduard-Ababei/streaming-etl-pipeline 
