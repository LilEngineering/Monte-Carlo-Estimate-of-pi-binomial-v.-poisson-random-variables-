from math import comb, exp, factorial
import matplotlib.pyplot as pl

#given values 
n, p = 100, 0.01

lamb = n * p #fun fact p is what i was also using to call matplot for a while ...

k = range(6) #python index start at 0 (bless) -> 0,1,2,3,4,5 is the range)

#both looped for i in range 0,1,...,5
biPmf = [comb(n,i) * (p**i) * ((1-p)**(n-i)) for i in k] #binomial
poPmf = [exp(-lamb) * (lamb**i) / factorial(i) for i in k] #poisson

#graph it up
pl.plot (k, biPmf, marker = 'o', label = 'binom')
pl.plot (k, poPmf, marker = 'o', label = 'poss')
pl.legend()
pl.show()

