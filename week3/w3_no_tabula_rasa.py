import random
 
N     = 3
L     = 1.0
sigma = 0.01
short_L = L - (2 * N * sigma)   # length of line without the widths of the pegs
 
# positions of pegs' centrepoints on the short line
short_pos = sorted(random.uniform(0, short_L) for _ in range(N))
# positions scaled to the real L (length) of the line
long_pos  = [pos + (2 * i + 1) * sigma for i, pos in enumerate(short_pos)]
 
print long_pos
