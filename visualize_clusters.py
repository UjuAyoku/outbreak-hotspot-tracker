import matplotlib.pyplot as plt
import numpy as np

def plot_clusters(points, centroids, clusters):
    colors = ['red', 'green', 'blue', 'purple', 'orange', 'cyan', 'brown']
    points = np.array(points)
    centroids = np.array(centroids)

    plt.figure(figsize=(8, 6))

    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        plt.scatter(cluster[:, 0], cluster[:, 1], s=30, color=colors[i % len(colors)], label=f'Cluster {i}')
        plt.scatter(centroids[i][0], centroids[i][1], s=200, color=colors[i % len(colors)], marker='X', edgecolors='k')

    plt.title("K-Means Clustering Results")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
