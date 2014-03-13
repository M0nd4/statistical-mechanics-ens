import pylab
 
def V(x):
    pot =  x ** 2 / 2 + cubic * x ** 3 + quartic * x ** 4
    return pot
 
cubic = -0.5
quartic = -cubic
x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
y = [V(a) for a in x]
pylab.plot(x, y, label='Anharmonic potentials \n(cubic = -0.5, quartic = 0.5)')
 
cubic = 0.0
quartic = 0.0
y = [V(a) for a in x]
pylab.title('Potential energy for particle at varied x-positions')
pylab.xlabel('x position')
pylab.ylabel('Energy')
pylab.plot(x, y, label='Harmonic potentials')
pylab.legend()
pylab.axis([-4.0, 4.0, 0.0, 3.0])
 
#pylab.show()
pylab.savefig('particle_energy_varying_position_a3_2.png')
