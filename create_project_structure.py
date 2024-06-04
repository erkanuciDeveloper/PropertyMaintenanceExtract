import os

# Define the directory structure
def create_directory_structure(root_dir):
    directories = [
        'src/presentation/app',
        'src/application',
        'src/domain/utils',
        'src/infrastructure/data_access',
        'src/infrastructure/logs',
        'src/infrastructure/exceptions',
        'tests/unit',
    ]

    for directory in directories:
        os.makedirs(os.path.join(root_dir, directory), exist_ok=True)

    files = [
        'src/presentation/app/__init__.py',
        'src/presentation/app/app.py',
        'src/application/__init__.py',
        'src/application/pipeline_manager.py',
        'src/domain/__init__.py',
        'src/domain/etl_process.py',
        'src/domain/utils/__init__.py',
        'src/domain/utils/data_utils.py',
        'src/infrastructure/data_access/database_client.py',
        'src/infrastructure/exceptions/custom_exceptions.py',
        'tests/unit/test_etl_process.py',
        'docker-compose.yml',
        'requirements.txt',
        'README.md',
        'setup.py'
    ]

    for filepath in files:
        with open(os.path.join(root_dir, filepath), 'w') as file:
            file.write('')

if __name__ == "__main__":
    project_root = "C:/Workspace/PropertyMaintenanceExtract" 
    create_directory_structure(project_root)
    print("Project structure and files created successfully.")
