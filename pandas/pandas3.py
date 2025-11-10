import pandas as pd
data = {
    'Name' : ['Subesh','Smith','Rajan','Ritesh','Amir','Ranjan','Anuz','Budhha'],
    'Age' : [25,27,21,26,25,28,31,43],
    'City' :["Bus-park","Gaidakot","Kshetrapur","Parsa","Parbatipur","Tandi","Chanauli","Gaidakot"]
}

df = pd.DataFrame(data)
#save the dataframe to a csv file

# df.to_csv('example.csv',index=False)
# print("\nDataframe saved sucessfully....")

#now after adding rows and column name "Salaries"
#read the csv file

df = pd.read_csv('example.csv')

#show basic information
print("Dataframe Info :")
print(df.info())

#show the mean of age 
age_mean = df['Age'].mean()
print("\nthe age of mean is :",age_mean)

#filter the dataframe for rows where age > 25 then save the record as filterdata.csv
filter_age =df[ df["Age"]>25]
print("age greater then 25 :\n",filter_age)
filter_age.to_csv('filterage.csv',index=False)
