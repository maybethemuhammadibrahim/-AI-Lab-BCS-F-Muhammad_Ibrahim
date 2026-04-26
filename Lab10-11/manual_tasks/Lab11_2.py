import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#sample data
data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}
df = pd.DataFrame(data)

df['vehicle_type_encoded'] = pd.factorize(df['vehicle_type'])[0]
x = df[['mileage', 'fuel_efficiency', 'maintenance_cost', 'vehicle_type_encoded']]

kmeans_unscaled = KMeans(n_clusters=3, random_state=42)
df['cluster_unscaled'] = kmeans_unscaled.fit_predict(x)

scaler = StandardScaler()
x_scaled = x.copy()
cols_to_scale = ['mileage', 'fuel_efficiency', 'maintenance_cost']
x_scaled[cols_to_scale] = scaler.fit_transform(x[cols_to_scale])

kmeans_scaled = KMeans(n_clusters=3, random_state=42)
df['cluster_scaled'] = kmeans_scaled.fit_predict(x_scaled)