# 🦠 Clustering of COVID-19 Patient Locations using K-Means

## Project Description
This project applies the K-Means clustering algorithm to group COVID-19 patient location data based on spatial proximity. Using the known coordinates of infected individuals, the natural groupings or clusters that could represent localized outbreak zones or transmission paths were identified.

The algorithm is implemented from scratch in Python using vectorized operations with NumPy, enhanced by k-means++ initialization for better accuracy and convergence, and visualized using matplotlib. The clustering quality is also evaluated using the Silhouette Score from scikit-learn.

This project demonstrates the power of unsupervised machine learning in deriving insight from unlabeled, real-world data.

## Problem Statement:
During the outbreak of viruses such as COVID-19, understanding how infections spread spatially is critical. Given only the coordinates of infected individuals—including a few known index cases (initially infected)—can we:

- Group other patients based on proximity to these initial cases?

- Identify which geographic regions are likely hotspots or cluster zones?

## Key Concepts and Technologies:
| Concept / Tool         | Purpose                                  |
| ---------------------- | ---------------------------------------- |
| **K-Means Clustering** | Group unlabeled data based on similarity |
| **k-means++ Init**     | Improve centroid selection               |
| **NumPy**              | Fast numeric operations                  |
| **Matplotlib**         | Cluster visualization                    |
| **Silhouette Score**   | Evaluate clustering quality              |
| **Python**             | Implementation and control logic         |

## Applications
K-means++ is widely used in various applications, including:
- Image segmentation: Segmenting images based on color or texture features.
- Customer segmentation: Grouping customers based on purchasing habits or demographic data.
- Anomaly detection: Identifying outliers in datasets.
- Document clustering: Grouping similar documents based on content.
- Recommender systems: Recommending products or services based on user preferences


## Input Format (kmeans.txt):
50              # Max number of iterations

100             # Number of total patients

4               # Number of clusters (initial infections)

12              # Index of centroid 1

23              # Index of centroid 2

50              # Index of centroid 3

67              # Index of centroid 4

83,13           # Patient 1 (x, y)

...

81,32           # Patient 100

## Outputs:
- Initial and final centroid coordinates

- Number of patients in each cluster

- Iterations to convergence

- Cluster visual plot

- Silhouette Score (clustering performance metric)


## Extensions:
- Incorporate time-stamped location data to track spread over time

- Use density-based clustering (e.g. DBSCAN) for comparison

- Deploy the model as an interactive web app


## How to Run

📥 Clone the repo:
   ```bash
   git clone https://github.com/UjuAyoku/kmeans-clustering.git
   cd kmeans-clustering
