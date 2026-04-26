from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

csv_data3 = """income,spending,age
50,30,25
100,80,35
150,10,45
40,40,22
120,90,30
160,5,50
60,20,28
110,75,32
140,15,40
,50,29"""

df3 = pd.read_csv(StringIO(csv_data3))

df3['income'] = df3['income'].fillna(df3['income'].median())

scaler3 = StandardScaler()
x3_scaled = scaler3.fit_transform(df3)

wcss = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(x3_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(2, 11), wcss)
plt.show()

kmeans_best = KMeans(n_clusters=3, random_state=42)
df3['cluster'] = kmeans_best.fit_predict(x3_scaled)

plt.scatter(df3['income'], df3['spending'], c=df3['cluster'])
plt.show()

print('assigned cluster for each row')
print(df3['cluster'])