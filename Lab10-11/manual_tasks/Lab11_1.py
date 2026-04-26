import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from io import StringIO

csv_data = """customer_id,gender,age,annual_income,spending_score
1,1,19,15,39
2,1,21,15,81
3,0,20,16,6
4,0,23,16,77
5,0,31,17,40
6,0,22,17,76
7,0,35,18,6
8,0,23,18,94
9,1,64,19,3
10,0,30,19,72"""

df = pd.read_csv(StringIO(csv_data))
x = df.drop('customer_id', axis=1)

kmeans_unscaled = KMeans(n_clusters=3, random_state=42)
clusters_unscaled = kmeans_unscaled.fit_predict(x)

x_scaled = x.copy()
cols_to_scale = ['gender', 'annual_income', 'spending_score']
scaler = StandardScaler()
x_scaled[cols_to_scale] = scaler.fit_transform(x[cols_to_scale])

kmeans_scaled = KMeans(n_clusters=3, random_state=42)
clusters_scaled = kmeans_scaled.fit_predict(x_scaled)

result = df[['customer_id', 'gender', 'age', 'annual_income', 'spending_score']].copy()
result['cluster_unscaled'] = clusters_unscaled
result['cluster_scaled'] = clusters_scaled

print('final clustered data')
print(result)

print('\ncluster counts without scaling')
print(pd.Series(clusters_unscaled).value_counts().sort_index())

print('\ncluster counts with scaling except age')
print(pd.Series(clusters_scaled).value_counts().sort_index())

centers_unscaled = pd.DataFrame(kmeans_unscaled.cluster_centers_, columns=x.columns)

centers_scaled = pd.DataFrame(kmeans_scaled.cluster_centers_, columns=x.columns)
centers_scaled_original_units = centers_scaled.copy()
centers_scaled_original_units[cols_to_scale] = scaler.inverse_transform(centers_scaled[cols_to_scale])

print('\ncluster centers without scaling')
print(centers_unscaled)

print('\ncluster centers with scaling except age shown in original units')
print(centers_scaled_original_units)

changed_labels = (result['cluster_unscaled'] != result['cluster_scaled']).sum()
print(f'\ncustomers with different cluster label across the two runs {changed_labels} out of {len(result)}')

print('\ninsights')
print('without scaling larger numeric features influence distance more strongly')
print('with scaling except age annual income and spending score contribute more evenly with gender')
print('age is left in original scale so age still keeps relatively high influence')