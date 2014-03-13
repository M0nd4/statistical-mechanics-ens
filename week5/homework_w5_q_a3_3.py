import pylab
import numpy as np
 
def Energy(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)
 
cubic = -0.5
quartic = -cubic
 
x = np.linspace(0, 1)
y = Energy(x, cubic, quartic)
pylab.plot(x, y, label='Energy')
 
pylab.title('Energy for particle at varied perturbation corrections\n(cubic = -0.5, quartic = 0.5)')
pylab.xlabel('Perturbation corrections')
pylab.ylabel('Energy')
pylab.savefig('particle_energy_varying_position_a3_3.png')
#pylab.show()
