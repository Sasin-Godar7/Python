import matplotlib.pyplot as plt

#vertical bar graph 
catagories = ['A','B','C','D','E']
values = [3,7,2,5,4]

plt.bar(catagories,values,color='skyblue' , edgecolor='black',linewidth=1.2)
plt.title("Custpmized bar graph")
plt.xlabel("Catagories")
plt.ylabel("Values")

plt.grid(True,axis='y',linestyle ='--' , linewidth=0.7)
plt.show()


#horizontal bar graph 
catagories = ['BCA','BIM','CSIT','DIPLOMA','BHM']
values = [31,27,48,59,22]

plt.bar(catagories,values,color='orange' , edgecolor='black',linewidth=1.2)
plt.title("Horizontal bar graph")
plt.xlabel("Catagories")
plt.ylabel("Values")

plt.grid(True,axis='x',linestyle ='--' , linewidth=0.7)
plt.show()




semester =['2nd','4th','6th','8th']
boys = [21,17,19,11]
girls = [11,18,14,19]

x =range(len(semester))
plt.bar(x,boys,width=0.4,label='Boys',color='skyblue',align='center')
plt.bar(x,girls,width=0.4, label='Girls' , color = 'pink', align='edge')

plt.title('Number of boys vs girls')
plt.xlabel("Semesters")
plt.ylabel("Number of students")

plt.xticks(x,semester)
plt.legend()
plt.show()



