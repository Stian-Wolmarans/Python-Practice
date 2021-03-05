import numpy as np

def firstend():
    array = np.random.randint(1,100, size = 10)
    array2 = []
    n = len(array)
    array2.append(array[0])
    array2.append(array[n-1])

    print(array)
    print(array2)

firstend()