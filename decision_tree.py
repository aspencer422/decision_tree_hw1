#-------------------------------------------------------------------------
# AUTHOR: Anthony Spencer
# FILENAME: decision_tree.py
# SPECIFICATION: program that reads in a specific .csv file and create a decision tree
# FOR: CS 4200- Assignment #1
# TIME SPENT: this qeustion 20 mins
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =
for i in range(len(db)):
    column = []
    for j in range(4):
      if db[i][j] == 'Young' or db[i][j] == 'Myope' or db[i][j] == 'No' or db[i][j] == 'Reduced':
        column.append(1)
      elif db[i][j] == 'Prepresbyopic' or db[i][j] == 'Hypermetrope' or db[i][j] == 'Yes' or db[i][j] == 'Normal':
        column.append(2)
      elif db[i][j] =='Presbyopic':
        column.append(3)
    X.append(column)
#used for testing 
#print(X)
#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =
for i in range(len(db)):
  if db[i][4] == 'No':
    Y.append(2)
  else:
    Y.append(1)
#used for testing 
#print(Y)
#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()