# Olist E-Commerce Data Pipeline

A data engineering portfolio project built to practice real-world pipeline development using Brazilian e-commerce data.

## What this project does

Takes raw e-commerce data from Olist (100k+ orders, 9 tables, 1.6M rows) and runs it through a complete data pipeline:
- Ingests CSV files into a local DuckDB warehouse
- Transforms and cleans the data using dbt
- Validates data quality with automated tests
- Orchestrates the full pipeline with Prefect

## Stack

- **Python + pandas** — ingestion
- **DuckDB** — local warehouse
- **dbt** — transformations and testing
- **Prefect** — orchestration

## Models built

**Staging** — cleaning and standardization:
- `stg_orders`, `stg_customers`, `stg_order_items`, `stg_order_payments`

**Marts** — business metrics:
- `mart_revenue_by_city` — revenue and order volume per city
- `mart_delivery_time` — delivery performance by state
- `mart_top_products` — top 50 products by revenue

## Running the pipeline

```bash
# Install dependencies
pip install duckdb dbt-duckdb prefect pandas

# Download the dataset
# https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
# Place CSVs in the data/ folder

# Configure dbt
# Edit ~/.dbt/profiles.yml with your local DuckDB path

# Run
python orchestration/pipeline.py
```

## Dataset

[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — Kaggle# Olis-pipeline
End-to-end data engineering pipeline using Python, DuckDB, dbt and Prefect
