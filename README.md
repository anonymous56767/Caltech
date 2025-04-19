# Caltech
AAC project under Ashish sir(Caltech)
Here’s a clean and informative `README.md` for your two Python scripts:

---

# Periodic Function Analysis and Visualization

This project contains two Python scripts focused on generating, analyzing, and visualizing symmetric triangle waveforms. The code demonstrates how to analyze periodic functions using Fourier techniques and statistical properties with and without noise.

## Files

### 1. `periodfinding.py`

This script demonstrates the use of Fourier analysis to estimate the period of a symmetric triangle wave.

#### Features:
- **Waveform Generation**: Creates a symmetric triangle wave based on a specified period.
- **Fourier Analysis**: Implements a basic Fourier decomposition to estimate the period of the waveform using the first few harmonic coefficients.
- **Visualization**: Plots the triangle waveform using `matplotlib`.

#### How to Run:
```bash
python periodfinding.py
```

---

### 2. `sawtooth.py`

This script focuses on generating a symmetric triangle wave and sampling it at random time points with and without added noise.

#### Features:
- **Waveform Plotting**: Plots the triangle wave across a defined time range.
- **Random Sampling**: Samples points randomly from the waveform and calculates the corresponding values.
- **Noise Simulation**: Adds Gaussian noise to demonstrate real-world signal irregularities.
- **Scatter Plot Visualization**: Plots the random samples with and without noise to visualize sampling effects.

#### How to Run:
```bash
python sawtooth.py
```

---
