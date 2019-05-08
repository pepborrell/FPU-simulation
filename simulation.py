from tools import *

# SIMULATION PARAMETERS

# Total time = time*dt
time = 10000
dt = 1e-3

#"Time checkpoints"
tc = [0,1000]

#Size of the system / number of particles
N = 100

# Potential parameters
alpha = -1.0
beta = 2.0
pot_par = (alpha,beta)

# Initial conditions
x = np.zeros(N)
v = np.zeros(N)
for i in range(10):
    x[i] = 10.0*(-1)**i


# SIMULATION: CALCULATION AND PLOT
E = vverlet(x, v, dt, time, pot_par, tc)

k = np.arange(N) + 1
fig, ax = plt.subplots(nrows = np.shape(E)[0])
i = 0
for axi in ax:
    axi.plot(k, E[i,:])
    i += 1
plt.show()


# Calculate Ek for 1 <= k <= N
# Plot Ek w.r.t. k
# Repeat for different values of time
