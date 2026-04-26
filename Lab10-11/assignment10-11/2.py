from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

csv_data2 = """rooms,sqm,zone,price
3,120,a,250
2,95,b,210
4,200,a,350
1,80,b,150
3,150,c,280
2,110,a,230
3,,c,260
4,180,b,320
2,90,a,200
3,140,c,270"""

df2 = pd.read_csv(StringIO(csv_data2))

df2['sqm'] = df2['sqm'].fillna(df2['sqm'].median())
df2 = pd.get_dummies(df2, columns=['zone'], drop_first=True)

x2 = df2.drop('price', axis=1)
y2 = df2['price']

scaler2 = StandardScaler()
x2_scaled = scaler2.fit_transform(x2)

x_train2, x_test2, y_train2, y_test2 = train_test_split(x2_scaled, y2, test_size=0.3, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(x_train2, y_train2)
lin_pred = lin_reg.predict(x_test2)

dt_reg = DecisionTreeRegressor(random_state=42)
dt_reg.fit(x_train2, y_train2)
dt_pred = dt_reg.predict(x_test2)

print(
	f"linear regression  mae {mean_absolute_error(y_test2, lin_pred):.3f}  "
	f"rmse {np.sqrt(mean_squared_error(y_test2, lin_pred)):.3f}"
)
print(
	f"decision tree  mae {mean_absolute_error(y_test2, dt_pred):.3f}  "
	f"rmse {np.sqrt(mean_squared_error(y_test2, dt_pred)):.3f}"
)