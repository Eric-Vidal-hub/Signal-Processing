# %%% 2.1 Load and store the audio signal as an array and the sampling
# frequency as a float
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import sounddevice as sd

files = ['./TDSound/PianoLaPeriod.wav',
         './TDSound/FluteLaPeriod.wav',
         './TDSound/ViolinLaPeriod.wav',
         './TDSound/TrumpetLaPeriod.wav']
frequencies = [0] * len(files)
amplitudes = [0] * len(files)
for i in range(len(files)):
    amplitudes[i], frequencies[i] = sf.read(files[i])

instruments = ['Piano', 'Flute', 'Violin', 'Trumpet']
for i in range(len(instruments)):
    print('Frequency of', instruments[i], 'La note:', frequencies[i])

# Sampling frequency with regards to the Shannon-Nyquist theorem?
# Frequency difference among them too little to distinguish for human


# %%% 2.2 Time interval between two values of the sound signal
spacing = []
for i in range(len(instruments)):
    spacing.append(1 / frequencies[i])

# Time interval between two values of the sound signal
times = []
for j in range(len(instruments)):
    amplitude = amplitudes[j]
    times.append([i * spacing[j] for i in range(len(amplitude))]) # in seconds

# %%% 2.3 Plot the signal
# Subplots of the signals
plt.figure(1)
for i in range(len(instruments)):
    plt.subplot(2, 2, i + 1)
    time = times[i]
    plt.plot([j * 10 ** 3 for j in time], amplitudes[i]) # time in miliseconds
    plt.ylabel(instruments[i] + ' La note')
    plt.xlabel('t (ms)')

plt.show()

# %%% 2.4 Playing notes
# Samples are too short, repeat 1000 periods
playing = []
for i in range(len(instruments)):
    playing.append(np.repeat(amplitudes[i], 1000))
    sd.play(playing[i], times[i])

# %%% 2.5 FFT
coeffs = []
for i in range(len(instruments)):
    coeffs.append(np.fft.fft(amplitudes[i]).tolist())  # convert numpy array to list

# Subplots for the absolute value of Fourier coefficients
plt.figure(2)
for i in range(len(instruments)):
    time = times[i]
    frequency = [j / time[-1] for j in range(len(coeffs[i]))]
    plt.subplot(2, 2, i + 1)
    plt.stem(frequency, np.abs(coeffs[i]))     # stem plot, it is better to understand the Fourier coefficients
    plt.ylabel(instruments[i] + ' La note')
    plt.xlabel('Frequency [Hz]')
plt.show()