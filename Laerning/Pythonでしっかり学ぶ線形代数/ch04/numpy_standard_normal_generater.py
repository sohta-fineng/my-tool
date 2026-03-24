import numpy as np

rng = np.random.default_rng()

samples1 = rng.standard_normal(1)
samples2 = rng.standard_normal(10)
samples3 = rng.standard_normal(100)
samples4 = rng.standard_normal(1000)

print(samples1.mean(), samples2.mean(), samples3.mean(), samples4.mean(), sep = " \n")