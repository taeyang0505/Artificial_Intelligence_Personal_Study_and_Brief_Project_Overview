// poisson.cdf() method in the scipy.stats library to evaluate the probability of observing a specific number or less given the expected value of a distribution
// expected value = 10, probability of observing 6 or less
// stats.poisson.cdf(6, 10)

import scipy.stats as stats

## Checkpoint 1
# calculate prob_more_than_20
prob_more_than_20 = 1 - stats.poisson.cdf(20, 15) 
print(prob_more_than_20) 

## Checkpoint 
# calculate prob_17_to_21
prob_17_to_21 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15) 
print(prob_17_to_21) 
