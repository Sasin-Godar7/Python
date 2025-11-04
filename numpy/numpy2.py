import numpy as np
#dataset creation
#generate sales data:10 employee, 7days
sales_data = np.random.randint(50,500,size=(10,7))
print("sales data :\n",sales_data)
#step2: total sales for each employee
total_sales = np.sum(sales_data,axis=1)                 # each employee ko daily ko total sales jun hunxa row wise so axis =1
print("\n total sales per employee :",total_sales)


#step3: average daily sales

average_daily_sales = np.mean(sales_data,axis=0)     # each employee ko daily ko sales i.e sunday to saturady is colum of days so axis=0 
print("aveage sales per day :",average_daily_sales)

#step4: increase sales by 10%
increase_sales  = sales_data*1.10
print("\n sales after 10% increase :\n",increase_sales)

#step5 : data manipulation (extract data for the first five employees)
first_five_employee = sales_data[ : 5, :]
print("\n sales data for the first five employee :\n",first_five_employee)

#step6: employee with total sales > 2000
high_performers = total_sales >2000
print("\n high performer(total sales > 2000) :",np.where(high_performers)[0])   #kun kun index ko employee ho tyo dekhauna lai

#step7 :statistical analysis
mean_sales = np.mean(sales_data)
median_sales = np.median(sales_data)
std_dev_sales = np.std(sales_data)
print("\n overall mean sales:",mean_sales)
print("\n overall median sales :",median_sales)
print("\n overall standerd deviation of sales :",std_dev_sales.round(2))

