import numpy as np
import random

def kmeans_plus_plus_init(points, k):
    centroids = [points[random.randint(0, len(points) - 1)]]
    for _ in range(1, k):
        distances = np.array([
            min(np.linalg.norm(p - c)**2 for c in centroids) for p in points
        ])
        probabilities = distances / distances.sum()
        cumulative_probs = np.cumsum(probabilities)
        r = random.random()
        for j, p in enumerate(cumulative_probs):
            if r < p:
                centroids.append(points[j])
                break
    return np.array(centroids)

def assign_clusters(points, centroids):
    distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

def compute_new_centroids(points, labels, k):
    return np.array([points[labels == i].mean(axis=0) if np.any(labels == i) else [0, 0] for i in range(k)])

def has_converged(old_centroids, new_centroids, tol=1e-4):
    return np.all(np.linalg.norm(old_centroids - new_centroids, axis=1) < tol)

def kmeans(points, k, max_iters):
    centroids = kmeans_plus_plus_init(points, k)
    initial_centroids = centroids.copy()
    for iteration in range(max_iters):
        labels = assign_clusters(points, centroids)
        new_centroids = compute_new_centroids(points, labels, k)
        if has_converged(centroids, new_centroids):
            break
        centroids = new_centroids
    clusters = [points[labels == i].tolist() for i in range(k)]
    return initial_centroids.tolist(), centroids.tolist(), clusters, iteration + 1
