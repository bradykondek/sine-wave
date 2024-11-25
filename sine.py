# Include libaries
import numpy as np
import matplotlib.pyplot as plt  # used to plot sine wave
import sounddevice as sd  # used to play sine wave
import tkinter as tk
from tkinter import messagebox

# Prompt user for frequency, amplitude, and duration
def getValues():

    # Prompt user for frequency
    frequency = float(input("Enter frequency: "))

    # Prompt user for amplitude
    amplitude = float(input("Enter amplitude: "))

    # Prompt user for duration
    duration = float(input("Enter duration: "))

    # Return user-inputted values
    return frequency, amplitude, duration

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

# Play sine wave
def playSineWave(sineWave, sample_rate):

    # Control function
    # Play sound
    def play_sound():

        # Disable play button
        play_button.config(state=tk.DISABLED)  # disable play button while sound is playing
        
        # Print status message
        print("Playing sound...")

        # Play sound
        sd.play(sineWave, sample_rate)

        # Re-enable play button after audio has finished playing
        play_button.config(state=tk.NORMAL)

    # Stop sound
    def stop_sound():

        # Stop sound
        sd.stop()

        # Enable play button
        play_button.config(state=tk.NORMAL)  # enable play button once stopped
        
        # Print status message
        print("Stopped sound.")

    # Wait while sine wave is being played
    print("Playing sine wave...")
    sd.wait()

    # Setting up the tkinter window
    root = tk.Tk()
    root.title("Sine Wave Player")

    # Add play button
    play_button = tk.Button(root, text="Play", command=play_sound)
    play_button.pack(pady=10)

    # Add stop button
    stop_button = tk.Button(root, text="Stop", command=stop_sound)
    stop_button.pack(pady=10)

    # Start the tkinter program
    root.mainloop()

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

    # Play sine wave
    playSineWave(sineWave, sample_rate)

# Main function
def main():

    # Prompt user for frequency, amplitude, and duration
    freq, amp, dur = getValues()
    
    # Generate sine wave, then plot results
    plotSineWave(frequency=freq, amplitude=amp, duration=dur)

main()