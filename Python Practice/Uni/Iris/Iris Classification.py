import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

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
    data = pd.read_csv("iris.data")
    inputs = data.data
    targets = data.target
    print(data)  

#Ex1()
Ex2()
