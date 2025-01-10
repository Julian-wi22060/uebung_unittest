import unittest
from instagram.image import Image


class TestImageValidation(unittest.TestCase):
    def test_validate_image_valid(self):
        """
        Testet, dass ein gültiges Bild (unter 5 MB, richtiges Format)
        als True zurückgegeben wird.
        """
        image = Image(file_format="jpeg", size_in_bytes=4_000_000)
        result = image.validate_image()
        print(f"Test für Bild mit Format {image.file_format} und Größe {image.size_in_bytes} Bytes: {result}")
        self.assertTrue(
            result,
            "Ein Bild unter 5MB und im Format 'jpeg' sollte als gültig erkannt werden."
        )

    def test_validate_image_invalid_format(self):
        """
        Testet, dass ein Bild mit einem nicht unterstützten Format
        als False zurückgegeben wird.
        """
        image = Image(file_format="gif", size_in_bytes=3_000_000)
        result = image.validate_image()
        print(f"Test für Bild mit Format {image.file_format} und Größe {image.size_in_bytes} Bytes: {result}")
        self.assertFalse(
            result,
            "Ein Bild im Format 'gif' sollte als ungültig erkannt werden."
        )

    def test_validate_image_invalid_size(self):
        """
        Testet, dass ein Bild mit einer Größe über 5 MB
        als False zurückgegeben wird.
        """
        image = Image(file_format="png", size_in_bytes=6_000_000)
        result = image.validate_image()
        print(f"Test für Bild mit Format {image.file_format} und Größe {image.size_in_bytes} Bytes: {result}")
        self.assertFalse(
            result,
            "Ein Bild über 5MB sollte als ungültig erkannt werden."
        )

    def test_validate_image_invalid_format_and_size(self):
        """
        Testet, dass ein Bild mit einem nicht unterstützten Format und
        einer Größe über 5 MB als False zurückgegeben wird.
        """
        image = Image(file_format="bmp", size_in_bytes=6_000_000)
        result = image.validate_image()
        print(f"Test für Bild mit Format {image.file_format} und Größe {image.size_in_bytes} Bytes: {result}")
        self.assertFalse(
            result,
            "Ein Bild mit Format 'bmp' und über 5MB sollte als ungültig erkannt werden."
        )


if __name__ == "__main__":
    unittest.main()
