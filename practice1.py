"""Practice 1: Compare Validity Clusters."""
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generating the sample data from make_blobs

X, Y = make_blobs(centers=4)

no_of_clusters = [2, 3, 4, 5, 6]

plt.figure(1)
plt.plot(X[:, 0], X[:, 1], 'bo')

for n_clusters in no_of_clusters:

    kmeans = KMeans(n_clusters=n_clusters)
    # Fitting with inputs
    kmeans = kmeans.fit(X)
    # Predicting the clusters
    labels = kmeans.predict(X)
    # Getting the cluster centers
    centers = kmeans.cluster_centers_

    plt.figure(n_clusters)
    plt.plot(X[:, 0], X[:, 1], 'bo')
    plt.plot(centers[:, 0], centers[:, 1], 'r*')

    # The silhouette_score gives the average value for all the samples.
    silhouette_avg = silhouette_score(X, labels)

    print("For no of clusters =", n_clusters,
          " The average silhouette_score is :", silhouette_avg)

plt.show()
