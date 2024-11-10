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
    sineWave = amplitude * np.sin(2 * np.pi * frequency * t)  # sine wave formula

    # Return time array and sine wave value as tuple
    return time, sineWave

# Main function
def main():

    #