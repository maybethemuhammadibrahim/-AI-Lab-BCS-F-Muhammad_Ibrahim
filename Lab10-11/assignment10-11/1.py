import pandas as pd
from io import StringIO
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

csv_data = """v1,v2,amount,class
0.1,-0.2,10,0
-0.5,0.8,20,0
-2.0,-3.5,100,1
1.5,0.2,12,0
0.8,-0.1,8,0
-0.2,0.5,15,0
-1.5,-2.0,80,1
0.5,0.5,25,0
1.0,-0.5,30,0
0.2,0.1,5,0"""

df = pd.read_csv(StringIO(csv_data))

df_majority = df[df['class'] == 0]
df_minority = df[df['class'] == 1]
df_minority_upsampled = resample(df_minority, replace=True, n_samples=8, random_state=42)
df_upsampled = pd.concat([df_majority, df_minority_upsampled])

x = df_upsampled.drop('class', axis=1)
y = df_upsampled['class']

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.3, random_state=42)

lr_model = LogisticRegression()
lr_model.fit(x_train, y_train)
lr_pred = lr_model.predict(x_test)

rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(x_train, y_train)
rf_pred = rf_model.predict(x_test)

print(
	f"logistic regression  accuracy {accuracy_score(y_test, lr_pred):.3f}  "
	f"precision {precision_score(y_test, lr_pred):.3f}  "
	f"recall {recall_score(y_test, lr_pred):.3f}  "
	f"f1 {f1_score(y_test, lr_pred):.3f}"
)
print(
	f"random forest  accuracy {accuracy_score(y_test, rf_pred):.3f}  "
	f"precision {precision_score(y_test, rf_pred):.3f}  "
	f"recall {recall_score(y_test, rf_pred):.3f}  "
	f"f1 {f1_score(y_test, rf_pred):.3f}"
)