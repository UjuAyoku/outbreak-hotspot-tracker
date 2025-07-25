## Patient Location Clustering for Disease Outbreak Analysis

### Project Description
This tool groups COVID-19 patient locations to identify potential outbreak hotspots. By analyzing where infected people are located, it helps pinpoint high-risk areas and is useful for healthcare planning and resource allocation.

### Why This Matters:
During outbreaks (such as COVID-19 or the recent measles outbreak in North America), knowing where infections are concentrated helps:

- Hospitals prepare for surges.
- Officials implement targeted lockdowns/testing.
- Researchers study spread patterns.

Therefore, given only the coordinates of infected individuals, including 4 known initially infected patients, can:
- Patients be grouped based on proximity to these initial cases?
- Hotspots be identified?

Note: This is a simplified model—it does not account for travel history nor method (car, plane, train etc.), temporal progression (when they got infected), infection chains or contact tracing, or individual behavior (mobility, superspreaders) due to data limitation.

### Key Concepts and Technologies Used:
| Tech Used              | Purpose                                  |
| ---------------------- | ---------------------------------------- |
| **K-Means Clustering (Custom Python)** | Find patient clusters                    |
| **Matplotlib**         | Visualize clusters                            |
| **Silhouette Score**   | Evaluate clustering quality              |


### Input Data Format:
The tool needs a text file (kmeans.txt) with: 
1. Settings: Max iterations, # of patients, # of clusters (number of known initial infections).
2. Initial Outbreak Sources: Pre-defined "centers" (e.g., first known cases).
3. Patient Locations: X,Y coordinates (e.g., 83,13 = patient at x=83, y=13).

50   # Stop after 50 steps  
100  # 100 patients  
4    # 4 outbreak sources  
12   # 1st source: Patient #12  
...  
83,13 # Patient 1’s location  
81,32 # Patient 2’s location  

### Sample Output
1. Cluster Map:

- 🟢 🔵 🟣 🔴 = Patient Clusters  
- ❌ Markers = outbreak sources (centroids).
2. Stats
  - Initial and final centroid coordinates
  - Patients per cluster
  - How long the analysis took
  - Silhouette Score (Quality check)


### Other Uses
Adaptations of this solution can be used in various applications such as:
- Customer segmentation: Grouping customers based on purchasing habits or location.
- Image segmentation: Segmenting images based on color or texture features.
- Anomaly detection: Identifying outliers in datasets.
- Document clustering: Grouping similar documents based on content.
- Recommender systems: Recommending products or services based on user preferences


### How to Run

📥 Clone the repo:
   ```bash
   git clone https://github.com/UjuAyoku/kmeans-clustering.git
   cd kmeans-clustering

### Future Improvements:
- Add time-based location data to track spread over time
- Compare with other clustering methods (e.g. DBSCAN)  
- Build a user-friendly web app.
