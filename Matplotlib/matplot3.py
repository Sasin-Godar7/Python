import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1,4,6,8,10]
y3 = [7,24,4,21,10]
y4 = [1,3,5,7,9]

fig,axs = plt.subplots(2,2,figsize=(10,8))

# First SubPlot
axs[0,0].plot(x,y1,marker = 'o',linestyle = '-', color = 'blue')
axs[0,0].set_title("Subplot 1")
axs[0,0].set_xlabel('X-axis')
axs[0,0].set_ylabel('Y-axis')

# Second SubPlot
axs[0,1].plot(x,y2,marker = 'o',linestyle = '-', color = 'blue')
axs[0,1].set_title("Temperature Census")
axs[0,1].set_xlabel('Months')
axs[0,1].set_ylabel('Degrees')

# Third SubPlot
axs[1,0].plot(x,y3,marker = 'o',linestyle = '-', color = 'blue')
axs[1,0].set_title("Sales Census")
axs[1,0].set_xlabel('Months')
axs[1,0].set_ylabel('Sales Amount')

# Fourth SubPlot
axs[1,1].plot(x,y4,marker = 'o',linestyle = '-', color = 'blue')
axs[1,1].set_title("Health")
axs[1,1].set_xlabel('Season')
axs[1,1].set_ylabel('Patient count')

plt.tight_layout()
plt.show()