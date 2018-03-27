import matplotlib.pyplot as plt
from math import log

# Input
colors=["#0000FF", "#00FF00", "#FF0066"]
front = [42,32,22]
rear = [12,14,16,18,21,24,28,32]


# List of gears
gears = []
for i in range(len(front)):
    for j in range(len(rear)):
        gears.append((front[i], rear[j], front[i]/rear[j], colors[i]))

gears.sort(key=lambda x: x[2])

for g in gears:
    print(g)
print('')


# Plot
X = list(range(len(gears)))
ratio = [g[2] for g in gears]
colors = [g[3] for g in gears]

fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(len(X)):
    ax.scatter(X[i], ratio[i], color=colors[i])

plt.show()
