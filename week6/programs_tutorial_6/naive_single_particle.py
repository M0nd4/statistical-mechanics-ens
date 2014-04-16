Emax = 50
States = []
for E_x in range(Emax):
    for E_y in range(Emax):
        for E_z in range(Emax):
            States.append(((E_x + E_y + E_z), (E_x, E_y, E_z)))
States.sort()
for k in range(50):
    print '%3d' % k, States[k][0], States[k][1]
