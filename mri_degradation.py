import numpy as np
import matplotlib.pyplot as plt

B0 = np.array([1, 3, 7, 10])
snr_loss = np.array([0.001, 0.01, 1.0, 3.0])  # SNR loss in %

plt.figure(figsize=(10, 6))
plt.plot(B0, snr_loss, 'm-*', markersize=10, linewidth=2)
plt.xlabel('Magnetic Field (Tesla)', fontsize=12)
plt.ylabel('SNR Loss (%)', fontsize=12)
plt.title('Relativistic SNR Degradation in MRI', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(B0)
plt.show()