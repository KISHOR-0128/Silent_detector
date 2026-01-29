import numpy as np

class SilenceDetector:
    def __init__(self, threshold=0.01, silence_duration=10, sample_rate=44100):
        self.threshold = threshold
        self.silence_duration = silence_duration  # in seconds
        self.sample_rate = sample_rate
        self.silent_time = 0.0

    def check_silence(self, audio_data):
        # Calculate average volume
        volume = np.mean(np.abs(audio_data))

        # Check if below silence threshold
        if volume < self.threshold:
            self.silent_time += len(audio_data) / self.sample_rate

            # If silence exceeds allowed duration
            if self.silent_time >= self.silence_duration:
                self.silent_time = 0.0
                return True  # Silence detected
        else:
            # Reset if sound is detected
            self.silent_time = 0.0

        return False