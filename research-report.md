## Introduction
Understanding how infectious diseases spread in a population is a core challenge in epidemiology. During outbreaks, early identification of geographical hotspots can enable hospitals to prepare for surges, public health officials to allocate resources, and policymakers to implement targeted interventions.

This work explores whether unsupervised clustering algorithms, specifically K-Means, can be used to group COVID-19 patient locations and identify outbreak clusters using only spatial coordinate data.

## Problem Statement

Given only the coordinates of infected individuals and a small set of known initial outbreak sources (index patients), can clustering:
1. Group patients based on proximity to the outbreak sources?
2. Identify high-density areas representing potential hotspots?
3. Provide meaningful insights despite data limitations (e.g., absence of temporal or mobility information)?

## Related Work
Clustering methods such as K-Means and DBSCAN have been widely applied in epidemiology, ecology, and geospatial analysis. They provide a scalable way to identify latent groupings without supervision. While more complex models incorporate time, mobility, or network effects, spatial-only clustering can still provide early signals of outbreak concentration.

## Methodology
### Dataset
The input dataset consists of:
- Number of patients: Total infected individuals.
- Number of clusters: Defined by number of known outbreak sources.
- Initial outbreak sources: Index cases treated as initial centroids.
- Patient locations: ($x_i, y_i$) coordinates of infected individuals.

### Algorithm

K-Means seeks to minimize the within-cluster variance (inertia), formalized by the following objective function:

![J = \sum_{k=1}^{K} \sum_{x_i \in C_k} \| x_i - \mu_k \|^2](https://latex.codecogs.com/svg.latex?J%20%3D%20%5Csum_%7Bk%3D1%7D%5E%7BK%7D%20%5Csum_%7Bx_i%20%5Cin%20C_k%7D%20%5C%7C%20x_i%20-%20%5Cmu_k%20%5C%7C%5E2)

**Where:**
*   $ K $ = number of clusters (outbreak sources)
*   $ x_i $ = coordinate of the \( i \)-th patient
*   $ \mu_k $ = centroid of cluster $ C_k $

The algorithm iteratively:
1.  **Assigns** each patient to the nearest centroid (based on Euclidean distance).
2.  **Updates** centroid positions to be the mean of all points assigned to that cluster.
3.  **Stops** when centroid assignments stabilize (convergence) or the maximum number of iterations is reached.

### Evaluation Metric

Cluster quality is evaluated using the **Silhouette Score**. The score for a single sample \( i \) is calculated as:

![s(i) = \frac{b(i) - a(i)}{\max\{a(i), b(i)\}}](https://latex.codecogs.com/svg.latex?s%28i%29%20%3D%20%5Cfrac%7Bb%28i%29%20-%20a%28i%29%7D%7B%5Cmax%5C%7Ba%28i%29%2C%20b%28i%29%5C%7D%7D)

**Where:**
*   \( a(i) \) = mean intra-cluster distance (average distance between sample \( i \) and all other points in the same cluster).
*   \( b(i) \) = mean nearest-cluster distance (average distance between sample \( i \) and all points in the *next nearest* cluster).

The overall Silhouette Score for a dataset is the mean of \( s(i) \) over all samples.
*   **Scores close to +1** indicate well-separated and dense clusters.
*   **Scores around 0** indicate overlapping clusters.
*   **Scores close to -1** suggest that samples may have been assigned to the wrong cluster.

### Tools
- Python (NumPy, scikit-learn)
- Matplotlib for visualization

## Results
- Cluster Maps: Distinct patient clusters emerge around outbreak sources.
- Centroid Stability: Centroids converge after multiple iterations, indicating stable groupings.
- Silhouette Score: Provides a quantitative check of cluster quality.
- Performance: Algorithm runtime remains efficient even for 100+ patients.

Example Output:
- Number of patients per cluster
- Initial vs. final centroid positions
- Execution time

## Discussion

The results suggest that even with limited data (spatial coordinates only), clustering can highlight potential outbreak hotspots. However, several limitations remain:
- No temporal modeling: Cannot track spread over time.
- No mobility data: Travel history and superspreading events are not captured.
- Fixed cluster number: Requires known outbreak sources, unlike density-based clustering (e.g., DBSCAN).

Despite these limitations, this approach demonstrates the feasibility of lightweight clustering methods for outbreak monitoring, especially in resource-limited settings where detailed epidemiological data is unavailable.


## Future Work
- Extend dataset to include time-series infection data to analyze outbreak dynamics.
- Compare K-Means with DBSCAN and hierarchical clustering for robustness.
- Build a user-friendly web app for real-time visualization of patient clustering.
- Integrate external datasets (mobility, demographics) to refine hotspot detection.

## Applications Beyond Epidemiology
- Customer segmentation in marketing
- Image segmentation in computer vision
- Anomaly detection in cybersecurity
- Recommender systems for personalization

## Conclusion
This project demonstrates how a fundamental clustering method (K-Means) can be adapted for outbreak hotspot detection. While simplified, the study provides a starting point for applying machine learning to real-world epidemiological challenges. With further extensions, such approaches can become valuable tools for public health decision-making.
