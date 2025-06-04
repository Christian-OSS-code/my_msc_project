import numpy as np
import matplotlib.pyplot as plt

# Parameters
B0 = 7.0  # Magnetic field strength in Tesla
T2_classical = 50e-3  # Classical T2 relaxation time in seconds (50 ms)
gamma = 42.58e6  # Gyromagnetic ratio (Hz/T)
c = 3e8  # Speed of light (m/s)
M0 = 1.0  # Initial magnetization

# Relativistic correction term (proportional to B0^3/c^2)
alpha = (gamma**2 * B0**3) / (8 * c**2)  # Additional decay rate from FW corrections

# Time array (0 to 150 ms)
t = np.linspace(0, 150e-3, 1000)  # Time in seconds

# Solutions
Mx_classical = M0 * np.exp(-t / T2_classical)  # Standard Bloch decay
Mx_relativistic = M0 * np.exp(-t * (1/T2_classical + alpha))  # FW-corrected decay

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t * 1e3, Mx_classical, '--', label='Standard Bloch Solution', linewidth=2)
plt.plot(t * 1e3, Mx_relativistic, '-', label='FW-Corrected (Relativistic)', linewidth=2)

# Highlight phase deviation at t=100 ms (inset example)
plt.annotate('Δφ > 0.7 rad', xy=(100, 0.15), xytext=(110, 0.3),
             arrowprops=dict(facecolor='red', shrink=0.05), color='red')

# Formatting
plt.xlabel('Time (ms)', fontsize=12)
plt.ylabel('$M_x$ (a.u.)', fontsize=12)
plt.title('Relativistic vs. Classical Transverse Magnetization Decay at 7T', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(0, 1.1)
plt.xlim(0, 150)
plt.show()