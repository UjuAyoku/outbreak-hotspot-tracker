from kmeans_hybrid import load_kmeans_input, run_kmeans
from visualize_clusters import plot_clusters
from sklearn.metrics import silhouette_score

def main():
    filename = 'kmeans.txt'
    use_kmeans_plus_plus = False  # 🔁 Set to True to use k-means++

    max_iters, k, initial_indices, all_points = load_kmeans_input(filename)

    initial_c, final_c, clusters, total_iters, labels = run_kmeans(
        all_points, k, initial_indices, max_iters, use_kpp=use_kmeans_plus_plus
    )

    print(f"{'k-means++' if use_kmeans_plus_plus else 'File-based'} initialization\n")
    print(f"Initial Centroids: {initial_c}\n")
    print(f"Iterations to achieve stability: {total_iters}\n")
    print("Final Centroids:")
    for c in final_c:
        print([round(x, 2) for x in c])
    print()
    for i, cluster in enumerate(clusters):
        print(f"Number of patients in cluster {i}: {len(cluster)}\n{cluster}\n")

    # Evaluate clustering performance
    if len(set(labels)) > 1:
        sil_score = silhouette_score(all_points, labels)
        print(f"Silhouette Score: {sil_score:.4f}")
    else:
        print("Silhouette Score: Not computable (only one cluster assigned)")

    # Optional visualization
    plot_clusters(all_points, final_c, clusters)

if __name__ == '__main__':
    main()
