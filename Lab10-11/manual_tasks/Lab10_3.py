import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

#using sample data
data_3 = """spend_6mo,age,visits,purch_freq,is_high_value
5000.0,45,20,0.8,1
150.0,22,2,0.1,0
8000.0,50,25,0.9,1
200.0,25,3,0.2,0
6000.0,40,18,0.7,1
99999.0,35,50,1.0,1
300.0,28,4,0.3,0
4500.0,38,15,0.6,1
100.0,20,1,0.05,0
,30,5,0.4,0"""

df3 = pd.read_csv(StringIO(data_3))

#handle missing values
df3['spend_6mo'] = df3['spend_6mo'].fillna(df3['spend_6mo'].median())

#outliers
q_95 = df3['spend_6mo'].quantile(0.95)
df3['spend_6mo'] = np.where(df3['spend_6mo'] > q_95, q_95, df3['spend_6mo'])

X3 = df3.drop('is_high_value', axis=1)
y3 = df3['is_high_value']

#scaling
scaler = StandardScaler()
X3_scaled = scaler.fit_transform(X3)

#traintest split
X_train, X_test, y_train, y_test = train_test_split(X3_scaled, y3, test_size=0.3, random_state=42)

#svm for hyperplane classification
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)
svm_accuracy = accuracy_score(y_test, svm_model.predict(X_test))
print(f"Task 3 - SVM (Hyperplane) Accuracy: {svm_accuracy:.2f}")


# We use unscaled data for trees to keep rules interpretable
X_train_tree, X_test_tree, y_train_tree, y_test_tree = train_test_split(X3, y3, test_size=0.3, random_state=42)
tree_model = DecisionTreeClassifier(max_depth=3)
tree_model.fit(X_train_tree, y_train_tree)
tree_accuracy = accuracy_score(y_test_tree, tree_model.predict(X_test_tree))
print(f"Task 3 - Decision Tree (Rules) Accuracy: {tree_accuracy:.2f}")

#display tree rules
from sklearn.tree import export_text
tree_rules = export_text(tree_model, feature_names=list(X3.columns))
print("Task 3 - Customer Classification Rules:\n", tree_rules)