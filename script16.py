import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 7

## Task 2:
print(stats.poisson.pmf(lam, lam))

  # probability of observing exactly

## Task 3:
print(stats.poisson.cdf(4, lam))

  # having 4 or fewer defects on a given day

## Task 4:
print(1 - stats.poisson.cdf(9, lam))

  # having more than 9 defects on any given day

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam, size = 365)

  # year_defects that has 365 random values from the Poisson distribution

## Task 6:
print(year_defects[0:20])

  # the first 20 values in this data set

## Task 7:
print(lam*365)

  # lambda defects on a given day, the number of defects we would expect over a 30-day month would be:

## Task 8:
print(sum(year_defects))

  # total sum of the data set year_defects

## Task 9:
print(np.mean(year_defects))

  # the average number of defects across all days

## Task 10:
print(year_defects.max())

  # If the data set were called month_defects, we could print the maximum value by using

## Task 11:
print(1 - stats.poisson.cdf(year_defects.max(), lam))

  # the probability of observing that value or greater using: 1 - stats.poisson.cdf(29, 10)

### Extra Bonus ###
# Task 12
print(stats.poisson.ppf(0.9, lam))  

  ## nth percentile of the Poisson(7) distribution
  # stats.poisson.ppf(percentile, lambda)
  # percentile is equal to the desired percentile (a decimal between 0 and 1)
  # lambda is the lambda parameter of the Poisson distribution

# Task 13

print(sum(year_defects >= stats.poisson.ppf(0.9, lam)) / len(year_defects))

  // to get the proportion of days that have more than 20 defects
