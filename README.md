# AAVAIL Revenue Forecasting Capstone

This repository contains a Flask-based time-series forecasting project for AAVAIL. The goal is to predict revenue by date and country, compare a baseline against a final model, and package everything in a reproducible workflow.

## What is included
- Data ingestion and feature engineering.
- Exploratory data analysis (EDA) and visualization.
- Baseline and final model training.
- Flask API for predictions.
- Unit tests for API, model, and logging.
- Docker configuration for local deployment.

## How to run

1. Create a virtual environment (optional but recommended).
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:

   ```bash
   python -m src.train
   ```

4. Start the app:

   ```bash
   python app.py
   ```

5. Run tests:

   ```bash
   python run_tests.py
   ```

6. Build Docker image:

   ```bash
   docker build -t aavail-capstone .
   ```

## API

### Health

- `GET /health`

Returns a simple JSON payload to confirm the service is up.

### Predict

- `POST /predict`

Example payload:

```json
{
  "country": "United Kingdom",
  "date": "2019-12-01"
}
```

Example response (placeholder):

```json
{
  "country": "United Kingdom",
  "date": "2019-12-01",
  "prediction": 0.0
}
```

## Project structure

- `src/` – application code (ingestion, features, model, training, prediction, logging, monitoring, visualization)
- `tests/` – unit tests for API, model, and logging
- `data/` – raw or sample data references
- `artifacts/` – saved model files
- `reports/` – plots and summaries for peer review
- `notebooks/` – notebooks for EDA and experimentation
- `logs/` – runtime logs
