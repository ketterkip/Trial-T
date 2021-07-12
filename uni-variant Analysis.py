import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os


"""reading dataset"""
#df = pd.read_csv("bigmart1.csv")
#print(df)

"""define working directory"""
os.chdir('C:\\Users\\KETTER\\PycharmProjects\\pythonProject')

"""import dataset"""
data = pd.read_csv("bigmart_data.csv")
#data.head(5)
#print(data)

"""data info"""
#data.info()

"""Checking for Null Data"""
df = data.isnull().sum()
#print(df)

"""Dropping Null DAta"""
df = data.fillna(how = 'any').shape
df = data.dropna(subset = ['Item_Weight', 'Outlet_Size', 'Item_Outlet_Sales'],how='any' ).shape
df = data.columns
#print(df)
df = data.dropna(inplace=False)
#print(df)

"""Saving New Dataset with No Null Data"""
data1 = df.to_csv("bigmart_data1.csv", index=False)
#print(data1)

"""print(converting into csv file with a new file name)"""
#df.to_csv('C:\\Users\\KETTER\\PycharmProjects\\pythonProject\\bigmart_data1.csv', index=False)
#print(df)

"""Reading New Dataset"""
data1 = pd.read_csv("bigmart_data1.csv")
#data1.head()
#print(data1)
data1.describe()

print(data1)

#data1.describe(include='all')
#print(data1)

#df.describe(include=[np.number])
#print(df)

#data_1 = pd.read_csv("bigmart1.csv")
#print(data_1)

#def min_max_values(col):
#    '''the function takes the column name as the argument and returns the top & bottom observation in that dataframe'''
#    top = data1[col].idmax()
#    top_obs = pd.DataFrame(data1.loc[top])
#
#    bottom = data1[col].idmin()
#    bot_obs = pd.DataFrame(data1.loc[bottom])

#    min_max_obs = pd.concat([top_obs, bot_obs], axis=1)
#    return min_max_obs

#min_max_values('Item_Weight')


"""Histogram of contineous numerical variable"""
#num_bins = 10
#plt.hist(data1['Outlet_Location_Type'], 10)
#plt.show()

"""probability Distribution Function"""
#sns.distplot(data1['Item_Outlet_Sales'],10)
#plt.show()

"""count by category - cross tabulation"""
#make_dist = data1.groupby('Item_Type').size()
#print(make_dist)

"""Distribution of categorical variable"""
#make_dist.plot(title='Item_Type' )
#plt.show()

#data.info()

"""select all numerical variables"""
data1_num = data1.select_dtypes(include=['float64', 'int64'])
#print(data1_num.head())

#data1_num.hist(bins=20)
#plt.show()

"""correlation with variable of interest ---Only numerical variables not categorical variables"""
#data1_corr = data1_num.corr()['Outlet_Establishment_Year'][:-1]
#print(data1_corr)

"""correlation plot using 'pairplot'"""
#for i in range(0, len(data1_num.columns),10):
 #   sns.pairplot(data1_num, y_vars=['Item_Visibility'], x_vars=data1_num.columns[i:i+10])
#plt.show()

"""box-plot (categorical variable)"""
#box1 = sns.boxplot(x='Item_Type', y='Outlet_Establishment_Year', data=data1)
#plt.show()

#box2 = sns.boxplot(x='Outlet_Size', y='Item_Outlet_Sales', data=data1)
#plt.show()


"""Regression plot"""
#sns.regplot(data1['Item_Outlet_Sales'], data1['Outlet_Establishment_Year'])
#plt.show()























