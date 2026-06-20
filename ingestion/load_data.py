import duckdb
import pandas as pd
from pathlib import Path

# Rutas
DATA_DIR = Path(__file__).parent.parent / "data"
DB_PATH = Path(__file__).parent.parent / "olist.duckdb"

# Archivos CSV a cargar
CSV_FILES = {
    "customers": "olist_customers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "product_category_translation": "product_category_name_translation.csv",
}

def load_csv_to_duckdb():
    con = duckdb.connect(str(DB_PATH))
    
    for table_name, file_name in CSV_FILES.items():
        file_path = DATA_DIR / file_name
        print(f"Cargando {file_name}...")
        df = pd.read_csv(file_path)
        con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
        print(f"✅ {table_name} — {len(df):,} filas cargadas")
    
    con.close()
    print("\n✅ Todas las tablas cargadas en DuckDB")

if __name__ == "__main__":
    load_csv_to_duckdb()