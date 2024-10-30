# Time Series Forecasting Project

## Project Overview
This project is a time series forecasting model designed to predict future values of "Enplaned Passengers" based on historical data. The model uses an ARIMA approach to capture trends and seasonality in the data.

## Files and Structure
- `data/your_dataset.csv`: The dataset used for forecasting.
- `src/data_preprocessing.py`: Handles data loading and preprocessing.
- `src/model_arima.py`: Contains functions to select and train the ARIMA model.
- `src/model_evaluation.py`: Evaluates the model's performance and saves RMSE.
- `src/main.py`: Main script that orchestrates the workflow.
- `results/evaluation.txt`: Contains the RMSE value for model evaluation.

## Project Steps
1. **Data Loading and Preprocessing**: The data is loaded, and preprocessing is applied to make it suitable for time series forecasting.
2. **Model Selection**: ARIMA parameters are selected based on AIC values.
3. **Model Training**: The ARIMA model is trained on the "Enplaned Passengers" data.
4. **Evaluation**: The model's performance is measured using RMSE, and the forecast is visualized.

## Results
- The RMSE for the model is stored in `results/evaluation.txt`.
- The forecast plot (generated in `main.py`) shows the predicted values alongside the actual values.

## How to Run
1. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
python src/main.py
