import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def relativistic_bloch(M, t, gamma, T1, T2, M0, B0, c):
    Mx, My, Mz = M

    # Standard Bloch terms
    dMxdt = gamma * My * B0 - Mx / T2
    dMydt = -gamma * Mx * B0 - My / T2
    dMzdt = -(Mz - M0) / T1  # No relativistic correction for Mz

    # Relativistic correction (FW transformation term)
    relativistic_correction = (gamma ** 2 * B0 ** 2) / (8 * c ** 2)
    dMxdt += relativistic_correction * Mx
    dMydt += relativistic_correction * My

    return [dMxdt, dMydt, dMzdt]


# Parameters (protons)
gamma = 42.58e6  # Gyromagnetic ratio (Hz/T)
T1 = 1000e-3  # Longitudinal relaxation (s)
T2 = 50e-3  # Transverse relaxation (s)
M0 = 1.0  # Equilibrium magnetization
B0 = 7.0  # Magnetic field (T)
c = 3e8  # Speed of light (m/s)

# Initial magnetization [Mx, My, Mz]
M_initial = [0.0, 0.0, M0]

# Time points (0 to 200 ms)
t = np.linspace(0, 0.2, 1000)

# Solve the ODE
solution = odeint(relativistic_bloch, M_initial, t, args=(gamma, T1, T2, M0, B0, c))
Mx, My, Mz = solution[:, 0], solution[:, 1], solution[:, 2]

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(t * 1000, Mx, label='$M_x$')
plt.plot(t * 1000, My, label='$M_y$')
plt.plot(t * 1000, Mz, label='$M_z$')
plt.xlabel('Time (ms)')
plt.ylabel('Magnetization')
plt.title('Relativistic Bloch Solutions ($B_0 = 7$ T)')
plt.legend()
plt.grid(True)
plt.show()