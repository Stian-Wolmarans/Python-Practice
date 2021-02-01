import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(-3.14,3.14, 100, int,)
y = numpy.sin(x)

plt.plot(x,y)
plt.draw()
plt.show()

