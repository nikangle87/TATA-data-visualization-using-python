# -*- coding: utf-8 -*-
"""TATA_from _hometown.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VTtTmECKl-JeJsZSLx7JJIqoXu5GLZoz
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

sales= pd.read_excel('/content/sample_data/Online Retail.xlsx')
sales.head()

### To set month in proper sequence for proper operation

sales['month_year'] = sales['InvoiceDate'].dt.to_period('M')

### Get total sales by total quantity multiply by unite price
 
sales['total_sales']= sales['Quantity']*sales['UnitPrice']
sales.head()

"""# For CEO
Which month generate more revenue and less also graph for all month...

--> its clearly show octomber, november and december generate 
"""

# To get which month we sell more...productive

max_sales=sales.groupby('month_year').sum()
max_month_sales=max_sales.drop(['CustomerID','Quantity','UnitPrice','CustomerID'],axis=1)
max_month_sales.reset_index(inplace=True)
max_month_sales.sort_values(['total_sales'],ascending=False)

pl=sns.catplot(y='month_year',x='total_sales',kind='bar',data=max_month_sales)

"""### Which country generate most revenue and less also.

## -->accoroding to sales number and graph we will see 
## -->united kingdom generate 83.99 its nearly ~84.00% revenue generate alone.
"""

country=sales.groupby(['Country']).sum()
country.reset_index(inplace=True)
country.sort_values(['total_sales'],ascending=False)

(8187806.364/(max_month_sales.sum())*100)

sns.catplot(data=country,x='total_sales',y='Country',kind='bar')

##top customer 
top_customer=sales.groupby(['CustomerID']).max()
top_customer.sort_values('total_sales',ascending=False)

a=sales['CustomerID']==16446.0
sales.loc[a]

"""# Top customer contribute and generate 1.72% revenue in total revenue."""

(168469.60/(max_month_sales.sum())*100)

filt=((sales['InvoiceDate']>= pd.to_datetime('2010-12-01')) & (sales['InvoiceDate']<=pd.to_datetime('2011-03-01')))
first_qtr=sales.loc[filt]
first_qtr['tsales1']=sales['Quantity']*sales['UnitPrice']
first_qtr1=first_qtr.groupby(['month_year']).sum()
# first_qtr.drop(['CustomerID','Quantity','UnitPrice'],axis=1)
first_qtr1.reset_index(inplace=True)
first_qtr1

sns.catplot(data=first_qtr1,x='month_year',y='tsales1',kind='bar')

filt=((sales['InvoiceDate']>= pd.to_datetime('2011-03-01')) & (sales['InvoiceDate']<=pd.to_datetime('2011-06-01')))
second_qtr=sales.loc[filt]
second_qtr['tsales2']=sales['Quantity']*sales['UnitPrice']
second_qtr2=second_qtr.groupby(['month_year']).sum()
# first_qtr.drop(['CustomerID','Quantity','UnitPrice'],axis=1)
second_qtr2.reset_index(inplace=True)
second_qtr2

sns.catplot(data=second_qtr2,x='month_year',y='tsales2',kind='bar')

filt=((sales['InvoiceDate']>= pd.to_datetime('2011-06-02')) & (sales['InvoiceDate']<=pd.to_datetime('2011-09-01')))
third_qtr=sales.loc[filt]
third_qtr['tsales3']=sales['Quantity']*sales['UnitPrice']
third_qtr3=third_qtr.groupby(['month_year']).sum()
# first_qtr.drop(['CustomerID','Quantity','UnitPrice'],axis=1)
third_qtr3.reset_index(inplace=True)
third_qtr3

sns.catplot(data=third_qtr3,x='month_year',y='tsales3',kind='bar')

filt=((sales['InvoiceDate']>= pd.to_datetime('2011-09-02')) & (sales['InvoiceDate']<=pd.to_datetime('2011-12-09')))
fourth_qtr=sales.loc[filt]
fourth_qtr['tsales4']=sales['Quantity']*sales['UnitPrice']
fourth_qtr4=fourth_qtr.groupby(['month_year']).sum()
# first_qtr.drop(['CustomerID','Quantity','UnitPrice'],axis=1)
fourth_qtr4.reset_index(inplace=True)
fourth_qtr4

sns.catplot(data=fourth_qtr4,x='month_year',y='tsales4',kind='bar')

totalsalesof1stqtr=first_qtr1['tsales1'].sum()
totalsalesof2ndqtr=second_qtr2['tsales2'].sum()
totalsalesof3rdqtr=third_qtr3['tsales3'].sum()
totalsalesof4thqtr=fourth_qtr4['tsales4'].sum()

import matplotlib.pyplot as plt
import seaborn
data=[totalsalesof1stqtr,totalsalesof2ndqtr,totalsalesof2ndqtr,totalsalesof4thqtr]
keys=['1st','2nd','3rd','4th']
palette_color = seaborn.color_palette('bright')
  
# plotting data on chart
plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')
  
# displaying chart
plt.show()

"""# **FOR CMO**

# product purchase more than '1' and generate revenue
"""

b=sales['Quantity']>1
c=sales.loc[b]
c['total_sales'].sum()

"""## 99% percent revenue genereted by customer who purchase more than one product."""

(9661173.749999996/(max_month_sales.sum())*100)

sales['Description'].value_counts()

"""# Most repeted product..WHITE HANGING HEART T-LIGHT HOLDER 
# purchase by customer max time and generate 1% revenue. 
"""

ad=sales['Description']=='WHITE HANGING HEART T-LIGHT HOLDER'
most_repeated=sales.loc[ad]
most_repeated['total_sales'].sum()

(99668.47/(max_month_sales.sum())*100)

# we get the data when customer buy more product so we improve buiness to give more offers on these time 
sales['hour']= sales['InvoiceDate'].dt.hour
sales['minute']= sales['InvoiceDate'].dt.minute
sales.head()

"""# TO generate revenue...give attaractive or combo offer

## accoroding to chart in morning 10:00 a.m. to evening 04:00 p.m. buying power is increase but in at 12:00 p.m. and 03:00 its pickso if we give offer between 11:30 a.m. to 12:30 p.m. and 2:30p.m. to 03:30 p.m.
"""

# accoroding to chart in morning 10:00 a.m. to evening 04:00 p.m. buying power is increase but in at 12:00 p.m. and 03:00 its pick
# so if we give offer between 11:30 a.m. to 12:30 p.m. and 2:30p.m. to 03:30 p.m.
hour= [hour for hour, df in sales.groupby('hour')]
plt.plot(hour,sales.groupby(['hour']).count())
plt.grid()
plt.xlabel('hour')
plt.ylabel('sales')
plt.show()
# sales.groupby(['hour']).count()

"""# accoroding to these operation we found that which product sold together so company give the combo offer or card offer as per transaction to generate maximum revenue when weekend or chrismas time."""

df=sales[sales['InvoiceNo'].duplicated(keep=False)]
df['group']=  df.groupby('InvoiceNo')['Description'].transform(lambda x : ','.join(x))
df=df[['InvoiceNo','group']].drop_duplicates()
# df.head(10)
from itertools import combinations
from collections import Counter

count = Counter()
for raw in df['group']:
  raw_list= raw.split(',')
  count.update(Counter(combinations(raw_list,2)))

for key,value in count.most_common(10):
  print(key,value)