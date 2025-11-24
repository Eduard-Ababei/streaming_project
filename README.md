# Streaming ETL Pipeline — Data Engineering Demo Project

This project implements a clean, modular and fully reproducible **ETL pipeline** using Python, Pandas, SQLAlchemy and Neon PostgreSQL.  
It simulates a realistic data engineering workflow using a local dataset and delivers a complete end-to-end solution within a structured 10-day development cycle.

The ETL process includes:

- **Extract:** load the raw Netflix dataset  
- **Transform:** clean and normalize movie metadata  
- **Load:** ingest data into Neon PostgreSQL  
- **Validate:** execute SQL queries to confirm correct ingestion  

---

## 1. Overview

The pipeline performs the following steps:

- Read a raw dataset (`movies_raw.csv`)
- Clean and validate records (Pandas)
- Apply a SQL schema (DDL)
- Load data into Neon PostgreSQL (SQLAlchemy)
- Validate using SQL queries
- Orchestrate the complete workflow using `run_pipeline.py`

The focus is on clarity, modularity, reproducibility and professional ETL engineering practices.

---

## 2. Technologies Used

| Category | Tools / Libraries |
|----------|-------------------|
| Language | Python 3.x |
| ETL | Pandas, SQLAlchemy |
| Database | PostgreSQL (Neon Cloud) |
| Environment | .env, python-dotenv |
| Orchestration | Subprocess runner |
| Version Control | Git & GitHub |

---

## 3. Project Structure

```
streaming-etl-pipeline/
│
├── data/
│   ├── raw/
│   │   └── movies_raw.csv
│   └── clean/
│       └── movies_clean.csv
│
├── etl/
│   ├── clean_local_netflix_csv.py      # Extract & Transform
│   ├── reset_schema.py                 # Drop all existing tables
│   ├── apply_schema.py                 # Apply SQL DDL schema
│   ├── etl_load_movies.py              # Load cleaned dataset
│   ├── test_connection.py              # SQLAlchemy test
│   ├── check_connection_direct.py      # psycopg2 test
│   ├── check_tables.py                 # Inspect DB tables
│   └── run_pipeline.py                 # Full ETL orchestrator
│
├── notebooks/
│   └── Streaming_ETL_Pipeline.ipynb
│
├── sql/
│   └── 000_schema.sql
│
├── docs/
│   └── setup.md
│
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

---

## 4. Development Timeline (Project Completed on Day 10)

| Day | Phase | Status | Description |
|-----|--------|---------|-------------|
| 1 | Planning | Completed | Scope definition and system architecture. |
| 2 | Dataset | Completed | Import and initial organization of the local dataset. |
| 3 | Environment | Completed | Virtual environment setup and Neon connection. |
| 4 | Repository | Completed | Folder structure and version control. |
| 5 | Exploration | Completed | Preliminary dataset exploration. |
| 6 | Data Model | Completed | MER design and structure of `movies` table. |
| 7 | SQL Schema | Completed | DDL implementation in Neon. |
| 8 | Cleaning | Completed | `movies_clean.csv` creation. |
| 9 | Load | Completed | Data loading with SQLAlchemy. |
| 10 | ETL Pipeline | Completed | End-to-end ETL orchestration and validation. |

This project is **fully closed and complete**.

---

## 5. ETL Pipeline

| Stage | Description | Output |
|--------|-------------|---------|
| Extract | Read raw dataset (`movies_raw.csv`). | Data in `data/raw/`. |
| Transform | Cleaning, column selection, normalization. | `movies_clean.csv` in `data/clean/`. |
| Load | Apply SQL schema and load into Neon. | `movies` table with 7,973 rows. |
| Validate | Test queries and verification. | Pipeline validated end-to-end. |

---

## 6. Running the Project

### 1. Create and activate the environment

```
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Set up `.env`

Copy the values from `.env.example`.

### 4. Run the full ETL pipeline

```
python etl/run_pipeline.py
```

Or run modules individually:

```
python etl/clean_local_netflix_csv.py
python etl/reset_schema.py
python etl/apply_schema.py
python etl/etl_load_movies.py
```

---

## 7. Final Results

- Clean dataset successfully generated  
- SQL schema applied in Neon  
- `movies` table created and populated  
- 7,973 validated rows inserted  
- Full ETL pipeline is **modular, reproducible and production-style**  
- Project officially **completed on Day 10**  

---

## 8. Author

Developed by  
**Stefan Eduard Ababei Jorascu**  
GitHub: https://github.com/Eduard-Ababei/streaming-etl-pipeline
