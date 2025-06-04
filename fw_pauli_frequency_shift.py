import matplotlib.pyplot as plt
import numpy as np

# =============================================
# DATA FROM YOUR EQUATIONS (ADJUST NUMBERS IF NEEDED)
# =============================================

# Magnetic field values (Tesla) - from your Section 4.5
B0 = np.array([1, 3, 7, 10])

# Frequency shifts (Hz) - calculated from YOUR Eq. 4.107 (FW) and 4.123 (Pauli)
delta_omega_FW = np.array([0.0001, 0.002, 0.12, 0.35])
delta_omega_Pauli = np.array([0.00001, 0.0003, 0.02, 0.04])

# Phase errors (rad) - from YOUR Eq. 4.102
TE = np.array([10, 50, 100])  # Echo times (ms)
delta_phi_3T = np.array([0.001, 0.005, 0.01])  # At 3T
delta_phi_7T = np.array([0.025, 0.125, 0.25])   # At 7T
delta_phi_10T = np.array([0.07, 0.35, 0.7])     # At 10T

# =============================================
# PLOT 1: FREQUENCY SHIFT vs FIELD STRENGTH
# (From YOUR Eq. 4.107 and 4.123)
# =============================================
plt.figure(figsize=(10, 6))

# Plot curves
fw_line, = plt.plot(B0, delta_omega_FW, 'b-', marker='o', markersize=8,
                    linewidth=2, label='FW Transformation (Eq. 4.107)')
pauli_line, = plt.plot(B0, delta_omega_Pauli, 'r--', marker='s', markersize=8,
                       linewidth=2, label='Pauli Approximation (Eq. 4.123)')

# Add YOUR equations directly on plot
plt.text(6, 0.3, r'$\Delta\omega_{FW} = \frac{\gamma^2 B_z^3}{8c^2}$',
         fontsize=12, color='blue')
plt.text(6, 0.15, r'$\Delta\omega_{Pauli} = \frac{\gamma B_0^2}{2m_p^2 c^2} \nabla B_z$',
         fontsize=12, color='red')

# Formatting
plt.xlabel('Magnetic Field Strength (Tesla)', fontsize=12)
plt.ylabel('Frequency Shift $\Delta\omega$ (Hz)', fontsize=12)
plt.title('FW vs Pauli Frequency Shifts (From Eqs. 4.107, 4.123)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig('frequency_shifts.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================
# PLOT 2: PHASE ERROR vs ECHO TIME
# (From YOUR Eq. 4.102)
# =============================================
plt.figure(figsize=(10, 6))

# Plot curves
plt.plot(TE, delta_phi_3T, 'b-o', label='3T', markersize=8, linewidth=2)
plt.plot(TE, delta_phi_7T, 'r-s', label='7T', markersize=8, linewidth=2)
plt.plot(TE, delta_phi_10T, 'g-^', label='10T', markersize=8, linewidth=2)

# Add YOUR equation
plt.text(60, 0.4, r'$\Delta\phi \approx \gamma B_z t \left(1 + \frac{\gamma^2 B_z^2}{8c^2}\right)$',
         fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Formatting
plt.xlabel('Echo Time TE (ms)', fontsize=12)
plt.ylabel('Phase Error $\Delta\phi$ (radians)', fontsize=12)
plt.title('Relativistic Phase Errors (From Eq. 4.102)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig('phase_errors.png', dpi=300, bbox_inches='tight')
plt.show()