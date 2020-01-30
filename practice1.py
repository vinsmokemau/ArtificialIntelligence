"""Practice 1: Compare Validity Clusters."""
import numpy as np
from scipy.stats import entropy
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# Generating the sample data from make_blobs

X, Y = make_blobs(centers=4)

no_of_clusters = [2, 3, 4, 5, 6]

plt.figure(1)
plt.plot(X[:, 0], X[:, 1], 'bo')

"""C-means with Entropy."""
n, car = X.shape

max_data_number = max(max(X[:, 0], X[:, 1], key=lambda x: abs(x[1])))

for n_clusters in no_of_clusters:

    V = np.random.rand(n_clusters, car) * max_data_number
    D = np.zeros((n_clusters, 100))
    U = np.zeros((n_clusters, 100))
    epsilon = 1

    while epsilon > 10**(-10):
        Vold = np.array(V)
        for i in range(n_clusters):
            for k in range(n):
                a = 1**(-10)
                for j in range(car):
                    a = (X[k, j] - V[i, j])**(2) + a
                D[i, k] = a ** (1 / 2)

        for i in range(n_clusters):
            for k in range(n):
                b = 0
                for j in range(n_clusters):
                    b = (D[i, k] / D[j, k])**2 + b
                U[i, k] = 1 / b

        for i in range(n_clusters):
            for j in range(car):
                c = 0
                d = 0
                for k in range(n):
                    c = ((U[i, k]**2) * X[k, j]) + c
                    d = ((U[i, k]**2)) + d
                V[i, j] = c / d
        epsilon = sum(sum(abs(Vold[:] - V[:])))

    total_entropy = 0

    for i in range(n_clusters):
        total_entropy += entropy(U[i])

    total_entropy *= -(1 / 100)

    print("For no of clusters =", n_clusters,
          " The entropy is :", total_entropy)

    plt.figure('Entropy {}'.format(n_clusters))
    plt.plot(X[:, 0], X[:, 1], 'bo')
    plt.plot(V[:, 0], V[:, 1], 'r*')

"""K-means with Silhoutte."""

for n_clusters in no_of_clusters:

    kmeans = KMeans(n_clusters=n_clusters)
    # Fitting with inputs
    kmeans = kmeans.fit(X)
    # Predicting the clusters
    labels = kmeans.predict(X)
    # Getting the cluster centers
    centers = kmeans.cluster_centers_

    plt.figure('Silhoutte {}'.format(n_clusters))
    plt.plot(X[:, 0], X[:, 1], 'bo')
    plt.plot(centers[:, 0], centers[:, 1], 'r*')

    # The silhouette_score gives the average value for all the samples.
    silhouette_avg = silhouette_score(X, labels)

    print("For no of clusters =", n_clusters,
          " The average silhouette_score is :", silhouette_avg)

plt.show()
