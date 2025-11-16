# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# #Heart co-ordinates

# t = np.linspace(0,2*np.pi,1000)
# x = 16 * np.sin(t)** 3 # double * denotes power
# y = 13 * np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

# #Setup Figure 
# fig,ax = plt.subplots(figsize=(6,6))
# ax.set_aspect('equal')
# ax.axis('off')



# #empty plot elements
# line, =ax.plot([],[],color='red',linewidth=3)
# fill = None
# text = ax.text(0,0,"",color='red',fontsize=22,fontweight = 'bold',ha='center',va='center')

# #update function for animation
# def update(frame):
#     global fill 

#     if frame <len(x):
#         line.set_data(x[:frame],y[:frame])

#     if frame == len(x):
#         fill = ax.fill(x,y,color='pink',alpha = 0.6)    

#     if frame > len(x):
#         alpha = min( (frame-len(x)) / 30,1) 
#         text.set_text("Love You ")
#         text.set_alpha(alpha)
#         return line,text

# total_frame = len(x) + 40
# ani = FuncAnimation(fig,update,frames=total_frame,interval=10,blit=False,repeat=False)
# plt.show()




import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Heart coordinates
t = np.linspace(0, 2*np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

# Setup figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.axis('off')

# Empty elements
line, = ax.plot([], [], color='red', linewidth=3)
text = ax.text(0, 0, "", color='red', fontsize=22, fontweight='bold', ha='center', va='center')

fill = None

# Update function
def update(frame):
    global fill

    if frame < len(x):
        line.set_data(x[:frame], y[:frame])

    elif frame == len(x):
        fill = ax.fill(x, y, color='pink', alpha=0.6)

    else:
        alpha = min((frame - len(x)) / 30, 1)
        text.set_text("Love You")
        text.set_alpha(alpha)

    return line, text

total_frames = len(x) + 40
ani = FuncAnimation(fig, update, frames=total_frames, interval=10, blit=False)
plt.show()

