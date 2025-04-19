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

def plot_wave(t, y):
    """Plot the given wave.

    Parameters:
    t (array-like): Time values.
    y (array-like): Wave values.
    """
    plt.plot(t, y)
    plt.title('Symmetric Triangle Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# Parameters
T = 10  # Period of the triangle wave
t = np.linspace(0, 50, 1000)  # Time values from 0 to 50 seconds

# Generate the triangle wave
y = symmetric_triangle_wave(t, T)

# Plot the triangle wave
plot_wave(t, y)

#pick random points between 0 and 50 seconds and get the value of the triangle wave at those points
random_times = np.random.uniform(0, 50, 100)
random_values = symmetric_triangle_wave(random_times, T)
print("Random times:{}\n".format(random_times))
print("Values at random times:{}\n".format(random_values))

#for those random times deivde by the period and get the value for remainder at the train=gle wave
# this is the same as the value of the triangle wave at those points
remainder = random_times % T
print("Remainder of random times divided by period:{}\n".format(remainder))
print("Values at remainder times:{}\n".format(symmetric_triangle_wave(remainder, T)))
#plot the scatter plot of the random times and the values at those points
plt.scatter(remainder, random_values, color='red', label='Random Points')
plt.legend()
plt.title('Random Points on Triangle Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


#pick random points between 0 and 50 seconds and get the value of the triangle wave at those points but with noise added
random_times = np.random.uniform(0, 50, 100)
random_values = symmetric_triangle_wave(random_times, T) + np.random.normal(0, 0.1, random_times.shape)
print("Random times:{}\n".format(random_times))
print("Values at random times:{}\n".format(random_values))

#for those random times deivde by the period and get the value for remainder at the train=gle wave
# this is the same as the value of the triangle wave at those points
remainder = random_times % T
print("Remainder of random times divided by period:{}\n".format(remainder))
print("Values at remainder times:{}\n".format(symmetric_triangle_wave(remainder, T)))
#plot the scatter plot of the random times and the values at those points
plt.scatter(remainder, random_values, color='red', label='Random Points')
plt.legend()
plt.title('Random Points on Triangle Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
