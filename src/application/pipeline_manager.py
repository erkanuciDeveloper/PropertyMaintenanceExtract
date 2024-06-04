import os
import sys

from domain.etl_process import ETLProcess
from infrastructure.data_access.database_client import MongoDBClient

class PipelineManager:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.db_client = MongoDBClient()

    def run_pipeline(self):
        try:
            etl_process = ETLProcess(self.csv_path, self.db_client)
            etl_process.run()
        except Exception as e:
            print(f"An error occurred during pipeline execution: {str(e)}")

    def close(self):
        try:
            self.db_client.close()
        except Exception as e:
            print(f"An error occurred while closing the database connection: {str(e)}")
