// norm.cdf() method from the scipy.stats library
// x: the value of interest
// loc: the mean of the probability distribution
// scale: the standard deviation of the probability distribution

import scipy.stats as stats

prob = stats.norm.cdf(175, 167.64, 8)
print(prob)
