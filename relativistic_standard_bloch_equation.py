from matplotlib import pyplot as plt
from scipy.integrate import odeint

from relativistic import M_initial, t, gamma, T1, T2, M0, B0, Mx


def standard_bloch(M, t, gamma, T1, T2, M0, B0):
    Mx, My, Mz = M
    dMxdt = gamma * My * B0 - Mx / T2
    dMydt = -gamma * Mx * B0 - My / T2
    dMzdt = -(Mz - M0) / T1
    return [dMxdt, dMydt, dMzdt]

solution_std = odeint(standard_bloch, M_initial, t, args=(gamma, T1, T2, M0, B0))
Mx_std, My_std, Mz_std = solution_std[:, 0], solution_std[:, 1], solution_std[:, 2]

plt.figure(figsize=(10, 6))
plt.plot(t * 1000, Mx, '--', label='Relativistic $M_x$')
plt.plot(t * 1000, Mx_std, label='Standard $M_x$')
plt.xlabel('Time (ms)')
plt.ylabel('$M_x$')
plt.title('Relativistic vs. Standard Bloch Solutions')
plt.legend()
plt.grid(True)
plt.show()