// norm.cdf() method from the scipy.stats library
// x: the value of interest
// loc: the mean of the probability distribution
// scale: the standard deviation of the probability distribution
// stats.norm.cdf(x, loc, scale)

  
import scipy.stats as stats

## Checkpoint 1
temp_prob_1 = stats.norm.cdf(25, 20, 3) - stats.norm.cdf(18, 20, 3)
print(temp_prob_1)

## Checkpoint 2
temp_prob_2 = 1 - stats.norm.cdf(24, 20, 3)
print(temp_prob_2)
