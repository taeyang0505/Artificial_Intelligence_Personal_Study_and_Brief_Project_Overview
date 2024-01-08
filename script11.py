// For the Poisson distribution, the variance is simply the value of lambda (λ), meaning that the expected value and variance are equivalent in Poisson distributions
// We can calculate the variance of a sample using the numpy.var() method

  // import scipy.stats as stats
  // import numpy as np

  // rand_vars = stats.poisson.rvs(4, size = 1000)
  // print(np.var(rand_vars))

// print the minimum and maximum values observed using the .min() and .max() Python functions

  // import scipy.stats as stats
  // rand_vars = stats.poisson.rvs(4, size = 1000)
  // print(min(rand_vars), max(rand_vars))
  

import scipy.stats as stats
import numpy as np

## For checkpoints 1 and 2
# 5000 draws, lambda = 7
rand_vars_7 = stats.poisson.rvs(7, size = 5000)

## Checkpoint 1
# print variance of rand_vars_7
print(np.var(rand_vars_7))

## Checkpoint 2
# print minimum and maximum of rand_vars_7
print(min(rand_vars_7), max(rand_vars_7))

## For checkpoints 3 and 4
# 5000 draws, lambda = 17
rand_vars_17 = stats.poisson.rvs(17, size = 5000)

## Checkpoint 3
# print variance of rand_vars_17
print(np.var(rand_vars_17))

## Checkpoint 4
# print minimum and maximum of rand_vars_17
print(min(rand_vars_17), max(rand_vars_17))
