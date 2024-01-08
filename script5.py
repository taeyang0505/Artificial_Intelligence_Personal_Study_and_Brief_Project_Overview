// binom.cdf() method from the scipy.stats library to calculate the cumulative distribution function
// x: the value of interest, looking for the probability of this value or less
// n: the sample size
// p: the probability of success
// binom.cdf(x, n, p)


import scipy.stats as stats

## Checkpoint 1
prob_1 = stats.binom.cdf(3, 10, 0.5) 
print(prob_1)

# compare to pmf code (checkpoint 2)
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))


## Checkpoint 3
prob_2 = 1 - stats.binom.cdf(5, 10, 0.5)
print(prob_2)


## Checkpoint 4
prob_3 = stats.binom.cdf(5, 10, 0.5) - stats.binom.cdf(1, 10, 0.5) 
print(prob_3)

# compare to pmf code (checkpoint 5)
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5))
