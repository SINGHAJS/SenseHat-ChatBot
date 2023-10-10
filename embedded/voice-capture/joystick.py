import os
import wave
import pyaudio
import time
import subprocess
from sense_hat import SenseHat
from embedded.senseHat_pixels.pixel_handler import PixelManager

class AudioRecorder:
    """
    This class handles the audio recording process, pixel manager
    to give visual feedback during recording and saving the recorded file.
    """

    # Audio configurations
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    DURATION = 6

    # File and path configurations
    FOLDER = "/home/s13/projects/sensehat_chatbot/embedded/assets/audio_files/current_user_prompt"
    FILENAME = "timestamp_{time}.wav"

    def __init__(self, pixel_manager: PixelManager):
        os.makedirs(self.FOLDER, exist_ok=True)
        self.pixel_manager = pixel_manager

    def record_audio(self):
        """Handles the recording process, saving the audio and updating visual feedback."""
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

        # Trigger other processes after recording
        self.post_recording_actions()

    def post_recording_actions(self):
        # Too easily broken when using our own implementation of threading, so we're using the subproces library. call() waits until completed
        cmd1 = ["python3", "-m", "services.src.main"]
        subprocess.call(cmd1, cwd="/home/s13/projects/sensehat_chatbot")

        cmd2 = ["python3", "embedded/file_handler/move_old_prompt.py"]
        subprocess.call(cmd2, cwd="/home/s13/projects/sensehat_chatbot")


def main():
    sense = SenseHat()
    pixel_manager = PixelManager()
    audio_recorder = AudioRecorder(pixel_manager)

    # Initial action to move old prompts
    cmd = ["python3", "embedded/file_handler/move_old_prompt.py"]
    subprocess.call(cmd, cwd="/home/s13/projects/sensehat_chatbot")

    print("Ready for voice input!")
    #this creates a thread that will display a message on the screen while the user is recording. (threading is inside pixel manager)
    # pixel_manager.start_displaying_message()

    try:
        is_recording = False
        while True:
            for event in sense.stick.get_events():
                # Check for joystick press to start recording
                if event.action == 'pressed' and not is_recording:
                    pixel_manager.stop_displaying_message()
                    is_recording = True
                    audio_recorder.record_audio()
                    sense.stick.get_events()  # Clear events to prevent rapid successive reads
                    is_recording = False
                    print("Ready for voice input!")
                    pixel_manager.start_displaying_message()

    except KeyboardInterrupt:  # Exit on keyboard interrupt
        pixel_manager.stop_displaying_message()
        print("Exiting...")

if __name__ == "__main__":
    main()
