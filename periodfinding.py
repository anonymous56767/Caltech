import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


def symmetric_triangle_wave(t, T):
    """Generate a symmetric triangle wave.

    Parameters:
    t (array-like): Time values.
    T (float): Period of the triangle wave.

    Returns:
    array-like: Symmetric triangle wave values.
    """
    return 2 * np.abs(2 * (t / T - np.floor(t / T + 0.5))) - 1

#def fourier_periodfinding(t, y, T, N=10): for any periodic function


def fourier_periodfinding(t, y, T, N=10):
    """Find the period of a periodic function using Fourier analysis.

    Parameters:
    t (array-like): Time values.
    y (array-like): Function values.
    T (float): Period of the function.
    N (int): Number of Fourier coefficients to compute.

    Returns:
    float: Estimated period of the function.
    """
    # Compute the Fourier coefficients
    a0 = np.mean(y)
    a = np.zeros(N)
    b = np.zeros(N)
    
    for n in range(1, N + 1):
        a[n - 1] = (2 / len(t)) * np.sum(y * np.cos(2 * np.pi * n * t / T))
        b[n - 1] = (2 / len(t)) * np.sum(y * np.sin(2 * np.pi * n * t / T))

    # Estimate the period using the first harmonic
    period_estimate = 2 * np.pi / np.sqrt(a[0]**2 + b[0]**2)

    return period_estimate

#apply to symmetric triangle wave
T = 1
t = np.linspace(0, 10, 1000)
y = symmetric_triangle_wave(t, T)
plt.plot(t, y)
plt.title("Symmetric Triangle Wave")
plt.grid()
plt.show()
period_estimate = fourier_periodfinding(t, y, T, N=100)
print(f"Estimated period: {period_estimate:.4f}")
