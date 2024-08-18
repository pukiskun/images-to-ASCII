import unittest
from src.converter import scale_image, grayscale_image, map_pixels_to_ascii
from PIL import Image

class TestConverter(unittest.TestCase):

    def setUp(self):
        self.image = Image.new("RGB", (100, 100), color='white')

    def test_scale_image(self):
        scaled_image = scale_image(self.image, new_width=50)
        self.assertEqual(scaled_image.size[0], 50)

    def test_grayscale_image(self):
        grayscale = grayscale_image(self.image)
        self.assertEqual(grayscale.mode, "L")

    def test_map_pixels_to_ascii(self):
        grayscale = grayscale_image(self.image)
        ascii_art = map_pixels_to_ascii(grayscale)
        self.assertTrue(isinstance(ascii_art, str))
        self.assertTrue(len(ascii_art) > 0)

if __name__ == '__main__':
    unittest.main()
