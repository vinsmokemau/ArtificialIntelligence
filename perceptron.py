"""."""
import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

hardlim = nl.trans.HardLim()

# No conditional
p0 = 0
w0 = 1

# Conditional
p = 1
w = 0

b = -0.5
alpha = 0.1
gamma = 0.2

for epoch in range(150):
    n = (w0 * p0) + (w * p) + (b * 1)
    a = hardlim(np.array([n]))
    w = w + (alpha * a[0] * p) - (gamma * w)
    if epoch > 10 and epoch < 60:
        p0 = 1
        p = 1
    else:
        p0 = 0
        p = 1
    plt.plot(epoch, w, '*r')
    plt.pause(0.1)

plt.show()
