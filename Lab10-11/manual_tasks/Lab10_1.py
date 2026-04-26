import pandas as pd
from io import StringIO
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#load data for task 1
data_1 = """sq_meters,bedrooms,bathrooms,age,neighborhood,price
120.5,3,2,15,suburb,250000
95.0,2,1,5,urban,210000
200.0,4,3,20,suburb,350000
80.5,1,1,2,urban,150000
150.0,3,2,10,rural,280000
110.0,2,2,8,suburb,230000
,3,2,12,rural,260000
180.0,4,3,25,urban,320000
90.0,2,1,3,suburb,200000
140.0,3,2,7,rural,270000"""

df1 = pd.read_csv(StringIO(data_1))

#clean data
df1['sq_meters'] = df1['sq_meters'].fillna(df1['sq_meters'].median())

#encodecategorical variable
df1 = pd.get_dummies(df1, columns=['neighborhood'], drop_first=True)

#identify features and target
X1 = df1.drop('price', axis=1)
y1 = df1['price']

#train mdoel
model1 = LinearRegression()
model1.fit(X1, y1)

#evaluate model
predictions1 = model1.predict(X1)
mae = mean_absolute_error(y1, predictions1)
print(f"Task 1 - Mean Absolute Error: {mae:.2f}")

#predict price for new house
new_house = pd.DataFrame({'sq_meters': [130.0], 'bedrooms': [3], 'bathrooms': [2], 'age': [10], 'neighborhood_suburb': [1], 'neighborhood_urban': [0]})

new_house = new_house.reindex(columns=X1.columns, fill_value=0)
predicted_price = model1.predict(new_house)[0]
print(f"Task 1 - Predicted Price for new house: ${predicted_price:.2f}")