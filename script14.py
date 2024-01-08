// The expected value of two independent random variables is the sum of each expected value separately
# E(X+Y) = E(X) + E(Y)

// Multiplying a random variable by a constant a changes the expected value to be a times the expected value of the random variable
# E(aX) = a * E(X)

// Adding a constant a to the distribution changes the expected value by the value a
# E(X+a) = E(X) + a

// Increasing the values in a distribution by a constant a does not change the variance
# Var(X+a) = Var(X)

// Scaling the values of a random variable by a constant a scales the variance by the constant squared
# Var(aX) = a^2 * Var(X)

// The variance of the sum of two random variables is the sum of the individual variances
# Var(X+Y) = Var(X) + Var(Y)

## This principle ONLY holds if the X and Y are independent random variables
  
import scipy.stats as stats
import numpy as np

## Checkpoint 1
expected_bonus = 0.08 * 75000
print(expected_bonus)

## Checkpoint 2
num_goals = stats.poisson.rvs(4, size = 100)

## Checkpoint 3
print(np.var(num_goals))

## Checkpoint 4
num_goals_2 = 2 * num_goals
print(np.var(num_goals_2))
