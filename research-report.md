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
- Patient locations: X, Y coordinates of infected individuals.

### Algorithm
- Clustering: A custom implementation of K-Means assigns patients to nearest outbreak source and iteratively updates centroids.
- Evaluation: The Silhouette Score measures clustering quality (cohesion vs. separation).
- Visualization: Clusters are plotted with distinct colors, and outbreak sources are highlighted as centroids.

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
