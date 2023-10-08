Customer Segmentation
Customer segmentation is the method of distributing a customer base into collections of people based on mutual characteristics so organizations can market to group efficiently and competently individually.

The purpose of segmenting customers is to determine how to correlate to customers in multiple segments to maximize customer benefits. Perfectly done customer segmentation empowers marketers to interact with every customer in the best efficient approach.

The data includes the following features:

Customer ID

Customer Gender

Customer Age

Annual Income of the customer (in Thousand Dollars)

Spending score of the customer (based on customer behaviour and spending nature)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv("/content/Mall_Customers.csv")
df.head()
  CustomerID	Gender	 Age	Annual Income (k$)	Spending Score (1-100)
0  1          Male	  19	  15	     39
1  2         	Male	  21   15	     81
2  3	         Female	20	  16	     6
3  4	         Female	23	  16	     77
4  5	         Female	31  	17     	40

df.shape
(200, 5)
df.describe()
CustomerID	Age	Annual Income (k$)	Spending Score (1-100)

count	200.000000	200.000000	200.000000	200.000000
mean	100.500000	38.850000	60.560000	50.200000
std	57.879185	13.969007	26.264721	25.823522
min	1.000000	18.000000	15.000000	1.000000
25%	50.750000	28.750000	41.500000	34.750000
50%	100.500000	36.000000	61.500000	50.000000
75%	150.250000	49.000000	78.000000	73.000000
max	200.000000	70.000000	137.000000	99.000000
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 5 columns):
 #   Column                  Non-Null Count  Dtype 
---  ------                  --------------  ----- 
 0   CustomerID              200 non-null    int64 
 1   Gender                  200 non-null    object
 2   Age                     200 non-null    int64 
 3   Annual Income (k$)      200 non-null    int64 
 4   Spending Score (1-100)  200 non-null    int64 

dtypes: int64(4), object(1)
memory usage: 7.9+ KB
df['Gender'].describe()

count        200
unique         2
top       Female
freq         112

Name: Gender, dtype: object
plt.figure(figsize=(8,7))
sns.countplot(df["Gender"])
plt.xlabel("Gender",fontsize = 15)
plt.show()
.........
plt.figure(figsize=(10,8))
sns.distplot(df["Age"],color = "Green")
plt.xlabel("Age",fontsize = 15)
plt.show()
