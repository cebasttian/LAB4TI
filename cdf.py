import numpy as np
import matplotlib.pyplot as plt

data1 = [4.07, 4.37, 5.05,5.34,6.05,2.59,4.77,9.49,9.67,6.90,9.80,8.27,9.20,8.30,10.48,11.84,15.27,5.38,9.18,7.46,5.22,5.36,3.10,6.02,7.42,5.52,10.10,8.27,4.93,8.89,8.93,12.91,15.81,15.83,12.83,12.16,22.86,27.14,19.63,21.54,25.38,25.06,26.28,27.06,22.80,18.50,24.66,30.49,26.40,27.18]
data2 = [8.76, 10.01, 10.05, 11.11, 11.00,11.63,12.61,10.64,10.72,11.67,11.99,12.48,12.03,12.97,11.48,10.77,11.74,12.30,13.13,13.15,12.06,12.76,12.54,13.01,13.07,13.81,14.35,13.18,13.20,13.31,13.52,17.31,21.66,23.47,26.48,28.15,28.39,30.24,27.20,26.69,27.12,26.60,25.23,26.01,26.06,26.48,29.06,30.02,28.96,28.17]

sorted_data1 = np.sort(data1)
sorted_data2 = np.sort(data2)

cdf1 = np.cumsum(sorted_data1) / np.sum(sorted_data1)
cdf2 = np.cumsum(sorted_data2) / np.sum(sorted_data2)

plt.plot(sorted_data1, cdf1, label='CDF Piso 5')
plt.plot(sorted_data2, cdf2, label='CDF Piso 4')
plt.xlabel('Valores')
plt.ylabel('CDF')
plt.title('Función de Distribución Acumulativa (CDF)')
plt.legend()
plt.grid(True)
plt.show()

