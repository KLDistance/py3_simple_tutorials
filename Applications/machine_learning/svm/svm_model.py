# advantages of support vector machines:
## Effective in high dimensional spaces
## Cases where number of dimensions is greate than the number of samples
## Memory efficient to use subset of training points in the decision function (support vector)
## Versatile for different types of kernel functions

# disadvantages of SVM:
## Over-fitting is possible if kernel functions are awful
## Do not directly support probability estimates

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# data loader
cancer = pd.read_csv('breast_cancer_data.csv')
X = cancer.drop(['diagnosis'], axis=1)
Y = cancer['diagnosis']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=20)

# loader info out
print('The size of our training X (input features) is ', X_train.shape, '\n')
print('The size of our testing X (input features) is ', X_test.shape, '\n')
print('The size of our training Y (output features) is ', Y_train.shape, '\n')
print('The size of our training Y (output features) is ', Y_test.shape, '\n')

# first to normalize training data to optimize the expectation
X_train_min = X_train.min()
X_train_max = X_train.max()
X_train_range = X_train_max - X_train_min
X_train_scaled = (X_train - X_train_min) / X_train_range

# training SVM model
svc_model = SVC()
svc_model.fit(X_train_scaled, Y_train)

# normalize testing data
X_test_min = X_test.min()
X_test_range = (X_test - X_test_min).max()
X_test_scaled = (X_test - X_test_min) / X_test_range

# model prediction
Y_predict = svc_model.predict(X_test_scaled)

# to evaluate the accuracy, use confusion matrix
cm = confusion_matrix(Y_test, Y_predict, labels=[1, 0])
confusion = pd.DataFrame(cm, index=['is cancer', 'is healthy'], columns=['predicted cancer', 'predicted healthy'])
sns.heatmap(confusion, annot=True, fmt='d')
plt.show()

# classification report
print(classification_report(Y_test, Y_predict))