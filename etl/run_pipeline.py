import subprocess
import time
import sys
import os

# ------------------------------------------------------------
# Detect project root dynamically
# ------------------------------------------------------------
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
ETL_DIR = os.path.join(PROJECT_ROOT, "etl")

# ------------------------------------------------------------
# Pipeline steps
# ------------------------------------------------------------
STEPS = [
    ("Cleaning dataset", "clean_local_netflix_csv.py"),
    ("Resetting database schema", "reset_schema.py"),
    ("Applying SQL schema", "apply_schema.py"),
    ("Loading cleaned data into Neon", "etl_load_movies.py"),
]


def run_step(description, script_name):
    """Execute a single ETL step."""
    print("\n====================================================")
    print(f"[STEP] {description}")
    print("====================================================")

    script_path = os.path.join(ETL_DIR, script_name)

    if not os.path.exists(script_path):
        print(f"[ERROR] Script not found: {script_path}")
        sys.exit(1)

    try:
        result = subprocess.run(
            [sys.executable, script_path],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",     # Prevent Windows CP1252 crashes
        )

        print(result.stdout)
        print("[OK] Step completed successfully.")

    except subprocess.CalledProcessError as e:
        print("\n[ERROR] Step failed:")
        print(e.stderr)
        sys.exit(1)


def main():
    print("\n===============================================")
    print(" STREAMING ETL PIPELINE — Full Execution")
    print("===============================================")
    print(f"[INFO] Project root detected: {PROJECT_ROOT}\n")

    start = time.time()

    for description, script in STEPS:
        run_step(description, script)

    duration = round(time.time() - start, 2)

    print("\n===============================================")
    print("[SUCCESS] ETL Pipeline completed successfully.")
    print(f"[INFO] Total runtime: {duration} seconds")
    print("===============================================")


if __name__ == "__main__":
    main()
