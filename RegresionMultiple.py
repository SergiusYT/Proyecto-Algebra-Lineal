import numpy as np
import requests
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Hacer la solicitud GET al script PHP que devuelve los datos
response = requests.get("http://localhost/Algebra%20Lineal/Datos/BaseDatos.php")

# Obtener los datos como una lista de listas desde la respuesta JSON
data = response.json()

# Convertir las cadenas a números
data = [[float(value) if i != 1 else int(value) for i, value in enumerate(row)] for row in data]

# Convertir la lista de listas a un array numpy
data_np = np.array(data)

# Ahora puedes utilizar data_np como los valores X e y en tu script de Python
X = data_np[:, :-1]  # Todas las columnas excepto la última
y = data_np[:, -1]   # Última columna

# Evitar notación científica y conservar la precisión máxima
np.set_printoptions(suppress=True, floatmode='maxprec')

# Añadir una columna de unos para representar el término independiente en la regresión
X = np.column_stack((np.ones(len(X)), X))

# Calcular X^T  Matriz Transpuesta de la matriz diseño 
X_T = np.transpose(X)

# Calcular X^T X  Se multiplica la transpuesta de la matriz diseño con la misma matriz de diseño pero la normal o base
X_T_X = np.dot(X_T, X)

# Calcular (X^T X)^-1  se saca la inversa del resultado de la multiplicacion
X_T_X_inv = np.linalg.inv(X_T_X)

# Calcular X^+
X_pseudo_inv = np.dot(X_T_X_inv, X_T)

# Calcular los coeficientes de la regresión lineal
theta = np.dot(X_pseudo_inv, y)

# Imprimir resultados
print("\nMatriz X:")
print(X)
print("\nMatriz Y:")
print(y)
print("\nMatriz X^T:")
print(X_T)
print("\nMatriz X^T X:")
print(X_T_X)
print("\nInversa de (X^T X):")
print(X_T_X_inv)
print("\nPseudoinversa (X^+):")
print(X_pseudo_inv)
print("\nCoeficientes:")
print(theta)

# Gráfico de dispersión 3D de los datos
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 1], X[:, 2], y, label='Datos reales', c='blue', marker='o')

# Plano de regresión
x1_values, x2_values = np.meshgrid(np.linspace(min(X[:, 1]), max(X[:, 1]), 100), np.linspace(min(X[:, 2]), max(X[:, 2]), 100))
plane = theta[0] + theta[1] * x1_values + theta[2] * x2_values
ax.plot_surface(x1_values, x2_values, plane, alpha=0.5, color='red', label='Plano de regresión') # type: ignore

# Etiquetas y leyenda
ax.set_xlabel('Edad')
ax.set_ylabel('Género')
ax.set_zlabel('Calificación') # type: ignore
ax.legend()

# Mostrar la gráfica
plt.show()