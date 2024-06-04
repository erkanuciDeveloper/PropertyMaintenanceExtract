# Property Maintenance Extract Pipeline

## Overview
This project demonstrates an ETL (Extract, Transform, Load) process for property maintenance records using a star schema data model. The data is loaded into a MongoDB database hosted via Docker.

## Project Structure
- `src/`: Contains the source code.
  - `presentation/app/`: Entry point of the application.
  - `application/`: Manages the overall workflow.
  - `domain/`: Contains business logic.
  - `infrastructure/data_access/`: Manages database interactions.
  - `infrastructure/exceptions/`: Custom exceptions.
- `tests/`: Contains unit tests.
- `docker-compose.yml`: Docker configuration for MongoDB.
- `requirements.txt`: Project dependencies.
- `README.md`: Project documentation.

## Prerequisites
- Docker and Docker Compose installed.
- MongoDB installed (if not using Docker).

## How to Run

### 1. Set Up the Environment
First, clone the repository and navigate into the project directory:

```bash
git clone <repository-url>
cd PropertyMaintenanceExtract
```

### Setup Instructions

1. **Install Docker and Docker Compose**:
   - Follow the official Docker documentation for installation instructions.

2. **Start MongoDB Database**:
   ```bash
   docker-compose up -d
   ```

3. **Set Up Python Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Run the ETL Pipeline**:
   ```bash
   python src/presentation/app/app.py
   ```

5. **Verify Processed Data in MongoDB**:
   - Open MongoDB Compass and apply filters to view processed data.

6. **Stop the MongoDB Container**:
   ```bash
   docker-compose down
   ```
