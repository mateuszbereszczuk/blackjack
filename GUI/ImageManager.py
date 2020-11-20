import os
from PIL import Image, ImageTk


class ImageManager:
    def add_image(self, file_name, window_height):
        relative_image_path = '../media/images/'
        script_dir = os.path.dirname(__file__)

        image_path = os.path.join(script_dir, relative_image_path, file_name)
        image = Image.open(image_path)
        image = self.resize_card_image(image, window_height)
        render = ImageTk.PhotoImage(image)
        return render

    @staticmethod
    def resize_card_image(image, window_height):
        image_width, image_height = image.size
        card_width = int((window_height / image_height) * image_width)
        return image.resize((card_width, int(window_height)))
