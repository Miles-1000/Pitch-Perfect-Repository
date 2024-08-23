# scatter plot of guesses vs actual values
import matplotlib.pyplot as plt
import numpy as np

# load data
data = np.loadtxt('bastiaan.txt')
frequencies = data[:,0]
guesses = data[:,1]
time_stamps = data[:,2] # ignore this

# plot data
plt.scatter(frequencies, guesses, c='black', marker='x')
plt.xlabel('Actual Frequency')
plt.ylabel('Guessed Frequency')

# draw straight line y = x
x = np.linspace(27, 4186, 100)
plt.plot(x, x, c='red')

plt.show()