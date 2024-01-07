// Probability Mass Function Over a Range using Python

import scipy.stats as stats

## Checkpoint 1
prob_1 = stats.binom.pmf(4, n=10, p=0.5) + stats.binom.pmf(5, n=10, p=0.5) + stats.binom.pmf(6, n=10, p=0.5)
print(prob_1)

## Checkpoint 2
prob_2 = 1 - stats.binom.pmf(0, n=10, p=0.5) - stats.binom.pmf(1, n=10, p=0.5) - stats.binom.pmf(2, n=10, p=0.5)
print(prob_2)
