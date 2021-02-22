import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
#from sklearn.datasets import load_digits
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import confusion_matrix

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
    plt.imshow(inputs)
    plt.show()
       
def Ex4():
    #load data
    data = pd.read_csv("C:\\git\\Python-Practice\\Python Practice\\Uni\\Iris\\Iris.csv")

    #extact inputs
    inputs = data.values[:,:-1].astype(float)

    #extract targets
    cls = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    targets = [cls.index(c) for c in data.values[:,-1].astype(str)]
    targets = np.array(targets)    
    
    #train neural network
    regressor = MLPRegressor()
    regressor.fit(inputs, targets)
    outputs = regressor.predict(inputs)

    #show error
    print(mean_absolute_error(targets, outputs))

    #compare result to target
    data = {'y_actual': [targets], 'y_predicted': [outputs]}
    df = pd.DataFrame(data, columns = ['y_actual', 'y_predicted'])
    print(df)
    #confusion_matrix = pd.crosstab(df['y_actual'], df['y_predicted'], rownames=['Actual'], colnames=['Predicted'])
    #print(confusion_matrix)

    
#Ex1()
#Ex2()
#Ex3()
Ex4()

