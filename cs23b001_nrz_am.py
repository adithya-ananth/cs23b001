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
am_signal = message * carrier_signal

# Plots
# Create a figure with three subplots
plt.figure(figsize=(12, 10))

# Subplot 1: Message Signal
plt.subplot(3, 1, 1)
plt.plot(np.arange(len(message)), message)
plt.title('Message Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid(True)

# Subplot 2: Carrier Signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal)
plt.title(f'Carrier Signal (fc = {fc} Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Subplot 3: AM Modulated Signal
plt.subplot(3, 1, 3)
plt.plot(t, am_signal)
plt.title('AM Modulated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.savefig('amplots.pdf') # Save the figure as amplots.pdf
plt.show()
