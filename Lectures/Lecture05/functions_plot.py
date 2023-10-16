import numpy as np
import matplotlib.pyplot as pyplot

x = np.linspace(0, 2.0*np.pi)

pyplot.plot(x, np.sin(x))
pyplot.plot(x, np.cos(x))
pyplot.plot(x, np.tan(x))

pyplot.axis([0, 2.0*np.pi, -1, 1])
# pyplot.show()

pyplot.savefig('fig.png')
pyplot.savefig('fig.pdf')
