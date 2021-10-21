import pandas as pd #load and manipulate data point, one-hot
import numpy as np #calculate the mean and standard deviation
import xgboost as xgb #you already know what it is
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split # split data into training and testing sets
from sklearn.metrics import balanced_accuracy_score, roc_auc_score, make_scorer #for scoring
from sklearn import GridSearchCV #cross validation
from sklearn import confusion_matrix #creates a confusion matrix
from sklearn import plot_confusion_matrix #draws a confusion matrix

df = pd.read_csv('')

df.head()
df.drop([]), axis=1, inplace=True # axis 0 rows, axis 1 columns
df[''].unique() #search for unique values and determine their usefulness as far as making predictions is concerned, remember the goal
#count, country vs city
df[''].replace('','_', regex = True, inplace = True) #xgb final product, no white spaces, regular expession
df.columns = df.columns.str.replace('','_') #also pay attention to white spaces in column names

#is there missing data?

df.dtypes #figure out what you are working with, we don't need any n/a placeholders
df[''].unique()
#are your numbers coming back as objects?
#deal with your missing data
#xgboost will determine default behavior for missing data

len(df.loc[df['']== 0] ) #what are the number of rows with missing values
df.loc[(df[''] == ''), ''] = 0 #set to 0
df[''] = pd.to_numeric(df[''])
df.types #check if your value converion applied
df.replace('', '_', regex= True, inplace= True) #just check for additional white spaces

#split data into 2 parts
#1. the columns of data that we will use to makes classifcations (X)
#2. the column of data that we want to predict. (y)

#we drop the value into a new variable and save it
X = df.drop('', axis=1).copy()
X.head() #make sure it worked

y = df[''].copy()
y.head()

#now format your variables to make it suitable for xgboost, one-hot encoding
X.dtypes
#one hot will take objects and format them into a data type xgboost can use 'categorical data'
#cannot treat categorical data like continuous data, we can't just switch them to a number. 
#if we do it will trick xgboost into treating categorical data as similar data types.
pd.get_dummies(X, columns=['what goes inone hot']).head()
#one hot is not for linear or logistic regression but it works great for trees
X_encoded = pd.get_dummies(X, columes=['any data that needs to be converted from an object value to a uses float or int'])
X_encoded.head() #print to verify
y.unique() #let's make sure y only contains 1 and 0's
#xgboost does not allocate memory for zeros, so checks to see if memory is allocated for real values

#remember xgboost model example
#Split data into training and testing sets and build the model. Remember we observed that dataset was imbalanced. We divided the number of people who left the company where y = 1,
#by the total number of people in the dataset sum(y)/len(y)
# we found that 27% of people left the company. so when we split the data into training and testing, we split using stratification in order to
#maintain the same percentage of people who lef thte company in both the training set and the testing set.
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, random_state=42, stratify=y) 
#verify
sum(y_train)/len(y_train)
sum(y_test)/len(y_test)

clf_xgb = xgb.XGBClassifier(objective='binary:logistic', missing=None, seed=42) #purpose of missing=none(default/nan)specify missing data
clf_xgb.fit(X_train,
            y_train,
            verbose=True,
            early_stopping_rounds=10,
            eval_metric='aucpr',
            eval_set=[(X_test, y_test)]


#create trees by running .fit
#early stopping, at some point the prediction will not improve and if so it will build 10 more trees and stop
# aucpr from sci kit learn
# evaluating how many trees to build usin the test data set
)


plot_confusion_matrix(clf_xgb,
                      X_test,
                      y_test,
                      values_format = 'd',
                      display_labels = ['did not leave', 'left']


)


#results trash because of imbalanced data? scale_pos_weight
#hyper paramters max_depth, learning_rate, gamma, reg_lambda


param_grid = {
    'max_depth': [3,4,5],
    'learning_rate': [0.1, 0.01, 0.05],
    'gamma': [0, 0.25, 1.0],
    'reg_lambda': [0, 1.0, 10.0],
    'scale_pos_weight': [1,3,5]

}

# start with multiple values, then optimize, based on output, second round below example:

param_grid = {
    'max_depth': [4],
    'learning_rate': [0.1, 0.5, 1],
    'gamma': [0.25],
    'reg_lambda': [10, 20, 100],
    'scale_pos_weight': [3]

}
#lets speed up our optimazation process by testing small randomized sections of data
optimal_params = GridSearchCV(
    estimator=xgb.XGBClassifier(objective='binary:logistic',
                                 seed=42,
                                 subsample=0.9,
                                 colsample_bytree=0.5),
    param_grid=param_grid,
    scoring='roc_auc', #sci kit learn evaluation
    verbose= 0,
    n_jobs= 10,
    cv = 3

)

optimal_params.fit(X_train,
            y_train,
            verbose=True,
            early_stopping_rounds=10,
            eval_metric='aucpr',
            eval_set=[(X_test, y_test)],
            verbose=False)
print(optimal_params.best_params_)

#example output values used for next model

clf_xgb = xgb.XGBClassifier(seed=42,
                        objective= 'binary:logistic',
                        gamma=0.25,
                        learn_rate=0.1,
                        max_depth=4,
                        reg_lambda= 10,
                        scale_pos_weight= 3,
                        subsample= 0.9,
                        colsample_bytree=0.5,)
#one more time
clf_xgb.fit(X_train,
            y_train,
            verbose=True,
            early_stopping_rounds=10,
            eval_metric='aucpr',
            eval_set=[(X_test, y_test)]


#create trees by running .fit
#early stopping, at some point the prediction will not improve and if so it will build 10 more trees and stop
# aucpr from sci kit learn
# evaluating how many trees to build usin the test data set
)

#and one more time to make output pretty
plot_confusion_matrix(clf_xgb,
                      X_test,
                      y_test,
                      values_format = 'd',
                      display_labels = ['did not leave', 'left']


)


#data model was used to determine people who might leave the company so company could take measures to prevent them from leaving and prevent cash loss. 

#draw actual tree for visualization
clf_xgb = xgb.XGBClassifier(seed=42,
                        objective= 'binary:logistic',
                        gamma=0.25,
                        learn_rate=0.1,
                        max_depth=4,
                        reg_lambda= 10,
                        scale_pos_weight= 3,
                        subsample= 0.9,
                        colsample_bytree=0.5,
                        n_estimators=1) #get your gain and cover

clf_xgb.fit(X_train, y_train)
#values you are looking for
#weight=number of times a feature is used in abrnch or root across all tress
#gain = the average gain across all splis that the feature is used in 
#cover = the avearage coverage across all splits is used in
#total_gain = the total gain across all splits the feature is used in 
#total_cover = the total coverage across all splits the feature is used in
#how did your model perform
bst = clf_xgb.get_gooster()
for importance_type in ('weight', 'gain', 'cover', 'total_gain', 'total_cover'):
    print('%s:' % importance_type, bst.get_score(importance_type=importance_type))
#styling your output
node_params= {'shape': 'box',
              'style': 'filled, rounded',
              'fillcolor': 'hexcode'}

leaf_params= {'shape': 'box',
              'style': 'filled, rounded',
              'fillcolor': 'hexcode'}

xgb.to_graphviz(clf_xgb, num_trees=0, size='10,10',
                condition_node_params=node_params,
                leaf_node_params=leaf_params)

#for saving: graph_data = xgb.to_graphviz.....