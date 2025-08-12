from sklearn.linear_model import LinearRegression
import numpy as np

def train_and_predict(data_desc: str):
    # Dummy training example
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    model = LinearRegression()
    model.fit(X, y)
    pred = model.predict([[6]])[0]
    return f"Predicted value for 6: {pred}"
