import numpy as np
import matplotlib.pyplot as plt

def acc(q, pot_par):
    # Parameter values for the potential
    alpha0 = pot_par[0]
    beta0 = pot_par[1]

    alpha = alpha0/3
    beta = beta0/4
    fa = lambda r : -r - alpha*r**2 - beta*r**3
    q1 = np.roll(q, 1)
    dif_q = q - q1
    a = np.zeros(len(q))
    a += fa(dif_q)
    q1 = np.roll(q, -1)
    dif_q = q - q1
    a += fa(dif_q)
    a[0] = a[-1] = 0

    return a

def vverlet_step(x, v, dt, pot_par):
    aux_acc = acc(x, pot_par)
    x = x + v*dt + 0.5*aux_acc*dt**2
    aux_acc_dt = acc(x, pot_par)
    v = v + 0.5*(aux_acc + aux_acc_dt)*dt

# Pre: x and v contain the initial conditions for position and velocity of each particle
# Post: x and v contain the position and velocity for each particle at time time*dt
# Retorna una matriu amb l'energia de cada mode per cada temps de tc 
def vverlet(x, v, dt, time, pot_par, tc):
    E = np.zeros((len(tc),len(x))) # matrix: time checkpoints x number of modes
    for t in range(time+1): #+1 per tenir els valors en time
        vverlet_step(x, v, dt, pot_par)
        if t in tc:
            E[tc.index(t)] = calc_Ek(x,v)
    return E

# Pk: cridar amb v = velocitats
# Qk: cridar amb v = q = posicions
def aux_calc_Ek(v):
    N = len(v)
    res = np.zeros(N)
    k = np.arange(N) + 1
    for i in range(1,N+1):
        res = res + v*np.sin(np.pi*k*i/(N+1))
    res = res * np.sqrt(2/(N+1))
    return res
    
# q = vector posicions (respecte equilibri)
# v = vector velocitats
def calc_Ek(q,v):
    N = len(q)
    k = np.arange(N) + 1
    wk = 2*np.sin(np.pi*k/(2*N+2))
    Pk = aux_calc_Ek(v)
    Qk = aux_calc_Ek(q)
    Ek = Pk**2 + wk**2 * Qk**2
    return Ek/2
