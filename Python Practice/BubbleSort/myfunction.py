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


