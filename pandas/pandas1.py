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
abvage = df["Age"]>25
print("salary of age above 25 is :\n",pd.where(abvage)[0])

