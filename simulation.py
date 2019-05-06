from tools import *

time = 10000
dt = 1e-3
size = 20
x = np.zeros((time, size))
v = np.zeros((time, size))

# Initial conditions
x[0, 1] = 1.0
v[0, 1] = 0.0

vverlet(x, v, dt, time)


# Plotting
t = np.arange(0, time)
fig, ax = plt.subplots(nrows = 5, ncols = 4)
i = 0
for axi in ax:
    for axij in axi:
        axij.plot(t, x[:, i])
        i += 1
plt.show()
