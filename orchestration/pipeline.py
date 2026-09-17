import subprocess
from pathlib import Path
from prefect import flow, task

# Rutas
PROJECT_ROOT = Path(__file__).parent.parent
DBT_PROJECT = PROJECT_ROOT / "olist_dbt"

@task(name="Ingest Data")
def ingest_data():
    print("Iniciando ingesta de datos...")
    result = subprocess.run(
        ["python", str(PROJECT_ROOT / "ingestion" / "load_data.py")],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Error en ingesta: {result.stderr}")
    print(result.stdout)
    print("✅ Ingesta completada")

@task(name="Transform Data")
def transform_data():
    print("Iniciando transformaciones dbt...")
    result = subprocess.run(
        ["dbt", "run"],
        cwd=str(DBT_PROJECT),
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Error en dbt run: {result.stderr}")
    print(result.stdout)
    print("✅ Transformaciones completadas")

@task(name="Test Data Quality")
def test_data_quality():
    print("Corriendo tests de calidad...")
    result = subprocess.run(
        ["dbt", "test"],
        cwd=str(DBT_PROJECT),
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Error en dbt test: {result.stderr}")
    print(result.stdout)
    print("✅ Tests completados")

@flow(name="Olist Pipeline")
def olist_pipeline():
    ingest_data()
    transform_data()
    test_data_quality()

if __name__ == "__main__":
    olist_pipeline()