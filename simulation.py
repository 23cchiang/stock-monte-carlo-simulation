import numpy as np
import matplotlib.pyplot as plt

## Parameters
S0 = 100        # starting stock price
mu = 0.7        # expected return
sigma = 0.2     # volatility
T = 1           # time in years
dt = 1/252      # time step (daily)
N = int(T/dt)   # number of steps
simulations = 100

# Time array
t = np.linspace(0, T, N)

# Storage for simulated paths
paths = np.zeros((simulations, N))

# Monte Carlo simulation
for i in range(simulations):
        prices = np.zeros(N)
        prices[0] = S0

        for j in range(1, N):
            Z = np.random.normal()

            prices[j] = prices[j-1] * np.exp( (mu - 0.5 *sigma**2) * dt + sigma * np.sqrt(dt) * Z
            )

        paths[i] = prices

# Plot results
plt.figure(figsize=(10, 6))

for i in range(simulations):
    plt.plot(t, paths[i])


plt.title("Monte Carlo Stock Price Siimulation")
plt.xlabel("Time (Years)")
plt.ylabel("Stock Price ($)")

plt.savefig("simulation_result.png")
plt.show()