# 2.1 Load and store the audio signal as an array and the sampling frequency as a float
import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

f_piano, piano = wavfile.read('./TDSound/PianoLaPeriod.wav')
f_flute, flute = wavfile.read('./TDSound/FluteLaPeriod.wav')
f_violin, violin = wavfile.read('./TDSound/ViolinLaPeriod.wav')
f_trumpet, trumpet = wavfile.read('./TDSound/TrumpetLaPeriod.wav')