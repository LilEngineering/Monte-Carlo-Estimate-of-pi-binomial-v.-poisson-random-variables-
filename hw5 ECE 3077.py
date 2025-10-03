import numpy as n
import matplotlib.pyplot as p

def monte_carlo_estimate (N, tr = int(10**6)):
    z = (n.random.rand(tr, N)**2 + n.random.rand(tr, N)**2 <= 1)
    zBar = z.mean(axis = 1)
    wn = 4 * zBar
    return wn

for i in [100,1000]:
    wn = monte_carlo_estimate(i)
    mu = n.mean(wn)
    sigma = n.std(wn)

    p.hist(wn, bins=20, density=True, alpha=0.7, edgecolor="black")

    for k in range (1,4): 
        std = k*sigma:0.2f 
        p.axvline(mu + k*sigma, color="blue", linestyle="-",
        linewidth=1, label = f'+{k} Std Dev: {mu + std}')
        
        p.axvline(mu - k*sigma, color="red", linestyle="-",
        linewidth=1, label = f'-{k} Std Dev: {mu - std}')

    p.axvline(mu, color="black", linestyle="--", label=f"mean = {mu:.4f}")
    p.title(f"Monte Carlo Estimate when N = {i}")
    p.legend()
    p.show()

