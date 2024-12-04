import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
from image_processor import ImageProcessor  # Импортируем модуль обработки изображений

class UserInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing App")
        self.processor = ImageProcessor()

        self.image_labels = []
        self.images = []

        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.master, text="Загрузить изображения", command=self.load_images)
        self.load_button.pack()

        self.resize_button = tk.Button(self.master, text="Изменить размер", command=self.resize_images)
        self.resize_button.pack()

        self.concatenate_button = tk.Button(self.master, text="Склеить изображения", command=self.concatenate_images)
        self.concatenate_button.pack()

    def load_images(self):
        file_paths = filedialog.askopenfilenames(title="Выберите изображения", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if file_paths:
            self.images = file_paths
            for path in file_paths:
                label = tk.Label(self.master, text=os.path.basename(path))
                label.pack()
                self.image_labels.append(label)

    def resize_images(self):
        if not self.images:
            messagebox.showwarning("Предупреждение", "Сначала загрузите изображения.")
            return

        width = int(input("Введите новую ширину: "))
        height = int(input("Введите новую высоту: "))

        for img_path in self.images:
            resized_img = self.processor.resize_image(img_path, (width, height))
            resized_img.show()  # Показываем измененное изображение

    def concatenate_images(self):
        if not self.images:
            messagebox.showwarning("Предупреждение", "Сначала загрузите изображения.")
            return

        concatenated_img = self.processor.concatenate_images(self.images)
        concatenated_img.show()  # Показываем склеенное изображение

if __name__ == "__main__":
    root = tk.Tk()
    ui = UserInterface(root)
    root.mainloop()
