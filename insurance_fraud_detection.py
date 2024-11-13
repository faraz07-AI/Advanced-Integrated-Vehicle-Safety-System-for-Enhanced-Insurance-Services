# -*- coding: utf-8 -*-
"""Insurance_fraud_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s-LYiO_Ey0ZRQsg5ByAn62ytdlytsPtW
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

df=pd.read_csv("/content/insurance_claims.csv")

df.info()

from google.colab import drive
drive.mount('/content/drive')

df.head()

df["policy_state"].unique()

df["insured_sex"].unique()

df["incident_location"].unique()

df["police_report_available"].unique()

df["fraud_reported"].unique()

df.dropna()
df

def filter_police_report(categeory,thres1,thres2):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=1 
         if categeory[i]==thres2 or categeory[i]=="?":
            categeory[i]=0         
     return categeory

df["police_report_available"].unique()

dff=df["fraud_reported"]
dff

thres1='Y'
thres2='N'
so1=filter_police_report(dff,thres1,thres2)
df["fraud_reported"]=so1
df

type(dff[0])

dd=df["police_report_available"]
dd

thres1='YES'
thres2='NO'
so=filter_police_report(dd,thres1,thres2)
df["police_report_available"]=so
df



thres1='YES'
thres2='NO'
so=filter_police_report(dd,thres1,thres2)
df["police_report_available"]=so
df

df.describe()

df.drop('_c39', axis=1, inplace=True)

db=df["insured_sex"]

def filter_police_reportk(categeory,thres1,thres2):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=1 
         if categeory[i]==thres2:
            categeory[i]=0         
     return categeory

thres1='MALE'
thres2='FEMALE'
sool=filter_police_reportk(db,thres1,thres2)
df["insured_sex"]=sool
def filter_police_reporttt(categeory,thres1,thres2,thres3):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0 
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3:
            categeory[i]=2           
     return categeory

dbb=df["policy_state"]
thres1="OH"
thres2="IN"
thres3="IL"
s1=filter_police_reporttt(dbb,thres1,thres2,thres3)
df["policy_state"]=s1
sns.set(style="white")

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(15, 15))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

sns.heatmap(df.corr(),cmap=cmap,vmax=.3,center=0,annot=True,square=True, linewidths=.5, cbar_kws={"shrink": .5})

df["insured_education_level"].unique()

def insured_education_level(categeory,thres1,thres2,thres3,thres4,thres5,thres6,thres7):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3:
            categeory[i]=2
         if categeory[i]==thres4:
            categeory[i]=3
         if categeory[i]==thres5:
            categeory[i]=5
         if categeory[i]==thres6:
            categeory[i]=6
         if categeory[i]==thres7:
            categeory[i]=7                        
     return categeory

diel=df["insured_education_level"]
print(diel)

thres1="MD"
thres2="PhD"
thres3="Associate"
thres4="Masters"
thres5="High School"
thres6="College"
thres7="JD"
iel=insured_education_level(diel,thres1,thres2,thres3,thres4,thres5,thres6,thres7)
df["insured_education_level"]=iel
df["policy_csl"].unique()

def policy_csl(categeory,thres1,thres2,thres3):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=5
         if categeory[i]==thres2:
            categeory[i]=3
         if categeory[i]==thres3:
            categeory[i]=5                     
     return categeory

dpcsl=df["policy_csl"]
print(dpcsl)

thres1="250/500"
thres2="100/300"
thres3="500/1000"
csl=policy_csl(dpcsl,thres1,thres2,thres3)
df["policy_csl"]=csl
df["incident_type"].unique()

def incident_type_filter(categeory,thres1,thres2,thres3,thres4):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3:
            categeory[i]=2
         if categeory[i]==thres4:
            categeory[i]=3                
     return categeory

dit=df["incident_type"]
thres1="Single Vehicle Collision"
thres2="Vehicle Theft"
thres3="Multi-vehicle Collision"
thres4="Parked Car"
it=incident_type_filter(dit,thres1,thres2,thres3,thres4)
df["incident_type"]=it
df["incident_state"].unique()

def incident_state_filter(categeory,thres1,thres2,thres3,thres4,thres5,thres6,thres7):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3:
            categeory[i]=2
         if categeory[i]==thres4:
            categeory[i]=3 
         if categeory[i]==thres5:
            categeory[i]=4
         if categeory[i]==thres6:
            categeory[i]=5 
         if categeory[i]==thres7:
            categeory[i]=6          
     return categeory

iss=df["incident_state"]
thres1="SC"
thres2="VA"
thres3="NY"
thres4="OH"
thres5="WV"
thres6="NC"
thres7='PA'
itt=incident_state_filter(iss,thres1,thres2,thres3,thres4,thres5,thres6,thres7)
df["incident_state"]=itt
df["insured_relationship"].unique()

def insured_relationship_filter(categeory,thres1,thres2,thres3,thres4,thres5,thres6):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3:
            categeory[i]=2
         if categeory[i]==thres4:
            categeory[i]=3 
         if categeory[i]==thres5:
            categeory[i]=4
         if categeory[i]==thres6:
            categeory[i]=5          
     return categeory

irff=df["insured_relationship"]
thres1="husband"
thres2="other-relative"
thres3="own-child"
thres4="unmarried"
thres5="wife"
thres6="not-in-family"
itrf=insured_relationship_filter(irff,thres1,thres2,thres3,thres4,thres5,thres6)
df["insured_relationship"]=itrf
df["incident_severity"].unique()

def incident_severity_filter(categeory,thres1,thres2,thres3,thres4):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3:
            categeory[i]=2
         if categeory[i]==thres4:
            categeory[i]=3                
     return categeory

disf=df["incident_severity"]
thres2="Major Damage"
thres1="Minor Damage"
thres4="Total Loss"
thres3="Trivial Damage"
isf=incident_severity_filter(disf,thres1,thres2,thres3,thres4)
df["incident_severity"]=isf
df["collision_type"].unique()

def collision_type_filter(categeory,thres1,thres2,thres3):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3 or categeory[i]=="?":
            categeory[i]=2               
     return categeory

dct=df["collision_type"]
thres3="Front Collision"
thres2="Rear Collision"
thres1="Side Collision"
ct=collision_type_filter(dct,thres1,thres2,thres3)
df["collision_type"]=ct
df["incident_city"].unique()

def incident_city_filter(categeory,thres1,thres2,thres3,thres4,thres5,thres6,thres7):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3:
            categeory[i]=2
         if categeory[i]==thres4:
            categeory[i]=3
         if categeory[i]==thres5:
            categeory[i]=5
         if categeory[i]==thres6:
            categeory[i]=6
         if categeory[i]==thres7:
            categeory[i]=7                        
     return categeory

icc=df["incident_city"]
thres1="Columbus"
thres2="Riverwood"
thres3="Arlington"
thres4="Springfield"
thres5="Hillsdale"
thres6="Northbend"
thres7="Northbrook"
icf=incident_city_filter(icc,thres1,thres2,thres3,thres4,thres5,thres6,thres7)
df["incident_city"]=icf
df["authorities_contacted"].unique()
def authorities_contacted_filter(categeory,thres1,thres2,thres3,thres4,thres5):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3:
            categeory[i]=2
         if categeory[i]==thres4:
            categeory[i]=3
         if categeory[i]==thres5:
            categeory[i]=3   
     return categeory

ac=df["authorities_contacted"]
thres1="Police"
thres2="Fire"
thres3="Ambulance"
thres4="None"
thres5="Other"
iacf=authorities_contacted_filter(icc,thres1,thres2,thres3,thres4,thres5)
df["authorities_contacted"]=iacf
df["property_damage"].unique()
pd=df["property_damage"]
thres1='YES'
thres2='NO'
dpd=filter_police_report(pd,thres1,thres2)
df["property_damage"]=dpd



df["auto_make"].unique()

def authorities_contacted_filter(categeory,thres1,thres2,thres3,thres4,thres5,thres6,thres7,thres8,thres9,thres10,thres11,thres12,thres13,thres14):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3:
            categeory[i]=2
         if categeory[i]==thres4:
            categeory[i]=3
         if categeory[i]==thres5:
            categeory[i]=4
         if categeory[i]==thres6:
            categeory[i]=5
         if categeory[i]==thres7:
            categeory[i]=6
         if categeory[i]==thres8:
            categeory[i]=7
         if categeory[i]==thres9:
            categeory[i]=8
         if categeory[i]==thres10:
            categeory[i]=9
         if categeory[i]==thres11:
            categeory[i]=10
         if categeory[i]==thres12:
            categeory[i]=11
         if categeory[i]==thres13:
            categeory[i]=12
         if categeory[i]==thres14:
            categeory[i]=13     
                     
     return categeory

am=df["auto_make"]
thres1="Saab"
thres2="Mercedes"
thres3="Dodge"
thres4="Chevrolet"
thres5="Accura"
thres6="Nissan"
thres7="Audi"
thres8="Toyota"
thres9="Ford"
thres10="Suburu"
thres11="BMW"
thres12="Jeep"
thres13="Honda"
thres14="Volkswagen"
iacf=authorities_contacted_filter(icc,thres1,thres2,thres3,thres4,thres5,thres6,thres7,thres8,thres9,thres10,thres11,thres12,thres13,thres14)
df["auto_make"]=iacf
df["auto_model"].unique()

df.drop('auto_model', axis=1, inplace=True)


df.drop('incident_location', axis=1, inplace=True)


df["insured_occupation"].unique()

dffff=df["insured_occupation"]

thres1="craft-repair"
thres2="machine-op-inspct"
thres3="sales"
thres4="armed-forces"
thres5="tech-support"
thres6="prof-specialty"
thres7="other-service"
thres8="priv-house-serv"
thres9="exec-managerial"
thres10="protective-serv"
thres11="transport-moving"
thres12="handlers-cleaners"
thres13="adm-clerical"
thres14="farming-fishing"
iacff=authorities_contacted_filter(icc,thres1,thres2,thres3,thres4,thres5,thres6,thres7,thres8,thres9,thres10,thres11,thres12,thres13,thres14)
df["insured_occupation"]=iacff


def insured_hobbies_filter(categeory,thres1,thres2,thres3,thres4,thres5,thres6,thres7,thres8,thres9,thres10,thres11,thres12,thres13,thres14,thres15,thres16,thres17,thres18,thres19,thres20):
     for i in range(len(categeory)):
         if categeory[i]==thres1:  
            categeory[i]=0
         if categeory[i]==thres2:
            categeory[i]=1
         if categeory[i]==thres3:
            categeory[i]=2
         if categeory[i]==thres4:
            categeory[i]=3
         if categeory[i]==thres5:
            categeory[i]=4
         if categeory[i]==thres6:
            categeory[i]=5
         if categeory[i]==thres7:
            categeory[i]=6
         if categeory[i]==thres8:
            categeory[i]=7
         if categeory[i]==thres9:
            categeory[i]=8
         if categeory[i]==thres10:
            categeory[i]=9
         if categeory[i]==thres11:
            categeory[i]=10
         if categeory[i]==thres12:
            categeory[i]=11
         if categeory[i]==thres13:
            categeory[i]=12
         if categeory[i]==thres14:
            categeory[i]=13
         if categeory[i]==thres15:
            categeory[i]=14
         if categeory[i]==thres16:
            categeory[i]=15
         if categeory[i]==thres17:
            categeory[i]=16
         if categeory[i]==thres18:
            categeory[i]=17
         if categeory[i]==thres19:
            categeory[i]=18
         if categeory[i]==thres20:
            categeory[i]=19              
                     
     return categeory

df["insured_hobbies"].unique()

ih=df["insured_hobbies"]
thres1="sleeping"
thres2="reading"
thres3="board-games"
thres4="bungie-jumping"
thres5="base-jumping"
thres6="golf"
thres7="camping"
thres8="dancing"
thres9="skydiving"
thres10="movies"
thres11="hiking"
thres12="yachting"
thres13="paintball"
thres14="chess"
thres15="kayaking"
thres16="polo"
thres17="basketball"
thres18="video-games"
thres19="cross-fit"
thres20="exercise"
ihf=insured_hobbies_filter(icc,thres1,thres2,thres3,thres4,thres5,thres6,thres7,thres8,thres9,thres10,thres11,thres12,thres13,thres14,thres15,thres16,thres17,thres18,thres19,thres20)
df["insured_hobbies"]=ihf
def data_split(data,ratio):
    np.random.seed(100)
    shuffled = np.random.permutation(len(data))
    test_data_size = int(len(data)*ratio)
    test_data_indices = shuffled[: test_data_size]
    train_data_indices = shuffled[test_data_size :]
    return data.iloc[test_data_indices], data.iloc[train_data_indices]

test_data, train_data = data_split(df, 0.25)

train_data

test_data

#df.drop(df.index[df['police_report_available'] == '?'], inplace=True)
#df

x=df["policy_annual_premium"]
x

import math

import math
def func(categeory):
  for i in range(len(categeory)):
    categeory[i]=math.ceil(int(categeory[i]))
  return categeory

fin=func(x)
df["policy_annual_premium"]=fin
df['policy_annual_premium'].astype('int')


print(type(df['policy_annual_premium'][1]))

from google.colab import files
df.to_csv('fd_cleaned_data.csv') 
files.download('fd_cleaned_data.csv')

x_train=train_data[["months_as_customer","age","policy_number","policy_state","policy_csl","policy_deductable","policy_annual_premium","umbrella_limit","insured_sex","insured_education_level","insured_occupation","insured_hobbies","insured_relationship","capital-gains","capital-loss","incident_type","collision_type","incident_severity","authorities_contacted","incident_state","incident_city","incident_hour_of_the_day","number_of_vehicles_involved","property_damage","bodily_injuries","witnesses","police_report_available","total_claim_amount","injury_claim","property_claim","vehicle_claim","auto_make","auto_year","fraud_reported"]].to_numpy()
x_train

x_test=test_data[["months_as_customer","age","policy_number","policy_state","policy_csl","policy_deductable","policy_annual_premium","umbrella_limit","insured_sex","insured_education_level","insured_occupation","insured_hobbies","insured_relationship","capital-gains","capital-loss","incident_type","collision_type","incident_severity","authorities_contacted","incident_state","incident_city","incident_hour_of_the_day","number_of_vehicles_involved","property_damage","bodily_injuries","witnesses","police_report_available","total_claim_amount","injury_claim","property_claim","vehicle_claim","auto_make","auto_year","fraud_reported"]].to_numpy()
x_test

y_train = train_data[['fraud_reported']].to_numpy().reshape(750, ).astype('int')
y_test = test_data[['fraud_reported']].to_numpy().reshape(250, ).astype('int')
from sklearn.linear_model import LogisticRegression
clflo = LogisticRegression()
clflo.fit(x_train, y_train)

y_pred=clflo.predict_proba(x_test)

from sklearn.metrics import log_loss
log_loss(y_test,y_pred)

from sklearn.tree import DecisionTreeClassifier

clf=DecisionTreeClassifier(criterion = "gini", splitter = 'random', max_leaf_nodes = 10, min_samples_leaf = 5, max_depth= 5)

# Train Decision Tree Classifer
clf= clf.fit(x_train,y_train)

DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=5,
            max_features=None, max_leaf_nodes=10, min_samples_leaf=5,
            min_samples_split=2, min_weight_fraction_leaf=0.0, random_state=None, splitter='random')

#Predict the response for test dataset
y_pred1 = clf.predict(x_test)

print(y_pred1)

from sklearn import tree

from sklearn.metrics import accuracy_score

score = accuracy_score(y_test,y_pred1)

print(score)

from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)

print(y_pred)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

y_pred2= classifier.predict(x_train)

print(y_pred2)

acc=accuracy_score(y_train,y_pred2)
acc1=accuracy_score(y_test,y_pred)
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine

model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')

model.fit(x_train, y_train)

XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, eval_metric='mlogloss',
              gamma=0, gpu_id=-1, importance_type='gain',
              interaction_constraints='', learning_rate=0.300000012,
              max_delta_step=0, max_depth=6, min_child_weight=1,
              monotone_constraints='()', n_estimators=100, n_jobs=16,
              num_parallel_tree=1, objective='multi:softprob', random_state=0,
              reg_alpha=0, reg_lambda=1, scale_pos_weight=None, subsample=1,
              tree_method='exact', use_label_encoder=False,
              validate_parameters=1, verbosity=None)

y_pred_fin=model.predict(x_test)


accuracy = accuracy_score(y_test,y_pred_fin)

result=classifier.predict([[228,42,342868,1,5,2000,1198.0,5000000,468176,1,0,1,1,1,0,0,1,2,0,1,1,1,8,1,0,0,0,0,5070,780,780,3510,1,2007]])
print(result)

if result==1:
  print("you are just goning to get only certain amount of money after exemption ")
else:
  print("your claim is successfully our officers are going to contact you soon and\"THANK YOU FOR INFORMING US :)\"")

result=classifier.predict([[94,26,215278,1,3,500,723.0,0,433696,1,0,3,3,0,50300,0,2,2,1,3,3,3,6,3,1,1,2,1,36700,3670,7340,25690,3,2010]])
print(result)

if result==1:print("you are just goning to get only certain amount of money after exemption ")
else:print("your claim is successfully our officers are going to contact you soon and\"THANK YOU FOR INFORMING US :)\"")

import pickle
pickle.dump(classifier,open('pickel_model.pkl','wb'))

model=pickle.load(open('pickel_model.pkl','rb'))