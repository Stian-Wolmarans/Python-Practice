def arrayprint(array):
    for x in array:
        print(x)

def bubblesort(array):
    n = len(array)
    print(array)
    print("Array length is: ", n)
    i = 0
    while(i < n):
        y = 0
        for x in array:
            if y < n - 1:
                if array[y] > array[y+1]:
                    array[y],array[y+1] = array[y+1],array[y]
                    y = y + 1
                else:
                    y = y + 1
        i = i + 1
    print("Array bubble sort: ")
    print(array)

def bubblesortop(array):
    n = len(array)
    for i in range(n-1):
        print("Outer Loop")
        print(array)
        for j in range(0,n-i-1):
            print(array)
            print("Inner Loop")
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    print("Sorted array is:", array)

