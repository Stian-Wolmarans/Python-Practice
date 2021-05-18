import numpy as np
import string
import random

def convertToString(string):
    newString = ''.join([str(elem) for elem in string])

    return newString

def genRandomString():
    
    password = []

    #generate some random numebrs
    for i in range(0,20):
        x = np.random.randint(0,9)
        password.append(x)
        i = i
    #generate some random characters
    for i in range(0,20):
        x = random.choice(string.ascii_letters)
        password.append(x)
        i = i

    #generate some random symbols
    for i in range(0,20):
        x = random.choice(string.punctuation)
        password.append(x)
        i = i
    #permutate array
    np.random.shuffle(password)

    #convert to string
    passwordString = convertToString(password)
    
    return passwordString

def genPasswordQuick():
    password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(60)])
    return password

def Main():
    password1 = genRandomString()
    print("Password 1: ", password1)
    password2 = genPasswordQuick()
    print("Password 2: ", password2)    

Main()