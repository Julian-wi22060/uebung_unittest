import unittest
from unittest.mock import MagicMock
from instagram.image import Image
from instagram.api import InstagramApi


class TestImageUploadIntegration(unittest.TestCase):
    def test_upload_image_success(self):
        """
        Testet, dass die upload_image-Methode die post-Methode korrekt aufruft
        und die API-Antwort verarbeitet, wenn das Bild gültig ist.
        """
        # Arrange
        image = Image(file_format="jpeg", size_in_bytes=4_000_000)
        api = InstagramApi()
        api.post = MagicMock(return_value={"success": True, "message": "Bild erfolgreich hochgeladen"})

        # Act
        response = api.upload_image(image)

        # Dynamische Print-Nachricht
        print(
            f"Test '{self._testMethodName}': Test für Bild mit Format {image.file_format} und Größe {image.size_in_bytes} Bytes. API-Antwort: {response}")

        # Assert
        api.post.assert_called_once_with({"format": "jpeg", "size": 4_000_000})
        self.assertEqual(response, {"success": True, "message": "Bild erfolgreich hochgeladen"})

    def test_upload_image_invalid_image(self):
        """
        Testet, dass die upload_image-Methode die API nicht aufruft,
        wenn das Bild ungültig ist.
        """
        # Arrange
        image = Image(file_format="bmp", size_in_bytes=6_000_000)  # Ungültiges Bild
        api = InstagramApi()
        api.post = MagicMock()

        # Act
        response = api.upload_image(image)

        # Dynamische Print-Nachricht
        print(
            f"Test '{self._testMethodName}': Test für Bild mit Format {image.file_format} und Größe {image.size_in_bytes} Bytes. API wurde nicht aufgerufen. Antwort: {response}")

        # Assert
        api.post.assert_not_called()
        self.assertEqual(response, {"success": False, "message": "Ungültiges Bild"})


if __name__ == "__main__":
    unittest.main()
