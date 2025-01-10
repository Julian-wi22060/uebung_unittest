class InstagramApi:
    """
    Eine Klasse, die die Kommunikation mit der Instagram-API abstrahiert.
    """

    def post(self, image_data: dict) -> dict:
        """
        Simuliert das Senden einer Anfrage an die Instagram-API.

        :param image_data: Daten des hochzuladenden Bildes
        :return: Antwort der API (z. B. Erfolgsstatus und Nachricht)
        """
        # Hier wäre normalerweise ein HTTP-Aufruf, z. B. mit requests
        raise NotImplementedError("Diese Methode sollte einen echten API-Aufruf machen.")

    def upload_image(self, image) -> dict:
        """
        Upload-Methode, die die `post`-Methode aufruft.

        :param image: Ein Objekt der Klasse Image
        :return: Antwort der API
        """
        if not image.validate_image():
            return {"success": False, "message": "Ungültiges Bild"}

        image_data = {
            "format": image.file_format,
            "size": image.size_in_bytes,
        }
        return self.post(image_data)
