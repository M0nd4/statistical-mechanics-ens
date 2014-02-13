import math, pylab, numpy

xs = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
ys = [0.4049348561784662, 
      0.2938066263645426, 
      0.19526444290538125, 
      0.14190105093418606, 
      0.10233515331951122, 
      0.07317285193683096, 
      0.051243445388703346, 
      0.036731364324109096, 
      0.024419130594434648]

est1 = [x ** -0.5 for x in xs]
est2 = [x ** -0.48 for x in xs]
pylab.plot(xs, ys, 'o')
pylab.plot(xs, est1, '<')
pylab.plot(xs, est2, '^')
pylab.gca().set_xscale('log')
pylab.gca().set_yscale('log')
pylab.xlabel('n_trials')
pylab.ylabel('$\sigma$')
pylab.show()
