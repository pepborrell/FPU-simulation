from tools import *

# SIMULATION PARAMETERS

# Total time = time*dt
time = 10000000
dt = 1e-1

#"Time checkpoints"
tc = [0,1000,10000,100000,200000,400000,500000,1000000,1500000,2000000,
        5000000,10000000]

#Size of the system / number of particles
N = 100

# Potential parameters
alpha = -1.0
beta = 2.0
pot_par = (alpha,beta)

# Initial conditions
# x[0] and x[-1] must be zero at all times
# idem for v[0] and v[-1]
#We excite the first mode (n=1)
#Stationary wave y = 2*A*sin(kx), k=2*pi/lambda, lambda=2*L/x, x/L = i/N
v = np.zeros(N+2)
A = 1 # such that the total energy is of the order of N*10^-4
x = np.array([A*np.sin(np.pi*i/(N+1)) for i in range(N+2)])

#initial energy per mode
#k = np.arange(N) + 1
#plt.plot(k,calc_Ek(x,v))
#plt.show()

# SIMULATION: CALCULATION AND PLOT
E = vverlet(x, v, dt, time, pot_par, tc)

k = np.arange(N) + 1
for i in range(E.shape[0]):
    fig, ax = plt.subplots()
    print("E total at time {}: {}".format(tc[i],np.sum(E[i,:])))
    ax.plot(k,E[i,:]) #, linefmt=':', markerfmt='C0.')
    ax.set_yscale('log')
    plt.savefig('./plots/energy_modes_{}.png'.format(tc[i]))