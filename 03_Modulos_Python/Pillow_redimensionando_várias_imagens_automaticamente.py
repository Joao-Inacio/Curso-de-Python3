"""
Pillow: redimensionando várias imagens automaticamente
"""
import os
from PIL import Image


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe')

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)
            new_file = file_name + '_CONVERTED' + extension
            new_file_full_path = os.path.join(root, new_file)

            if os.path.isfile(new_file_full_path):
                print(f'Arquivo {new_file_full_path} já existe')

            if '_CONVERTED' in file_full_path:
                continue

            img_pillow = Image.open(file_full_path)
            width, height = img_pillow.size
            new_height = round(new_width * height / width)

            new_image = img_pillow.resize(
                (new_width, new_height),
                Image.LANCZOS,
            )
            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70,
                exif=img_pillow.info['exif']
            )

            new_image.close()
            print(width, new_width, height, new_height)
            img_pillow.close()

        #  if '_CONVERTED' in new_file_full_path:
                # os.remove(new_file_full_path)


if __name__ == '__main__':
    main_images_folder = r'C:\Users\joaoi\OneDrive\Imagens\Wallpaper'
    main(main_images_folder, 640)
