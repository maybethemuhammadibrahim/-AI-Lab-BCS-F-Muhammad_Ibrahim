import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from io import StringIO

csv_data = """student_id,gpa,study_hours,attendance_rate
1,3.5,15,90
2,2.0,5,60
3,3.8,20,95
4,2.5,8,70
5,3.9,25,98
6,2.1,6,65
7,3.2,12,85
8,2.8,10,75
9,3.7,18,92
10,2.4,7,62"""

df = pd.read_csv(StringIO(csv_data))
x = df[['gpa', 'study_hours', 'attendance_rate']]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

wcss = []
for i in range(2, 7):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(x_scaled)
    wcss.append(kmeans.inertia_)

kmeans_final = KMeans(n_clusters=2, random_state=42)
df['cluster'] = kmeans_final.fit_predict(x_scaled)

print(df[['student_id', 'cluster']])

plt.scatter(df['study_hours'], df['gpa'], c=df['cluster'])
plt.title('student clusters')
plt.xlabel('study hours')
plt.ylabel('gpa')
plt.show()