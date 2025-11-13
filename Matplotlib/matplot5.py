import matplotlib.pyplot as plt

#Pie Chart

labels = ['BCA','BIM','CSIT','DIPLOMA','BHM']
sizes = [31,27,48,59,22]
colors = ['gold','blue','green','pink','red']
explode = (0.2,0,0,0,0)

plt.pie(sizes,explode=explode, labels=labels,colors=colors,autopct='%1.1f%%',shadow=True)
plt.title('Distribution of students across Faculty')
plt.show()

