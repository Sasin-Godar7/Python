import pandas as pd

#create a series
s = pd.Series([1,2,3,4,5])
print("Series :",s)

#create a dataframe
# data ={
#     'A' :[1,2,3,4],
#     'B' : [5,6,7,8],
#     'C':[9,10,11,12]
# }

# df = pd.DataFrame(data)
# print("DataFrame :\n",df)


data = {
    'Name': ["subesh","Smith","ranjan","ritesh","amir"],
    'Age' :[12,23,23,34,34,],
    'City' : ["buspark","ctwn","ktm","pkr","butwal"]
}

df = pd.DataFrame(data)
print("DataFrame :\n",df)

age_colum = df['Age']
# print("Age column :\n",age_colum)

name_age  = df[['Name','Age']]
print("name colum and age colum:\n",name_age)


#selecting row by index

first_row = df.iloc[0]  #indexing ni deko
print("\nFirst row :\n",first_row)

first_two_rows = df.loc[0:1]  #level deko tokera  
print("\n first two rows :\n",first_two_rows)

#adding new salary column
df['Salary'] = [75000,45000,23000,32334,20000]
print("DataFrame with salary column :\n",df)

#filtering data:show the data whose age > 25
filter_data = df[df["Age"]>25]
print("salary of age above 25 is :\n",filter_data)

#using head to view first 5 rows
print("first 5 rows :\n",df.head())

#using head to view first 3 rows
print("first 3 rows:\n",df.head(3))

#using tail
print("last five rows :\n",df.tail())

#for last 3 rows
print("last 3 rows :\n",df.tail(3))
print("\n")

#Accessing dataFrame attributes

print("dataframe index :",df.index)
print("\n")
print("dataframe column :",df.columns)
print("\n")
print("dataframe data types :\n",df.dtypes)
print("\n")
print("dataframe shape :",df.shape)
print("\n")
print("dataframe size :",df.size)
print("\n")
print("dataframe values :",df.values)
print("\n")
print("dataframe transpose :\n",df.T)
print("\n\n")
print("dataframe info :")
df.info()
print("\n")

#For series

ser = pd.Series([1,2,3],index=['a','b','c'], name = "Example Series")

#Accenssing the series 

print("Series index :",ser.index)
print("\n")
print("Series data types :\n",ser.dtypes)
print("\n")
print("Series shape :",ser.shape)
print("\n")
print("Series size :",ser.size)
print("\n")
print("Series Name :\n",ser.name)
print("\n")
print("Series transpose :\n",ser.is_unique)
print("\n\n")
print("Series info :\n",ser.isnull())
print("\n")



