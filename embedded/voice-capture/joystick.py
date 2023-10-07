#joystick.py
import os
import wave
import pyaudio
import time
from sense_hat import SenseHat
from senseHat_pixels.pixel_handler import PixelManager

class AudioRecorder:
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    DURATION = 6
    FOLDER = "/home/s13/projects/sensehat_chatbot/embedded/assets/audio_files/current_user_prompt"
    FILENAME = "timestamp_{time}.wav"

    def __init__(self, pixel_manager):
        os.makedirs(self.FOLDER, exist_ok=True)
        self.pixel_manager = pixel_manager
    
    def record_audio(self):
        p = pyaudio.PyAudio()
        self.pixel_manager.update_pixels("recording")
        
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        
        print("Recording...")
        frames = [stream.read(self.CHUNK) for _ in range(0, int(self.RATE / self.CHUNK * self.DURATION))]
        
        print("Finished recording.")
        self.pixel_manager.update_pixels("off")

        filepath = os.path.join(self.FOLDER, self.FILENAME.format(time=int(time.time())))
        with wave.open(filepath, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
        
        print(f"Audio recorded and saved to {filepath}")

        stream.stop_stream()
        stream.close()
        p.terminate()


def main():
    sense = SenseHat()
    pixel_manager = PixelManager()
    audio_recorder = AudioRecorder(pixel_manager)
    
    print("Ready for voice input!")
    pixel_manager.start_displaying_message()
    
    try:
        is_recording = False
        while True:
            for event in sense.stick.get_events():
                if event.action == 'pressed' and not is_recording:
                    pixel_manager.stop_displaying_message()
                    is_recording = True
                    audio_recorder.record_audio()
                    sense.stick.get_events()
                    is_recording = False
                    print("Ready for voice input!")
                    pixel_manager.start_displaying_message()
    except KeyboardInterrupt:
        pixel_manager.stop_displaying_message()
        print("Exiting...")

if __name__ == "__main__":
    main()