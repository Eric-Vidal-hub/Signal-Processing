# %%% 2.9 Sound explanation

# It is not periodic

# %%% 2.10 Load other files
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import sounddevice as sd

files = ['./TDSound/PianoLa.wav',
         './TDSound/FluteLa.aif',
         './TDSound/ViolinLa.aif',
         './TDSound/TrumpetLa.aif']
frequencies = [0] * len(files)
amplitudes = [0] * len(files)
for i in range(len(files)):
    amplitudes[i], frequencies[i] = sf.read(files[i])

ch1_amplitudes = [0] * len(files)
ch2_amplitudes = [0] * len(files)
for i in range(len(files)):
    ch1_amplitudes[i] = [amplitudes[i][j][0] for j in range(len(amplitudes[i]))]
    ch2_amplitudes[i] = [amplitudes[i][j][1] for j in range(len(amplitudes[i]))]

instruments = ['Piano', 'Flute', 'Violin', 'Trumpet']
for i in range(len(instruments)):
    # Should be the same as it is recorded by the same instrument
    print('Frequency of', instruments[i], 'La note:', frequencies[i], 'Hz')

# %%% 2.11 Time interval between two values of the sound signal
spacing = []
for i in range(len(instruments)):
    spacing.append(1 / frequencies[i])

# Time interval between two values of the sound signal
times = []
for j in range(len(instruments)):
    amplitude = amplitudes[j]
    times.append([i * spacing[j] for i in range(len(amplitude))]) # in seconds

# Subplots of the signals
plt.figure(1)
for i in range(len(instruments)):
    plt.subplot(2, 2, i + 1)
    time = times[i]
    plt.plot([j * 10 ** 3 for j in time], amplitudes[i]) # time in miliseconds
    plt.ylabel(instruments[i] + ' La note')
    plt.xlabel('t (ms)')
plt.show()

# %%% 2.12 FFT
amplitudes = ch1_amplitudes  # We have to work with just one channel
# for i in range(len(instruments)):
    # sd.play(amplitudes[i], times[i])

coeffs = []
for i in range(len(instruments)):
    coeffs.append(np.fft.fft(amplitudes[i]).tolist())  # convert numpy array to list

# Subplots for the absolute value of Fourier coefficients
plt.figure(2)
for i in range(len(instruments)):
    time = times[i]
    frequency = [j / time[-1] for j in range(len(coeffs[i]))]
    plt.subplot(2, 2, i + 1)
    plt.plot(frequency, np.abs(coeffs[i]))     # stem plot, it is better to understand the Fourier coefficients
    plt.ylabel(instruments[i] + ' La note')
    plt.xlabel('Frequency [Hz]')
plt.show()

# %%% 2.13 Discussion

# To think

# %%% 2.14 Propose an order

Thum = 0.1
Nw = 2 ** np.ceil(np.log2(Thum * frequencies[0]))  # Numbers in the window, 8192
s = 4.

N = []
Ns = []
for i in range(len(instruments)):
    N.append(len(amplitudes[i]))
    Ns.append(np.floor((N[i]-Nw)/(Nw/s)))  # 142 for piano
print(Ns,Nw)

matrices = []
for i in range(len(instruments)):
    matrices.append(np.zeros((int(Nw), int(Ns[i]))))