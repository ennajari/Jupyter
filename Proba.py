from scipy.stats import binom
# Given values
n = 100  # number of trials
p = 0.01  # probability of failure
# Calculate the probabilities
P_X_0 = binom.pmf(0, n, p)
P_X_1 = binom.pmf(1, n, p)
P_X_2 = binom.pmf(2, n, p)
P_X_3 = binom.pmf(3, n, p)
P_X_ge_4 = 1 - binom.cdf(3, n, p)

P_X_0, P_X_1, P_X_2, P_X_3, P_X_ge_4
