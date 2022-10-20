import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = 4 + 2 * np.sin(2 * x)
z = 4 + 2 * np.cos(2 * x)
#w = 4 + 2 * np.tan(2 * x)
plt.plot(x, y, linewidth=2.0)
plt.plot(x, z, linewidth=2.0)
#plt.plot(x, w, linewidth=2.0)
plt.show()