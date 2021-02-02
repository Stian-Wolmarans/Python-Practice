import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
x = np.random.normal(100, 20, 200)

#plt.hist(x)
#plt.show()

fig = plt.figure(figsize = (10,7))
plt.boxplot(x)
plt.show()