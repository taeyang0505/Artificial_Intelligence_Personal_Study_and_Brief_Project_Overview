/ expected value = 10, probability of observing 6
// stats.poisson.pmf(6, 10)

import scipy.stats as stats

## Checkpoint 1
# calculate prob_15
prob_15 = stats.poisson.pmf(15, 15)
print(prob_15)


## Checkpoint 
# calculate prob_7_to_9
prob_7_to_9 = stats.poisson.pmf(7, 15) + stats.poisson.pmf(8, 15) + stats.poisson.pmf(9, 15)
print(prob_7_to_9)
