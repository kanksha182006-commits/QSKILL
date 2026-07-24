import sounddevice as sd
import soundfile as sf

devices = [1, 5, 9]

for device in devices:
    print(f"\nTesting microphone device {device}")
    input("Press Enter and speak for 5 seconds...")

    audio = sd.rec(
        int(5 * 44100),
        samplerate=44100,
        channels=1,
        dtype="int16",
        device=device
    )

    sd.wait()

    filename = f"test_device_{device}.wav"
    sf.write(filename, audio, 44100)

    print(f"Saved {filename}")
    