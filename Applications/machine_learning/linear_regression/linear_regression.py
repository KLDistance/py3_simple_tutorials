# here is an example of a simple prediction of salary to years of working experience in CS field

import pandas as pd
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# load data set
data_set = pd.read_csv('salary_data.csv')
X = data_set.iloc[:, 0].values
Y = data_set.iloc[:, -1].values

# divide the data into training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
X_train = X_train.reshape(-1, 1)
Y_train = Y_train.reshape(-1, 1)

# use linear regression to train data
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
# predict Y in test set
predict = regressor.predict(X_train.reshape(-1, 1))

# evaluate the residual square
Y_test_predict = regressor.coef_[0, 0] * X_test + regressor.intercept_[0]
print('r2_score is ' + str(r2_score(Y_test, Y_test_predict)))

# visualize the result
plt.figure(figsize=(10,12))

# training set
figure = plt.subplot(211)
plt.scatter(X_train, Y_train, color='red')
# predict linear model (function)
plt.plot(X_train, predict, color='black')
plt.xlabel('Years Experience')
plt.ylabel('Salary')
plt.title('Training Set')

# test set
plt.subplot(212)
plt.scatter(X_test, Y_test, color='red')
plt.plot(X_train, predict, color='black')
plt.xlabel('Years Experience')
plt.ylabel('Salary')
plt.title('Test Set')
plt.show()