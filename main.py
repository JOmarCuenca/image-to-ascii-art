from PIL import Image
from tqdm import tqdm
from math import ceil

from utils.args_parser import Args
import os


def load_image(file_path):
    try:
        image = Image.open(file_path)
        return image
    except IOError:
        print("Unable to load image.")


def image_to_ascii(image: Image, size_ratio=1, colorful=False):
    """
    Convert an image to ASCII art.

    Args:
        image (PIL.Image): The input image.
        size_ratio (int, optional): The ratio to resize the image. Defaults to 1.
        colorful (bool, optional): Whether to use colorful ASCII characters. Defaults to False.

    Returns:
        str: The ASCII representation of the image.
    """
    ascii_chars = "@%#*+=-:. "
    if colorful:
        ascii_chars = "⬛⬜🔳🔲⚫⚪⬜🟤🟣🔵🟢🟡🟠🔴🟧🟨🟩🟦🟪🟫⬛"
    ascii_image = ""
    width, height = image.size
    new_width = width // size_ratio
    new_height = height // size_ratio
    image = image.resize((new_width, new_height))
    total_pixels = new_width * new_height
    with tqdm(total=total_pixels, unit="pixels", desc="Transforming pixels to characters") as pbar:
        for y in range(new_height):
            for x in range(new_width):
                pixel = image.getpixel((x, y))
                grayscale = sum(pixel) // 3
                ascii_image += ascii_chars[min(grayscale // ceil(
                    255 / len(ascii_chars)), len(ascii_chars) - 1)]
                pbar.update(1)
            ascii_image += "\n"
    return ascii_image


if __name__ == "__main__":
    args = Args.parseArgs()
    file_path = args.image_path
    size_ratio = args.image_size
    image = load_image(file_path)
    if image:
        ascii_image = image_to_ascii(image, size_ratio, args.colorful)

        if not os.path.exists("outputs"):
            os.makedirs("outputs")

        with open(f"outputs/{args.output_path}", "w") as f:
            f.write(ascii_image)

        print("Image converted successfully.")
    else:
        print("Error converting image.")
