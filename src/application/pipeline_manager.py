import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from domain.etl_process import ETLProcess
from infrastructure.data_access.database_client import MongoDBClient

class PipelineManager:
    def __init__(self, csv_path, collection_name):
        self.csv_path = csv_path
        self.collection_name = collection_name
        self.db_client = MongoDBClient()

    def run_pipeline(self):
        try:
            etl_process = ETLProcess(self.csv_path, self.db_client)
            etl_process.run(self.collection_name)
        except Exception as e:
            print(f"Error occurred during pipeline execution: {e}")
            raise
    def close(self):
        try:
            self.db_client.close()
        except Exception as e:
            print(f"An error occurred while closing the database connection: {str(e)}")
