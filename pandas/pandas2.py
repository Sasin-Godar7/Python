import pandas as pd

data = {
    'Name' : ["subash","Smith","Rajan","Ritesh","Amir"],
    'Age' : [25,27,None,26,25],
    'City' : ["buspark",None,'kshetrapur','parsa','parbatipur'],
    # 'pity' : ["buspark",'csksd','kshetrapur','parsa','parbatipur']
}

df = pd.DataFrame(data)

print("Is Null:\n",df.isnull())

df_dropped_rows = df.dropna()
print("DataFrame with dropped rows :\n",df_dropped_rows)

df_dropped_columns  = df.dropna(axis=1)
print("DataFrame with dropped columns: \n ",df_dropped_columns) #jun jun column ma null value xaina tyo drop / show.

#fillings
# ffill = forward fill so it will fill the none value with previous value
# bfill = backward fill so it will fill the none value with after/behind value
df_filled_ffill = df.fillna(method='ffill')
print("datframe with forward fill :\n",df_filled_ffill)

df_filled_bfill = df.fillna(method='bfill')
print("dataframe with backward fill :\n",df_filled_bfill)

#selecting rows where city is "parsa"
city = df[df['City']=="parsa"]
print("\n rows where city is Parsa :\n",city)

#EXTRACTING rows whose age > 26 and city is parsa
# city_age = df[(df['City']=="parsa") and (df['Age']>25)]
# print("\n rows where city is Parsa and age greater theb 25  :\n",city_age)

#using query
# subset_query = df.query('Age > 20 and City == "parsa')
# print("\subset query :\n",subset_query)

#JOINING 
df1 = pd.DataFrame( {
    'ID' :[1,2,3,4],
    "Name" :["Smith","Subesh","Ranjan","Amir"]
} )

df2 = pd.DataFrame( {
    'ID':[3,4,5,6],
    "Age" :[25,30,32,37]
})

#inner join
inner_join = pd.merge(df1,df2,on="ID",how='inner')
print("Inner join \n",inner_join)

#left join
left_join = pd.merge(df1,df2,on='ID', how="left")
print("left join:\n",left_join)

#right join
right_join = pd.merge(df1,df2,on='ID' ,how="right")
print("right join :\n",right_join)




