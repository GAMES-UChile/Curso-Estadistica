import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Crear muestra

N = 5000
mu = 3

X = stats.poisson.rvs(mu, size=N)

# Definir confianza

alpha = stats.norm.ppf(1-0.05/2)

vect_medias = np.array([])
medias_index = np.array([])

for j in range(1,N+1):
    """
    Graficar la diferencia entre lambda teórico y práctico para distintos
    valores de n, haciendo primero el cálculo del promedio, plotearlos
    y luego trazar la curva que simbolice el error de estimación
    """
    media = np.mean(X[:j])
    vect_medias = np.append(vect_medias, media)
    medias_index = np.append(medias_index, media/j)

espaciado = np.arange(5000) + 1
diff = np.abs(vect_medias -3)
delta = alpha*np.sqrt(medias_index)