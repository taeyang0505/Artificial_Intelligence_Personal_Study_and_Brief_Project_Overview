// poisson.rvs() method in the scipy.stats library to generate random values
# generate random variable
# stats.poisson.rvs(lambda, size = num_values)
// rvs = stats.poisson.rvs(10, size = 1000)


import scipy.stats as stats
import codecademylib3

from histogram_function import histogram_function

## Checkpoint 1
# lambda = 15, 1000 random draws 
rand_vars = stats.poisson.rvs(15, size = 1000)

## Checkpoint 2
# print the mean of rand_vars
print(rand_vars.mean())

## Checkpoint 3
histogram_function(rand_vars)
