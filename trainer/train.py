import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
import matplotlib.pyplot as plt

# Datos
X = np.arange(0, 10, 0.5).reshape(-1, 1)
y = 3*X + 5 + np.random.randn(20,1)

# Entrenar modelo
model = LinearRegression()
model.fit(X, y)

# Guardar modelo
joblib.dump(model, "/models/model.pkl")

# Guardar gráfico
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.title("Modelo Entrenado")
plt.savefig("/output/training_plot.png")
