import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from application.pipeline_manager import PipelineManager

def main():
    try:
        csv_path = 'src/infrastructure/data/raw/synthetic_property_data.csv'
        collection_name = 'property_maintenance'
        pipeline_manager = PipelineManager(csv_path, collection_name)
        pipeline_manager.run_pipeline()
        pipeline_manager.close()
    except Exception as e:
        print("An error occurred during pipeline execution:", str(e))

if __name__ == "__main__":
    main()
