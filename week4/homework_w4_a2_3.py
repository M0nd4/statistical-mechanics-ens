import math, pylab
 
def Vol1_s(dimension):
    return (math.pi ** (dimension / 2.0))/ math.gamma(dimension / 2.0 + 1.0)
 
xs = [x for x in range(1, 200)]
ys = [Vol1_s(d) for d in xs]
 
line, = pylab.plot(xs, ys, '-', linewidth=2)
pylab.grid(True)
pylab.gca().set_yscale('log')
pylab.xlabel('Dimension, d')
pylab.ylabel('$Volume_d$')
pylab.title('Volume of unit hypersphere varying dimensions')
pylab.savefig('hypersphere_volumes.png')
pylab.show()
 
print '5D  ', Vol1_s(5)
print '20D ', Vol1_s(20)
print '200D', Vol1_s(200)
