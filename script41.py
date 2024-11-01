import pandas as pd
import numpy as np
import codecademylib3
from scipy.stats import chi2_contingency

npi = pd.read_csv("npi_sample.csv")

print(npi.head())
print()

influence_leader_freq = pd.crosstab(npi.influence, npi.leader)
print(influence_leader_freq)
print()

# calculate the chi squared statistic and save it as chi2, then print it:
chi2, pval, dof, expected = chi2_contingency(influence_leader_freq)

print(np.round(expected))
print()
print(chi2)
