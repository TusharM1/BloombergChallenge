import matplotlib.pyplot as plt
 
# Data to plot
labels = ['Python', 'C++', 'Ruby', 'Java']
sizes = [504, 337, 415, 280]
labels_gender = ['Man','Woman','Man','Woman','Man','Woman','Man','Woman']
sizes_gender = [315,189,125,212,270,145,190,90]
# colors = ['#ff6666', '#ffcc99', '#99ff99', '#66b3ff']
# colors_gender = ['#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6']
 
# Plot
plt.pie(sizes, labels=labels,frame=True)
plt.pie(sizes_gender,radius=0.75,)
centre_circle = plt.Circle((0,0),0.5,color='black', fc='white',linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
 
plt.axis('equal')
plt.tight_layout()
plt.show()