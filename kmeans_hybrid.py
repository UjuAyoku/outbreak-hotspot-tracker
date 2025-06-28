import numpy as np
import random

def load_kmeans_input(filename):
    with open(filename, 'r') as f:
        max_iters = int(f.readline())
        num_points = int(f.readline())
        k = int(f.readline())
        initial_indices = [int(f.readline()) for _ in range(k)]
        points = [list(map(int, line.strip().split(','))) for line in f.readlines()]
    return max_iters, k, initial_indices, np.array(points)

def kmeans_plus_plus(points, k):
    centroids = [points[random.randint(0, len(points) - 1)]]
    for _ in range(1, k):
        distances = np.array([
            min(np.linalg.norm(p - c)**2 for c in centroids) for p in points
        ])
        probabilities = distances / distances.sum()
        cumulative_probs = np.cumsum(probabilities)
        r = random.random()
        for i, p in enumerate(cumulative_probs):
            if r < p:
                centroids.append(points[i])
                break
    return np.array(centroids)

def hybrid_init(points, given_indices, k, use_kpp=False):
    if use_kpp:
        return kmeans_plus_plus(points, k)
    else:
        return np.array([points[i] for i in given_indices])

def assign_clusters(points, centroids):
    distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

def update_centroids(points, labels, k):
    return np.array([
        points[labels == i].mean(axis=0) if np.any(labels == i) else [0, 0]
        for i in range(k)
    ])

def has_converged(old, new, tol=1e-4):
    return np.all(np.linalg.norm(old - new, axis=1) < tol)

def run_kmeans(points, k, initial_indices, max_iters, use_kpp=False):
    centroids = hybrid_init(points, initial_indices, k, use_kpp)
    initial_centroids = centroids.copy()
    for iteration in range(max_iters):
        labels = assign_clusters(points, centroids)
        new_centroids = update_centroids(points, labels, k)
        if has_converged(centroids, new_centroids):
            break
        centroids = new_centroids
    clusters = [points[labels == i].tolist() for i in range(k)]
    return initial_centroids.tolist(), centroids.tolist(), clusters, iteration + 1, labels
