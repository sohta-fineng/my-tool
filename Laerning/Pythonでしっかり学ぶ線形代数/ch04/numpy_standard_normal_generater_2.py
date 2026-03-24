import numpy as np

rng = np.random.default_rng()

samples1 = rng.standard_normal(1)
samples2 = rng.standard_normal(10)
samples3 = rng.standard_normal(100)
samples4 = rng.standard_normal(1000)

print(samples1.mean(), samples2.mean(), samples3.mean(), samples4.mean(), sep = " \n")


sizes = [1, 10, 100, 1000]

for s in sizes:
    sample = rng.standard_normal(s)
    print(f"Size {s:4}: Mean = {sample.mean():6f}")