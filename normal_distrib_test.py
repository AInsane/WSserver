
import matplotlib.pyplot as plt
import numpy as np


mu, sigma = 0, 1

s = np.random.normal(mu, sigma, 1000)
# Really didn`t find how to get 95% of all numbers (think that they arebetween -2 and 2 ...)
for i in s:
    if i >= -2 and i <= 2:
        print(i)

print(dir(s))

print(abs(mu - np.mean(s)) < 0.01)


count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp(-(bins - mu)**2 / (2 * sigma**2)),
         linewidth=2, color='r')

plt.show()