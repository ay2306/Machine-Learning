import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
def mae(max_leaves,train_X,val_X,train_y,val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaves,random_state=0)
    model.fit(train_X,train_y)
    pred_x = model.predict(val_X)
    return mean_absolute_error(pred_x,val_y)

data = pd.read_csv('./test1.csv')
# Handling NaN values
my_imputer = SimpleImputer()
data = my_imputer.fit_transform(data)
# print (data.columns)
y = data.median_house_value
features = ['total_rooms','population','median_income']
X = data[features]
train_X, val_X, train_y, val_y = train_test_split(X,y)

model = DecisionTreeRegressor()
model.fit(train_X,train_y)
pred_x = model.predict(val_X)
mae = mean_absolute_error(val_y,pred_x)
print(mae)

# leaf_options = [5,10,15,25,50,100,250,500]
# for number_of_leaves in leaf_options:
#     print ("ACCURACY at " + str(number_of_leaves) + " = " + str(mae(number_of_leaves,train_X,val_X,train_y,val_y)))

# ACCURACY at 5 = 62094.31174448778
# ACCURACY at 10 = 60379.75834502197
# ACCURACY at 15 = 59673.20012625267
# ACCURACY at 25 = 59745.01759513017
# ACCURACY at 50 = 59769.203847948265
# ACCURACY at 100 = 60795.030603810315
# ACCURACY at 250 = 62297.00446678799
# ACCURACY at 500 = 65100.51665308253

# model = RandomForestRegressor(random_state=1)
# model.fit(train_X,train_y)
# model.fit(X,y)
# pred_x = model.predict(val_X)
# print(mean_absolute_error(val_y,pred_x))
# ACCURACY = 61283.53556547619



