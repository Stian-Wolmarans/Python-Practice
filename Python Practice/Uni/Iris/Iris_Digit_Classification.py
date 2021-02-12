import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn.datasets import load_digits

def Ex1():

    #loading iris data
    data = load_iris()
    inputs = data.data
    targets = data.target

    # Project the data into two dimensions using PCA.
    pca = PCA(n_components=2)
    compressed = pca.fit_transform(inputs)

    # Train the classifier.
    classifier = KNeighborsClassifier(n_neighbors=10)
    classifier.fit(inputs, targets)
    classifiedData = classifier.predict(inputs)

    # Plot the results.
    plt.figure()
    plt.scatter(compressed[:,0], compressed[:,1], c=classifiedData)
    plt.title("PCA projection - classified")
    plt.savefig("iris_pca_classified.png", bbox_inches="tight")
    plt.show()

def Ex2():

    #load and print data
    data = pd.read_csv("C:\\git\\Python-Practice\\Python Practice\\Uni\\Iris\\Iris.csv")
    print(data)

    #extract inputs
    inputs = data.values[:,:-1].astype(float)

    #extract targets
    cls = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    targets = [cls.index(c) for c in data.values[:,-1].astype(str)]
    targets = np.array(targets)

    #reduce dimensions
    pca = PCA(n_components=2)
    compressed = pca.fit_transform(inputs)

    # Train the classifier.
    classifier = KNeighborsClassifier(n_neighbors=10)
    classifier.fit(inputs, targets)
    classifiedData = classifier.predict(inputs)

    # Plot the results.
    plt.figure()
    plt.scatter(compressed[:,0], compressed[:,1], c=classifiedData)
    plt.title("PCA projection - classified")
    plt.savefig("iris_pca_classified.png", bbox_inches="tight")
    plt.show()

def Ex3():
    #load data
    digits = load_digits()

    #extract three parts of the data
    data = digits.data
    images = digits.images
    targets = digits.target

    
    print(data)
    print("Gap")
    print(images)
    print("Gap")
    print(targets)
    

    #reduce dimensions    
    inputs = data
    pca = PCA(n_components=2)
    compressed = pca.fit_transform(inputs)    

    #train classifier
    classifier = KNeighborsClassifier(n_neighbors=10)
    classifier.fit(inputs, targets)
    classifiedData = classifier.predict(inputs)

    #plot results using Maptplotlib imshow
    #add target value as figure title
    plt.imshow(inputs, cmap = 'Blues', 
                extent = (-2,5,-2,5,), 
                filternorm = True, 
                resample = True,
                vmin = 1,
                vmax = 1)
    plt.show()
       

#Ex1()
#Ex2()
Ex3()

