import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('uber.csv')
df.head()
Unnamed:
0 key fare_amount pickup_datetime pickup_longitude
0 24238194 2015-05-07
19:52:06.0000003 7.5 2015-05-07
19:52:06 UTC -73.999817
1 27835199 2009-07-17
20:04:56.0000002 7.7 2009-07-17
20:04:56 UTC -73.994355
2 44984355 2009-08-24
21:45:00.00000061 12.9 2009-08-24
21:45:00 UTC -74.005043
3 25894730 2009-06-26
08:22:21.0000001 5.3 2009-06-26
08:22:21 UTC -73.976124
4 17610152 2014-08-28
17:47:00.000000188 16.0 2014-08-28
17:47:00 UTC -73.925023
df.columns
Index(['Unnamed: 0', 'key', 'fare_amount', 'pickup_datetime',
'pickup_longitude', 'pickup_latitude', 'dropoff_longitude',
'dropoff_latitude', 'passenger_count'],
dtype='object')
df=df.drop(columns=(['pickup_longitude', 'pickup_latitude', 'dropoff_longitude'
df.head()
Unnamed:
0 key fare_amount pickup_datetime passenger_count
0 24238194 2015-05-07
19:52:06.0000003 7.5 2015-05-07
19:52:06 UTC 1
1 27835199 2009-07-17
20:04:56.0000002 7.7 2009-07-17
20:04:56 UTC 1
2 44984355 2009-08-24
21:45:00.00000061 12.9 2009-08-24
21:45:00 UTC 1
3 25894730 2009-06-26
08:22:21.0000001 5.3 2009-06-26
08:22:21 UTC 3
4 17610152 2014-08-28
17:47:00.000000188 16.0 2014-08-28
17:47:00 UTC 5
In [82]:
In [83]:
In [84]:
Out[84]:
In [85]:
Out[85]:
In [86]:
In [87]:
Out[87]:
df.describe()
Unnamed: 0 fare_amount passenger_count
count 2.000000e+05 200000.000000 200000.000000
mean 2.771250e+07 11.359955 1.684535
std 1.601382e+07 9.901776 1.385997
min 1.000000e+00 -52.000000 0.000000
25% 1.382535e+07 6.000000 1.000000
50% 2.774550e+07 8.500000 1.000000
75% 4.155530e+07 12.500000 2.000000
max 5.542357e+07 499.000000 208.000000
df.describe()[['fare_amount', 'passenger_count']]
fare_amount passenger_count
count 200000.000000 200000.000000
mean 11.359955 1.684535
std 9.901776 1.385997
min -52.000000 0.000000
25% 6.000000 1.000000
50% 8.500000 1.000000
75% 12.500000 2.000000
max 499.000000 208.000000
df.shape
(200000, 5)
Finding outliers using data-visualization
methods
View the data distribution using a
histogram
plt.figure(figsize=(16,5))
In [88]:
Out[88]:
In [89]:
Out[89]:
In [90]:
Out[90]:
In [91]:
plt.subplot(1,1,1)
sns.histplot(df['fare_amount'])
<Axes: xlabel='fare_amount', ylabel='Count'>
Find outliers in data using a box plot
sns.boxplot(y=df['fare_amount'])
<Axes: ylabel='fare_amount'>
sns.boxplot(y=df['passenger_count'])
<Axes: ylabel='passenger_count'>
Out[91]:
In [92]:
Out[92]:
In [93]:
Out[93]:
Finding outliers using statistical
methods
calculate the outlier data points using the statistical method called interquartile
range (IQR). Using the IQR, the outlier data points are the ones falling below
Q1–1.5 IQR or above Q3 + 1.5 IQR. The Q1 is the 25th percentile and Q3 is the
75th percentile of the dataset, and IQR represents the interquartile range
calculated by Q3 minus Q1 (Q3–Q1).
Use pandas .quantile() function
#create a function to find outliers using IQR
def find_outliers_IQR(df):
q1=df.quantile(0.25)
q3=df.quantile(0.75)
IQR=q3-q1
outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]
return outliers
outliers = find_outliers_IQR(df['fare_amount'])
print("number of outliers: "+ str(len(outliers)))
number of outliers: 17167
In [94]:
In [95]:
In [96]:
print('max outlier value: '+ str(outliers.max()))
max outlier value: 499.0
print('min outlier value: '+ str(outliers.min()))
min outlier value: -52.0
outliers
6 24.50
30 25.70
34 39.50
39 29.00
48 56.80
...
199976 49.70
199977 43.50
199982 57.33
199985 24.00
199997 30.90
Name: fare_amount, Length: 17167, dtype: float64
Removing Outliers
q1 = df['fare_amount'].quantile(0.25)
q3 = df['fare_amount'].quantile(0.75)
IQR = q3-q1
lower_bound= q1-1.5*IQR
lower_bound
np.float64(-3.75)
upper_bound = q3 + 1.5 * IQR
upper_bound
np.float64(22.25)
#Filter the data to keep only non-outliers
# This creates a new DataFrame where the 'fare_amount' is within the bounds
df_cleaned = df[(df['fare_amount'] >= lower_bound) & (df['fare_amount'] <= upper_bound
df_cleaned
In [97]:
In [98]:
In [99]:
Out[99]:
In [100…
Out[100…
In [101…
In [102…
Out[102…
In [103…
In [104…
In [105…
Unnamed:
0 key fare_amount pickup_datetime passenger_count
0 24238194 2015-05-07
19:52:06.0000003 7.5 2015-05-07
19:52:06 UTC
1 27835199 2009-07-17
20:04:56.0000002 7.7 2009-07-17
20:04:56 UTC
2 44984355 2009-08-24
21:45:00.00000061 12.9 2009-08-24
21:45:00 UTC
3 25894730 2009-06-26
08:22:21.0000001 5.3 2009-06-26
08:22:21 UTC
4 17610152 2014-08-28
17:47:00.000000188 16.0 2014-08-28
17:47:00 UTC
... ... ... ... ...
199994 3189201 2014-01-31
14:42:00.000000181 12.0 2014-01-31
14:42:00 UTC
199995 42598914 2012-10-28
10:49:00.00000053 3.0 2012-10-28
10:49:00 UTC
199996 16382965 2014-03-14
01:09:00.0000008 7.5 2014-03-14
01:09:00 UTC
199998 20259894 2015-05-20
14:56:25.0000004 14.5 2015-05-20
14:56:25 UTC
199999 11951496 2010-05-15
04:08:00.00000076 14.1 2010-05-15
04:08:00 UTC
182833 rows × 5 columns
df_cleaned.shape
(182833, 5)
182833 +17167
200000
sns.histplot(df_cleaned['fare_amount'])
<Axes: xlabel='fare_amount', ylabel='Count'>
Out[105…
In [106…
Out[106…
In [107…
Out[107…
In [108…
Out[108…
plt.figure(figsize=(16,5))
plt.subplot(1,2,1)
sns.histplot(df['fare_amount'])
plt.subplot(1,2,2)
sns.histplot(df_cleaned['fare_amount'])
<Axes: xlabel='fare_amount', ylabel='Count'>
sns.boxplot(y=df_cleaned['fare_amount'])
<Axes: ylabel='fare_amount'>
In [109…
Out[109…
In [68]:
Out[68]:
plt.figure(figsize=(16,5))
plt.subplot(1,2,1)
sns.boxplot(df['fare_amount'])
plt.subplot(1,2,2)
sns.boxplot(df_cleaned['fare_amount'])
<Axes: ylabel='fare_amount'>
In [110…
Out[110…
In [ ]:
