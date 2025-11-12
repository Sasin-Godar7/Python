
import matplotlib.pyplot as plt
#create a figure
#simple data
x=[1,2,3,4,5]
y=[2,4,6,8,12]
z=[7,24,4,21,10]

plt.figure(figsize = (10,5))
#First Subplot
plt.subplot(1,2,1)
plt.plot(x,y,marker='o',linestyle = '-',color = 'blue')
plt.title('Subplot 1')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

#Second Subplot
plt.subplot(3,4,5)
plt.plot(x,y,marker='^',linestyle = '--',color = 'red')
plt.title('Subplot 2')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.tight_layout()
plt.show()