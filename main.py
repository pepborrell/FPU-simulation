import numpy as np

def acc (qi):
    # Parameter values
    alpha0 = 1
    beta0 = 2

    alpha = alpha0/3
    beta = beta0/4
    fa = lambda r : -r - alpha*r**2 - beta*r**3
    a = fa(qi)

    return a

def vverlet_step (x, v, dt, i):
    aux_acc = acc(x[i])
    x[i+1] = x[i] + v[i]*dt + 0.5*aux_acc*dt**2
    aux_acc_dt = acc(x[i+1])
    v[i+1] = v[i] + 0.5*(aux_acc + aux_acc_dt)*dt


def vverlet (x, v, dt, time):
    for i in range(time-1):
        vverlet_step(x, v, dt, i)

def main():
    time = 100
    dt = 1e-7
    size = 10
    x = np.zeros((time, size))
    v = np.zeros((time, size))

    # Initial conditions
    x[0, 0] = 1.0
    v[0, 0] = 2.0

    vverlet(x, v, dt, time)

    print(x[-1])

main()
