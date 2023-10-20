#%%% 2.1 Load and store the audio signal as an array and the sampling frequency as a float
import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

f_piano, piano = wavfile.read('./TDSound/PianoLaPeriod.wav')
f_flute, flute = wavfile.read('./TDSound/FluteLaPeriod.wav')
f_violin, violin = wavfile.read('./TDSound/ViolinLaPeriod.wav')
f_trumpet, trumpet = wavfile.read('./TDSound/TrumpetLaPeriod.wav')

instruments = ['piano', 'flute', 'violin', 'trumpet']
frequencies = [f_piano, f_flute, f_violin, f_trumpet]
amplitudes = [piano, flute, violin, trumpet]

for i in range(len(instruments)):
    print('Frequency of', instruments[i], 'La note:', frequencies[i])

# Sampling frequency with regards to the Shannon-Nyquist theorem?
# Frequency difference among them too little to distinguish for human


#%%% 2.2 Time interval between two values of the sound signal

spacing = [0] * len(instruments)
for i in range(len(instruments)):
    spacing[i] = 1 / frequencies[i]

t_piano = [i * spacing[0] * 10 ** 3 for i in range(len(piano))]
t_flute = [i * spacing[1] * 10 ** 3 for i in range(len(flute))]
t_violin = [i * spacing[2] * 10 ** 3 for i in range(len(violin))]
t_trumpet = [i * spacing[3] * 10 ** 3 for i in range(len(trumpet))]

# times = [[i * spacing[0] * 10 ** 3 for i in range(len(instrument[j]))] for j in range(len(instruments))]
times = [t_piano, t_flute, t_violin, t_trumpet]
#%%% 2.3 Plot the signal

# Subplots of the signals
plt.figure(1)
for i in range(len(instruments)):
    plt.subplot(2, 2, i + 1)
    plt.plot(times[i], amplitudes[i])
    plt.title(instruments[i] + ' La note')
    plt.ylabel('Amplitude')
    plt.xlabel('t (ms)')
plt.show()

#%%% 2.4 Playing notes

# Samples are too short, repeat 1000 periods
playing = instruments.copy()

for i in range(len(playing)):
    playing[i] = np.repeat(playing[i], 1000)

#%%% 2.5 Calculate the Fourier coefficients
# Peridoic and with a power of 2 number of points

coeffs = [0] * len(instruments)
for i in range(len(instruments)):
    coeffs[i] = np.fft.fft(amplitudes[i])

# Subplots for the absolute value of Fourier coefficients
plt.figure(2)
for i in range(len(instruments)):
    # frequency = np.fft.fftfreq(len(coeffs[i]), spacing[i])   # Should study
    coeff = coeffs[i]
    frequency_step = 1 / spacing[-1]
    frequency = [i * frequency_step for i in range(len(coeff))]
    plt.subplot(2, 2, i + 1)
    plt.stem(frequency, np.abs(coeff))     # stem plot, it is better to understand the Fourier coefficients
    plt.title(instruments[i] + ' La note')
    plt.ylabel('Amplitude')
    plt.xlabel('Frequency [Hz]')
plt.show()
