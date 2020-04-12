# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:22:59 2020

@author: draj7
"""

'''Note: 

* Before writing any code remember that this assigment is for helping you understand the basics of file
handling in csv file. 

* This project is designed to have a work flow such that everyone is in same page for this purpose the variables are
given a strict name which should not be changed or modified according to your convinience

* Few of new functions like .head() .xticks().... and concepts may have been introduced in the assingment, so we encourage you
all to go through them without skipping.

*  functions which are to be used in the Your code sections are globally available so try to look for those where you have been prompted
'''

'''Its the data of a meal delivery company which operates in multiple cities. 
They have various fulfillment centers in these cities for dispatching meal orders to their customers.
train.csv: Historical data of demand for a product-center combination 
fulfilment_center_info.csv: Information for fulfillment center like center area, city information etc.
meal_info.csv: Product(Meal) features such as category, sub-category, current price and discount'''


'''START CODE'''

#Import necessary libraries: Numpy,pandas,matplotlib

'''************************Your code here**********************'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''************************************************************'''


#read meal_info.csv file from provided dataset into a df_meal named variable
#Note: Proper file directory should be provided

'''************************Your code here**********************'''
df_meal=pd.read_csv('meal_info.csv')
'''************************************************************'''


df_meal.head()'''This is for displaying first five data points'''

#read fulfilment_center_info.csv file from provided dataset
#Note: Proper file directory should be provided

'''************************Your code here**********************'''
df_center=pd.read_csv('fulfilment_center_info.csv')
'''************************************************************'''

df_center.head()'''This is for displaying first five data points'''

#read train.csv file from provided dataset
#Note: Proper file directory should be provided

'''************************Your code here**********************'''
df_food=pd.read_csv('train.csv')
'''************************************************************'''

df_food.head()

'''Since the provided information is in different files, your work here is to merge them.Look for the functions
in pandas library to do so'''

'''************************Your code here**********************'''
df=pd.concat([df_meal,df_center,df_food],axis=1,sort=False)
'''************************************************************'''

'''Here we have used pd.pivot_table() kindly go through the function and mention in comment what it does'''

table = pd.pivot_table(data=df,index='category',values='num_orders',aggfunc=np.sum)



'''Graph tweaking
************************
Plot a bar graph with title 'Most popular food' for category(x-axis) vs number-of-orders(y-axis)

give x label 'Food items'
give y label 'Quantity sold'

'''

'''************Yourcode*********************'''
table.plot(kind='bar')
#bar graph


#xticks 
plt.xticks(rotation=70) '''Write on comment what you feel this function does'''

#x-axis labels 
plt.xlabel('food_category')

#y-axis labels 

plt.ylabel('num_of_orders')
#plot title 
plt.title('category VS num_of_orders')

#save plot 
plt.savefig('bar_grapgh')
#display 
plt.show()

'''************************************************'''


'''Comparison of weekly and monthly sales
 Create a new column
* named 'revenue' where each element is product of checkout_price and num_orders 
** named 'month' by using ['week'] column (week column value divided by 4 gives month value)'''

'''**************************Your code******************************'''
Week=pd.concat([df['week'],df['checkout_price']*df['num_orders']],axis=1)
Week.columns=['week','num_orders']
Week=Week.groupby(['week'],as_index=False).sum()

Month=Week.copy()
Month['week']=(Month['week']-1)//4
Month.columns=['month','num_orders']
Month=Month.groupby(['month'],as_index=False).sum()

'''******************************************************************'''
'''Here we have created two list month and month_order ,
store month number in month list and revenue of each month in month_order'''
#list to store month-wise revenue 
month=[] 
month=Month['month']
'''***********************************Your code***********************'''
  month_order=[] 
month_order=Month['num_orders']  
'''*********************************************************************'''
'''Here we have created two list week and week_order ,you need to store in them mapping the monthly orders'''    
#list to store week-wise revenue 
week=[] 
week_order=[] 
'''***********************************Your code***********************'''
week=Week['week']
week_order=Week['num_orders']

'''*********************************************************************'''
''' Plot two subplots in the same space : one for weekly revenue and other for monthly revenue.
For weekly : Title(Weekly income),x_label(week),y_label(revenue); similarly for monthly revenue.
'''

'''************Yourcode*********************'''
plt.subplot(2,1,2)
plt.plot(Month['month'],Month['num_orders'])
plt.title('monthly income')
plt.xlabel('month')
plt.ylabel('revenue')

plt.subplot(2,1,1)
plt.plot(Week['week'],Week['num_orders'])
plt.title('weekly income')
plt.xlabel('week')
plt.ylabel('revenue')

''' Display the plot'''
plt.show()
