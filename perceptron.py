"""Perceptron with Hebb rules."""
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
alpha = 0.1  # Learning Factor
gamma = 0.2  # Forgetting Factor

for epoch in range(150):
    n = (w0 * p0) + (w * p) + (b * 1)
    a = hardlim(np.array([n]))
    print('W:', w)
    print('Sum:', alpha * a[0] * p)
    print('Minus:', gamma * w)
    w = w + (alpha * a[0] * p) - (gamma * w)
    print('W new:', w)
    # w = w + (alpha * a[0] * p) - (gamma * w * a[0])
    if epoch > 10 and epoch < 60:
        p0 = 1
        p = 1
    else:
        p0 = 0
        p = 1
    plt.plot(epoch, w, '*r')
    plt.pause(0.1)

plt.show()

"""
The difference between the equation 1

    w = w + (alpha * a[0] * p) - (gamma * w)

and the equation 2

    w = w + (alpha * a[0] * p) - (gamma * w * a[0])

is that the first one the gamma limits the w in a factor of alpha/gamma,
but if you don't present the data starts to forgot the data structure. In
the second one the gamma also limits the w but only when the neuron is active
so the neuron won't forget the data structure if you don't present the data.
"""
