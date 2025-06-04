import numpy as np
import matplotlib.pyplot as plt

B0 = np.linspace(1, 10, 20)  # Tesla
grad_B = np.linspace(0, 100, 20)  # mT/m
B0_grid, grad_grid = np.meshgrid(B0, grad_B)

# Example: Pauli approximation Δω (simplified)
delta_omega = (42.58e6 * B0_grid**2 * grad_grid) / (2 * (1.67e-27)**2 * (3e8)**2)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(B0_grid, grad_B, delta_omega, cmap='viridis')
ax.set_xlabel('B₀ (Tesla)')
ax.set_ylabel('∇B (mT/m)')
ax.set_zlabel('Δω (Hz)')
ax.set_title('Pauli Δω vs. B₀ and Gradients')
plt.savefig('3d_frequency_shift.png', dpi=300)
plt.show()