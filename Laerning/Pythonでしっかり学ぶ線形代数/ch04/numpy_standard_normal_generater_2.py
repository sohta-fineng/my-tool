import numpy as np

rng = np.random.default_rng()

sizes = [1, 10, 100, 1000]

for s in sizes:
    sample = rng.standard_normal(s)
    print(f"Size {s:4}: Mean = {sample.mean():6f}")