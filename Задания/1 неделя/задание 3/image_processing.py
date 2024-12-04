from PIL import Image
import os

class ImageProcessor:
    def __init__(self):
        pass

    def resize_image(self, image_path, new_size):
        """Изменение размера изображения."""
        with Image.open(image_path) as img:
            resized_img = img.resize(new_size)
            return resized_img

    def concatenate_images(self, image_paths):
        """Склеивание изображений в одно изображение."""
        images = [Image.open(img_path) for img_path in image_paths]

        # Определяем ширину и высоту для нового изображения
        total_width = sum(img.width for img in images)
        max_height = max(img.height for img in images)

        # Создаем новое изображение
        new_image = Image.new('RGB', (total_width, max_height))

        # Склеиваем изображения
        x_offset = 0
        for img in images:
            new_image.paste(img, (x_offset, 0))
            x_offset += img.width

        return new_image

