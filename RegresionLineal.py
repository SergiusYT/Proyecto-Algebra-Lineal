import numpy as np
import requests
import matplotlib.pyplot as plt

# Hacer la solicitud GET al script PHP que devuelve los datos
response = requests.get("http://localhost/Algebra%20Lineal/Datos/BaseDatos.php")

# Obtener los datos como una lista de listas desde la respuesta JSON
data = response.json()

# Convertir las cadenas a números
data = [[float(value) if i != 1 else int(value) for i, value in enumerate(row)] for row in data]

# Convertir la lista de listas a un array numpy
data_np = np.array(data)

# Utilizar solo la columna correspondiente a "Edad"
X = data_np[:, 0]  # Seleccionar la primera columna (Edad y Genero)
y = data_np[:, -1]  # Última columna (Calificación)

# Evitar notación científica y conservar la precisión máxima
np.set_printoptions(suppress=True, floatmode='maxprec')

# Añadir una columna de unos para representar el término independiente en la regresión
X = np.column_stack((np.ones(len(X)), X))

# Calcular X^T Matriz Transpuesta de la matriz diseño
X_T = np.transpose(X)

# Calcular X^T X Se multiplica o se saca el producto punto la transpuesta de la matriz diseño con la misma matriz de diseño pero la normal o base 
X_T_X = np.dot(X_T, X)

# Calcular (X^T X)^-1 se saca la inversa del resultado de la multiplicación
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

# Gráfico de dispersión de los datos
plt.scatter(X[:, 1], y, label='Datos reales', color='blue')

# Línea de regresión
x_values = np.linspace(min(X[:, 1]), max(X[:, 1]), 100)
y_values = theta[0] + theta[1] * x_values
plt.plot(x_values, y_values, label='Regresión lineal', color='red')

# Etiquetas y leyenda
plt.xlabel('Edad')
plt.ylabel('Calificación')
plt.legend()

# Mostrar la gráfica
plt.show()