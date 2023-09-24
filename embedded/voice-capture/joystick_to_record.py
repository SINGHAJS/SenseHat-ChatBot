import subprocess
import time
import os
import signal  # Import the signal module
from sense_hat import SenseHat

class AudioRecorder:
    def __init__(self, device, duration, type, file_prefix="rec", folder="../assets/audio_files"):
        self.device = device
        self.duration = duration
        self.type = type
        self.file_prefix = file_prefix
        self.folder = folder
        self.process = None
        os.makedirs(self.folder, exist_ok=True)

    def start_recording(self):
        if self.is_recording():
            print("Already recording!")
            return
        filename = f"{self.file_prefix}_{int(time.time())}.{self.type}"
        filepath = os.path.join(self.folder, filename)
        cmd = ["arecord", "-D", self.device, "-d", str(self.duration), filepath]
        self.process = subprocess.Popen(cmd)
        print(f"Recording started... {filepath}")

    def stop_recording(self):
        if not self.is_recording():
            print("Not recording!")
            return
        self.process.send_signal(signal.SIGINT)  # Send SIGINT to arecord process
        self.process.wait()
        print("Recording stopped.")

    def is_recording(self):
        return self.process is not None and self.process.poll() is None

def joystick_event_handler(event, recorder):
    if event.action == 'pressed':
        recorder.start_recording()
    elif event.action == 'released':
        recorder.stop_recording()

def main():
    sense = SenseHat()
    # Below will depend on which device our mic is
    # run arecord -l to find plughw<n,m>
    recorder = AudioRecorder(device="plughw:1,0", duration=5, type="wav")
    
    try:
        while True:
            event = sense.stick.wait_for_event()
            joystick_event_handler(event, recorder)
    except KeyboardInterrupt:
        print("line 56 exiting...")
    finally:
        if recorder.is_recording():
            recorder.stop_recording()

if __name__ == "__main__":
    main()
