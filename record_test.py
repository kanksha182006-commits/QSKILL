import sounddevice as sd
import soundfile as sf

device = 1  # Your microphone device

# Get the microphone's default sample rate
info = sd.query_devices(device, 'input')
fs = int(info['default_samplerate'])

print("Using sample rate:", fs)
print("Speak for 5 seconds...")

audio = sd.rec(
    int(5 * fs),
    samplerate=fs,
    channels=1,
    dtype='int16',
    device=device
)

sd.wait()

sf.write("test.wav", audio, fs)

print("Recording saved as test.wav")
