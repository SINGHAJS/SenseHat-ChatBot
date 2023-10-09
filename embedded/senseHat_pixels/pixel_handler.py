# pixel_handler.py

from sense_hat import SenseHat
import threading

# Colors
RED = [255, 0, 0]
OFF = [0, 0, 0]
BLUE = [0, 0, 255]

class PixelManager:
    def __init__(self):
        self.sense = SenseHat()
        self.running = False
        self.thread = None

    def update_pixels(self, status):
        if status == 'recording':
            self.sense.set_pixels([RED] * 64)
        else:
            self.sense.clear()

    def display_message_from_file(self, file_path='/home/s13/projects/sensehat_chatbot/embedded/assets/responses/responses.txt'):
        while self.running:
            with open(file_path, 'r') as f:
                message = f.read().strip()
                self.sense.show_message(message, scroll_speed=0.08, text_colour=BLUE)

    def start_displaying_message(self):
        self.running = True
        self.thread = threading.Thread(target=self.display_message_from_file)
        self.thread.start()

    def stop_displaying_message(self):
        self.running = False
        if self.thread:
            self.thread.join()
