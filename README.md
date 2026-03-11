# Monte Carlo Stock Price Simulation
This project simulates stock price paths using **Geometric Brownain Motion** and **Monte Carlo simulation**, a method widely used in quantitative finance.

## Model
The stock price follows the stochastic progess:
S(t+1) = S(t) * exp((μ - 0.5σ²)Δt + σ√Δt Z)

where:
- μ = expected return
- σ = volatility
- Z = standard normal random variable

## Technologies

- Python
- NumPy
- Matplotlib

## Example Output

The simulation generates multiple possible stock price paths.

![Simulation Output](simulation_results.png)