import pytest
import pandas as pd
from pymongo import MongoClient
from config import Config
from src.domain.etl_process import ETLProcess

@pytest.fixture(scope='module')
def db_client():
    client = MongoClient(Config.DB_HOST, Config.DB_PORT)
    db = client[Config.DB_NAME]
    yield db
    client.close()

def test_etl_process(db_client):
    csv_path = 'path/to/your/testfile.csv'  # Update with the actual path to your test CSV file
    etl_process = ETLProcess(csv_path, db_client)

    # Run the ETL process
    etl_process.run()

    # Check the inserted data
    dim_property_count = db_client.dim_property.count_documents({})
    fact_maintenance_count = db_client.fact_maintenance.count_documents({})

    assert dim_property_count > 0
    assert fact_maintenance_count > 0
