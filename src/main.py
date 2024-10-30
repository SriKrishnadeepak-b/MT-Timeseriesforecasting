import os
from src.data_preprocessing import load_data, preprocess_data
from src.model_arima import select_arima_model, train_arima
from src.model_evaluation import evaluate_model
import matplotlib.pyplot as plt

# Load and preprocess data
data_path = os.path.join("..", "data", "your_dataset.csv")
data = load_data(data_path)
data = preprocess_data(data)

# Select and train ARIMA model
best_order = select_arima_model(data)
print(f"Best ARIMA order: {best_order}")
fitted_model = train_arima(data, best_order)

# Evaluate model and plot results
forecast, rmse = evaluate_model(fitted_model, data)
print(f"RMSE: {rmse}")

# Plot forecast
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Enplaned'], label="Actual")
plt.plot(data.index[-len(forecast):], forecast, label="Forecast")
plt.title("ARIMA Forecast of Enplaned Passengers")
plt.legend()
plt.show()
from src.model_evaluation import evaluate_model, save_evaluation

# Evaluate model and plot results
forecast, rmse = evaluate_model(fitted_model, data)
print(f"RMSE: {rmse}")

# Save evaluation result
save_evaluation(rmse)
from src.model_evaluation import evaluate_model, save_evaluation

# Evaluate model and plot results
forecast, rmse = evaluate_model(fitted_model, data)
print(f"RMSE: {rmse}")

# Save evaluation result
save_evaluation(rmse)
