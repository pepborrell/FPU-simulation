import numpy as np
import matplotlib.pyplot as plt

def acc(q):
    # Parameter values
    alpha0 = 5.0
    beta0 = 5.0

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

def vverlet_step(x, v, dt, i):
    aux_acc = acc(x[i])
    x[i+1] = x[i] + v[i]*dt + 0.5*aux_acc*dt**2
    aux_acc_dt = acc(x[i+1])
    v[i+1] = v[i] + 0.5*(aux_acc + aux_acc_dt)*dt


def vverlet(x, v, dt, time):
    for i in range(time-1):
        vverlet_step(x, v, dt, i)

def calc_Pk(v, N, k):
    
