import matplotlib.pyplot as plt

#Sample data 
x=[1,2,3,4,5]
y = [3,4,5,6,7]
z=[7,24,4,21,10]

#plot with different markers
plt.plot(x,y,marker='s' , linestyle ='-',color='b',label='Square Marker')
# plt.plot(x,y,marker='o' , linestyle ='-',color='b',label='Circle Marker')
plt.plot(x,[i-1 for i in y],marker='^',linestyle='--',color='r',label='Traingle Marker')
plt.plot(x,z,color=(0,1,0.2,0.5),marker='^',linestyle='solid',label='RGB Line')

#add tittle and labels
plt.title('Plot with different markers')
plt.xlabel('this is x axis')
plt.ylabel('this is x axis')

#show legend
plt.legend()
plt.grid(True,axis='x',linestyle='--',linewidth='0.7',color='blue')
plt.grid(True,axis='y',linestyle='--',linewidth='0.5',color='red')
#display the plot
plt.show()