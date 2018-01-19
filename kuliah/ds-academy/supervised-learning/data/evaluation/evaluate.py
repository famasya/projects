import pandas as pd
data       = pd.read_csv('data1.csv')
actual     = data['Actual']
prediction = data['Prediction']


#1. Ratio
sum(1 for x in actual if x == 0)
# 49
sum(1 for x in actual if x == 1)
# 51
# 49:51


#2. Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(actual, prediction)
#array([[35, 14],
#       [ 9, 42]])


#3. Accuracy
from sklearn.metrics import accuracy_score
accuracy_score(actual, prediction)
#  0.77000000000000002


#4. Precision
from sklearn.metrics import precision_score
precision_score(actual, prediction)
# 0.75


#5. Recall
from sklearn.metrics import recall_score
recall_score(actual, prediction)
# 0.82352941176470584


