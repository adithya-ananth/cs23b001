import numpy as np
import matplotlib.pyplot as plt

data = [1,0,1,0,1,1,0]
data_new = np.array([-1 if i == 0 else 1 for i in data])
message = np.repeat(data_new, 200)
