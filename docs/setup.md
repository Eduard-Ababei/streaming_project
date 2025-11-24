# Project Setup Guide – Streaming ETL Demo

This document explains how to configure, run, and validate the complete ETL pipeline for the **Streaming Demo Project** using Python, PostgreSQL (Neon), and SQLAlchemy.

---

## 1. Requirements

Before starting, ensure you have:

- Python 3.10+  
- Git  
- Visual Studio Code  
- Access to a Neon PostgreSQL database  
- A valid `.env` file (not included in the repository)

# Core Python Dependencies
- Library	Purpose
- pandas	Data cleaning and transformation
- SQLAlchemy	Database engine and ORM
- psycopg2	  PostgreSQL driver
- python-dotenv	  Environment variable loading

---

## 2. Project Structure

```
streaming_project/
│
├── data/
│   ├── raw/            # Original dataset
│   ├── clean/          # Cleaned dataset
│   └── processed/      # Optional intermediate files
│
├── docs/               # Documentation
├── etl/                # ETL scripts
├── sql/                # SQL schema
├── .env                # Environment variables (NOT committed)
├── .env.example        # Template for environment variables
└── requirements.txt    # Dependencies
```

---

## 3. Environment Setup

### 1. Create virtual environment

```
python -m venv .venv
```

### 2. Activate it

Windows:

```
.\.venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Environment Variables

The project requires one environment variable:

```
DATABASE_URL=
```

### Example (`.env.example`)

```
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@HOST/DATABASE?sslmode=require
```

### Real credentials must be stored in:

```
.env
```

This file MUST NOT be committed to Git and is already included in `.gitignore`.

---

## 5. Running the ETL Pipeline

### Step 1 — Clean the local dataset

```
python etl/clean_local_netflix_csv.py
```

This generates:

```
data/clean/movies_clean.csv
```

---

### Step 2 — Reset the database schema in Neon

```
python etl/reset_schema.py
```

---

### Step 3 — Apply SQL schema

```
python etl/apply_schema.py
```

This creates the `movies` table based on `sql/000_schema.sql`.

---

### Step 4 — Load cleaned data into Neon

```
python etl/etl_load_movies.py
```

This uploads ~7,973 rows into the `movies` table.

---

## 6. Connection Testing

To validate your Neon connection:

```
python etl/test_connection.py
```

To confirm that the target tables exist:

```
python etl/check_tables.py
```

---

## 7. Manual Validation in Neon

You can inspect the database visually by opening:

```
https://console.neon.tech
```

Example SQL:

```sql
SELECT * FROM movies LIMIT 10;
```

---

## 8. Common Issues & Fixes

### Missing libraries  
Install dependencies:

```
pip install -r requirements.txt
```

### Wrong Python interpreter  
Ensure VS Code is using:

```
.\.venv\Scripts\python.exe
```

### Database authentication errors  
Verify `.env`:

```
DATABASE_URL=...
```

---

## 9. Security Notes

- NEVER commit `.env` or credentials.  
- ALWAYS commit `.env.example`.  
- Do not store RAW passwords in documentation.  
- `AYUDA.TXT` has been fully replaced by this guide.

---

## 10. Project Status

This project is **complete**, finalised on **Day 10**, and ready for use as a professional ETL demo.

---

## Author

Developed by **Stefan Eduard Ababei Jorascu**  
GitHub: https://github.com/Eduard-Ababei/streaming_project

