from sense_hat import SenseHat

# Colors
RED = [255, 0, 0]
OFF = [0, 0, 0]

class PixelManager:
    def __init__(self):
        self.sense = SenseHat()

    def update_pixels(self, status):
        if status == 'recording':
            self.sense.set_pixels([RED] * 64)
        else:
            self.sense.clear()

# If you want to use the PixelManager outside of this module, you can use this:
# pixel_manager = PixelManager()
# pixel_manager.update_pixels('recording')
