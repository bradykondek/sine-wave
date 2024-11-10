# Include libaries
import numpy as np
import matplotlib.pyplot as plt

# Model a sine wave
def generateSineWave(frequency=1, amplitude=1, duration=2, sample_rate=1000):  # sets the "=" values to the following values if corresponding value has no direct input

    """
    Generates a sine wave based on the given parameters.

    Parameters:
        frequency (float): Frequency of the sine wave (Hz)
        amplitude (float): Amplitude of the sine wave
        duration (float): Duration of the wave (seconds)
        sample_rate (int): Number of samples per second
    
    Returns:
        tuple: time array and sine wave values
    """

    # Time axis
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint = False)

    # Sine wave value
    sineWave = amplitude * np.sin(2 * np.pi * frequency * time)  # sine wave formula

    # Return time array and sine wave value as tuple
    return time, sineWave

# Plot sine wave
def plotSineWave(frequency=1, amplitude=1, duration=2, sample_rate=1000):

    # Call generateSineWave function to get time array and sine wave
    time, sineWave = generateSineWave(frequency, amplitude, duration, sample_rate)

    # Plot results
    plt.plot(time, sineWave)
    plt.title(f"Sine wave - {frequency} Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

# Main function
def main():

    # Generate sine wave, then plot results
    plotSineWave(frequency=10, amplitude=1, duration=2)

main()