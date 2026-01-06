import numpy as np
import matplotlib.pyplot as plt

data = [1,0,1,0,1,1,0]
data_new = np.array([-1 if i == 0 else 1 for i in data])
message = np.repeat(data_new, 200)

# Carrier signal
fc = 20

N = 7 * 200
T = 7

t = np.linspace(0, T, N, endpoint = False)

carrier_signal = np.cos(2* np.pi * fc * t)

# Amplitude Modulation
mod_index = 0.8

am_signal = message * carrier_signal
