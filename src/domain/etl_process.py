import pandas as pd

class ETLProcess:
    def __init__(self, csv_path, db_client):
        self.csv_path = csv_path
        self.db_client = db_client

    def extract_data(self):
        try:
            return pd.read_csv(self.csv_path)
        except Exception as e:
            raise Exception(f"Error occurred during data extraction: {str(e)}")

    def transform_data(self, df):
        try:
            # Transformation logic
            pass
        except Exception as e:
            raise Exception(f"Error occurred during data transformation: {str(e)}")

    def load_data(self, dim_property, fact_maintenance):
        try:
            self.db_client.insert_many('dim_property', dim_property)
            self.db_client.insert_many('fact_maintenance', fact_maintenance)
        except Exception as e:
            raise Exception(f"Error occurred during data loading: {str(e)}")

    def run(self):
        try:
            df = self.extract_data()
            dim_property, fact_maintenance = self.transform_data(df)
            self.load_data(dim_property, fact_maintenance)
        except Exception as e:
            raise Exception(f"Error occurred during ETL process: {str(e)}")
