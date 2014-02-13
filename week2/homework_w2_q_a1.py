import random, pylab

def direct_disks_box(N, sigma):
    overlap = True
    while overlap == True:
        L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
        for k in range(1, N):
            a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
            min_dist_sq = min(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L) 
            if min_dist_sq < 4.0 * sigma ** 2: 
                overlap = True
                break
            else:
                overlap = False
                L.append(a)
    return L

N = 4
sigma = 0.1196
n_runs = 1000000
histo_data = []
for run in range(n_runs):
    pos = direct_disks_box(N, sigma)
    [histo_data.append(pos[k][0]) for k in range(N)]

pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('x location')
pylab.ylabel('frequency (bucketed)')
pylab.title('Distribution of disks along the x-axis by frequency. Question A1')
pylab.grid()
pylab.savefig('direct_disks_histo.png')
pylab.show()
