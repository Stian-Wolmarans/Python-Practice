import numpy as np

def convert(sentance): 
    return (sentance[0].split())

#manual way
"""def wordswap(words):
    lst = [words]
    array = (convert(lst))
    print(array)
    n = len(array)
    newarray = []
    for i in range(0,n):
        newarray.append(array[n-1-i])
    print(newarray) """   

#simple function way
def wordswap2(words):
    lst = [words]
    array = (convert(lst))
    print(array)
    array.reverse()
    print(array)
    
wordswap2("The duck may swim on the lake but my daddy owns the lake")



    
