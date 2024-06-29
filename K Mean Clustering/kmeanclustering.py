# -*- coding: utf-8 -*-
"""KMeanClustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yRSRHcW5QC4QJiiOj6MrO9oZds3EcQ7g
"""

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris = load_iris()
X = iris.data

# Initialize the K-Means model
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit the model to the data
kmeans.fit(X)

# Predict the cluster for each data point
clusters = kmeans.predict(X)

# Add the cluster assignments to the original data
iris_df = pd.DataFrame(X, columns=iris.feature_names)
iris_df['Cluster'] = clusters

# Print the first few rows of the dataframe
print(iris_df.head())

# Plot the clusters
plt.figure(figsize=(10, 7))
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', marker='o')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='x')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('K-Means Clustering of Iris Dataset')
plt.show()