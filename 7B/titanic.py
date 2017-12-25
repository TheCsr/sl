import pandas as pd
import numpy as np
import matplotlib as plt
titanic_data=pd.read_csv('titanic.csv')
print(titanic_data.head())
titanic_data.info()
print(titanic_data.describe())

titanic_data=titanic_data(['Ticket'],axis=1)

titanic_data['Embarked']=titanic_data['Embarked'].fillna("XX")
print ( "No of entries,No of attributes",titanic_data.shape) 

print(titanic_data.keys())

print(titanic_data.dtypes)

print ("Min age: ",titanic_data['Age'].min())
print ("Max age: ",titanic_data['Age'].max())
print ("Mean age: ",titanic_data['Age'].mean())

titanic_data= titanic_data['Age'].plot.hist()
titanic_data.set_xlabel('Age')
titanic_data.set_ylabel('Number of People')
plt.show(block=True)

