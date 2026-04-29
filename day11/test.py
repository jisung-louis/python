import numpy as np
data = np.genfromtxt("./day11/customer_purchase_data.csv", delimiter=',', skip_header=1, encoding='utf-8', dtype=str)

print(data.shape)
print(data)