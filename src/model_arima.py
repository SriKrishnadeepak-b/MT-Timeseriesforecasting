from statsmodels.tsa.arima.model import ARIMA
import itertools

def select_arima_model(data):
    p = d = q = range(0, 3)
    pdq = list(itertools.product(p, d, q))
    best_aic = float("inf")
    best_order = None

    for param in pdq:
        try:
            model = ARIMA(data['Enplaned'], order=param)
            results = model.fit()
            if results.aic < best_aic:
                best_aic = results.aic
                best_order = param
        except:
            continue
    return best_order

def train_arima(data, order):
    model = ARIMA(data['Enplaned'], order=order)
    return model.fit()
