from sklearn.metrics import mean_squared_error
import numpy as np

def evaluate_model(fitted_model, data, steps=12):
    forecast = fitted_model.forecast(steps=steps)
    actual = data['Enplaned'].iloc[-steps:]
    rmse = np.sqrt(mean_squared_error(actual, forecast[:steps]))
    return forecast, rmse
def save_evaluation(rmse, filepath="results/evaluation.txt"):
    with open(filepath, "w") as file:
        file.write(f"Model Evaluation\n")
        file.write(f"-----------------\n")
        file.write(f"RMSE: {rmse}\n")
def save_evaluation(rmse, filepath="results/evaluation.txt"):
    with open(filepath, "w") as file:
        file.write(f"Model Evaluation\n")
        file.write(f"-----------------\n")
        file.write(f"RMSE: {rmse}\n")
import os

def save_evaluation(rmse, filepath=None):
    if filepath is None:
        # Use an absolute path to the results folder
        project_root = os.path.dirname(os.path.dirname(__file__))  # Go up one level from `src`
        filepath = os.path.join(project_root, "results", "evaluation.txt")

    # Write the RMSE to the specified file
    with open(filepath, "w") as file:
        file.write("Model Evaluation\n")
        file.write("-----------------\n")
        file.write(f"RMSE: {rmse}\n")
