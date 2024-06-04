from application.pipeline_manager import PipelineManager

def main():
    try:
        pipeline_manager = PipelineManager('src/infrastructure/data/raw/data.csv')
        pipeline_manager.run_pipeline()
        pipeline_manager.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
