#joining Datasets
import pandas
import pandas as pd

"""Reading datasets"""
customer = pd.read_csv("customer.csv")
#print(customer)

#payment = pd.read_csv("payment.csv")
#print(payment)

#staff = pd.read_csv("staff.csv")
#print(staff)

address = pd.read_csv("address.csv")
#print(address)

city = pd.read_csv("city.csv")
#print(city)

country = pd.read_csv("country.csv")
#print(country)

#rental = pd.read_csv("rental.csv")
#print(rental)

"""joining diferent tables with relationships"""

customer = customer.set_index('address_id')

jointaddr = customer.join(address, rsuffix=('address_id'))
#print(jointaddr)

jointaddr= jointaddr.set_index('city_id')

joincity = jointaddr.join(city, rsuffix=('city_id'))
#print(joincity)

joincity = joincity.set_index('country_id')

joincountry = joincity.join(country, rsuffix=('country_id'))
joinall = pd.DataFrame(joincountry)
#print(joinall)

"""Saving joint tables to CSV"""

#joinall.to_csv('C:\\Users\\KETTER\\PycharmProjects\\pythonProject\\join_all.csv')


"""Analysis"""

df = pd.read_csv('join_all.csv')
#df.head()
#print(df)

df1 = df[df['country'] == 'Chad']
#print(df1)

selected = df[["first_name", "last_name", "country"]]
filt = pd.DataFrame(selected)
df.shape
#print(filt)

df1 = filt[df['country'] == 'India']
df2 = filt[df['country'] == 'Egypt']
df3 = filt[df['country'] == 'Kuwait']

#print(df1)
#print(df2)
#print(df3)

result = df1.append([df2, df3])

d1 = result
df = pd.DataFrame(d1)
#print('Source DataFrame:\n', df)

#rename columns
df1 = df.rename(columns={'first_name': 'First Name', 'last_name': 'Last Name', 'country': 'Country'})
#print('Source DataFrame:\n', df1)
df1.reset_index(drop=True, inplace=True)

#print(df1)

"""Save Dataframe in CSV"""

df1.to_csv('C:\\Users\\Public\\SQL\\customer_home_final.csv')


#df = df1.rename(columns={"first_name":"First Name"})
#print(df)



"""Question 3, a list of Customers with their payments"""

"""list of Customers with their payments."""

cust_join  = pd.read_csv("join_all.csv")

#print(cust_join)

payment = pd.read_csv("payment.csv")
#print(payment)

"""joining Tables"""
cust_join = cust_join.set_index('customer_id')

cust_pay = cust_join.join(payment, rsuffix=('customer_id'))
cust_payment = pd.DataFrame(cust_pay)
#print(cust_payment)

#cust_payment.to_csv('C:\\Users\\KETTER\\PycharmProjects\\pythonProject\\customerPayment.csv')

"""list with their payment"""
"""Query columns first"""

cpayment = pd.read_csv("customerPayment.csv")
#cpayment.info()
#cpayment= cpayment.isnull().sum()
#print(cpayment)

#print(cpayment[['customer_id','first_name','last_name','payment_id','amount','payment_date']])
list_customerPayment = pd.DataFrame(cpayment)
#print(list_customerPayment)

list_customerPayment.drop(list_customerPayment.columns[[1,2,5,6,7,8,9,1,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26]], axis=1, inplace=True)
list_customerPayment.reset_index(drop=True, inplace=True)
df11 = pd.DataFrame(list_customerPayment)
#print(df11)

"""To CSV file"""
#list_customerPayment.to_csv('C:\\Users\\Public\\SQL\\list_customerPayment_final.csv')

























