import numpy as np

def convert(sentance): 
    return (sentance[0].split())

def wordswap(words):
    lst = [words]
    array = (convert(lst))
    print(array)
    n = len(array)
    newarray = []
    for i in range(0,n):
        newarray.append(array[n-1-i])
    print(newarray)    
    
wordswap("This is my new longer sentance")



    
