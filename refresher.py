# this is a refresher on matplotlib knowledge

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [22, 33, 44, 55, 66]

plt.plot(x, y)
plt.legend('the legend')
plt.title('the heading of the plot')

plt.xlabel('x line')
plt.ylabel('y line')

print(plt.show())
