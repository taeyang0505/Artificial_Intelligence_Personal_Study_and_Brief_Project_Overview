// binom.pmf() method from the scipy.stats library can be used to calculate the PMF of the binomial distribution at any value
// x: the value of interest
// n: the number of trials
// p: the probability of success


import scipy.stats as stats

# value of interest
# change this
x = 3

# sample size
# change this
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print(prob_1)

## Question 2
prob_2 = stats.binom.pmf(7, 20, 0.5)
print(prob_2)
