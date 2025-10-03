# Carga de librerías base para todo el diplomado
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.cluster import KMeans

np.random.seed(42)
print("Versiones -> numpy:", np.__version__, "| pandas:", pd.__version__)
data = pd.read_csv("./ml_py/iris_dataset.csv")
print(data)
print(data.info())

plt.figure()
for sp, subdf in data.groupby('Class'):
    plt.scatter(subdf['SepalLength'], subdf['PetalLength'], label=sp, alpha=0.8)
plt.xlabel('Sepal length (cm)')
plt.ylabel('Petal length (cm)')
plt.legend()
plt.title('Iris: vista rápida')
plt.show()