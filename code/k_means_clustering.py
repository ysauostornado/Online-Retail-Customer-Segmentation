from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt

# Load RFM data
rfm = pd.read_csv('data/rfm_results.csv')

# Prepare data for clustering
rfm_data = rfm[['Recency', 'Frequency', 'Monetary']].copy()
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_data)

# Apply K-Means
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Save cluster assignments
rfm.to_csv('data/rfm_clusters.csv')

# Visualize Clusters
plt.scatter(rfm['Frequency'], rfm['Monetary'], c=rfm['Cluster'])
plt.xlabel('Frequency')
plt.ylabel('Monetary Value')
plt.title('Customer Clusters')
plt.show()
