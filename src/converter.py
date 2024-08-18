from PIL import Image, ImageDraw, ImageFont
import numpy as np

ASCII_CHARS = "@%#*+=-:. "

def scale_image(image, new_width=100):
    """Resizes the image while maintaining the aspect ratio."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    return image.resize((new_width, new_height))

def grayscale_image(image):
    """Converts the image to grayscale."""
    return image.convert("L")

def map_pixels_to_ascii(image):
    """Maps grayscale pixels to ASCII characters."""
    pixels = np.array(image)
    ascii_str = ""
    for pixel_row in pixels:
        for pixel in pixel_row:
            ascii_char = ASCII_CHARS[pixel // 32]
            ascii_str += ascii_char
        ascii_str += "\n"
    return ascii_str

def map_pixels_to_ascii_with_color(image):
    """Maps pixels to colored ASCII characters."""
    grayscale_image = image.convert("L")
    pixels = np.array(grayscale_image)
    ascii_str = ""
    colored_ascii = []

    for y, pixel_row in enumerate(pixels):
        row = []
        for x, pixel in enumerate(pixel_row):
            ascii_char = ASCII_CHARS[pixel // 32]
            color = image.getpixel((x, y))
            row.append((ascii_char, color))
            ascii_str += ascii_char
        ascii_str += "\n"
        colored_ascii.append(row)
    
    return colored_ascii

def ascii_to_image(colored_ascii, output_path, font_path="cour.ttf", font_size=10, black_bg=False):
    """Converts colored ASCII characters back to an image with optional black background."""
    font = ImageFont.truetype(font_path, font_size)
    
    # Measure character dimensions using getbbox()
    bbox = font.getbbox("A")
    char_width = bbox[2] - bbox[0]  # x1 - x0
    char_height = bbox[3] - bbox[1]  # y1 - y0

    img_width = char_width * len(colored_ascii[0])
    img_height = char_height * len(colored_ascii)
    
    # Use black background if specified
    bg_color = (0, 0, 0) if black_bg else (255, 255, 255)
    output_image = Image.new("RGB", (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(output_image)

    for y, row in enumerate(colored_ascii):
        for x, (char, color) in enumerate(row):
            draw.text((x * char_width, y * char_height), char, fill=color, font=font)

    output_image.save(output_path)


def convert_image_to_ascii(image_path, output_path, width=100, color=False, font_path="cour.ttf", font_size=10, black_bg=False):
    """Main function to convert an image to ASCII and optionally save it back as an image."""
    image = Image.open(image_path)
    image = scale_image(image, width)

    if color:
        colored_ascii = map_pixels_to_ascii_with_color(image)
        ascii_to_image(colored_ascii, output_path, font_path, font_size, black_bg)
    else:
        image = grayscale_image(image)
        ascii_str = map_pixels_to_ascii(image)
        with open(output_path, "w") as f:
            f.write(ascii_str)

