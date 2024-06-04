import pandas as pd

class ETLProcess:
    def __init__(self, csv_path, db_client):
        self.csv_path = csv_path
        self.db_client = db_client

    def extract_data(self):
        try:
            return pd.read_csv(self.csv_path)
        except Exception as e:
            print(f"Error during data extraction: {e}")
            raise

    def transform_data(self, df):
        try:
            # Transformation logic here
            dim_property = df.copy()
            fact_maintenance = df.copy()
            return dim_property, fact_maintenance
        except Exception as e:
            print(f"Error during data transformation: {e}")
            raise

    def load_data(self, dim_property, fact_maintenance, collection_name):
        try:
            self.db_client.insert_many(f'{collection_name}_dim_property', dim_property.to_dict(orient='records'))
            self.db_client.insert_many(f'{collection_name}_fact_maintenance', fact_maintenance.to_dict(orient='records'))


            

        except Exception as e:
            print(f"Error during data loading: {e}")
            raise

    def run(self, collection_name):
        try:
            df = self.extract_data()
            dim_property, fact_maintenance = self.transform_data(df)
            self.load_data(dim_property, fact_maintenance, collection_name)
        except Exception as e:
            print(f"Error occurred during ETL process: {e}")
            raise
