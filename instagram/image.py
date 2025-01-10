class Image:
    """
    Stellt ein Bild-Objekt dar, das hochgeladen werden kann.
    """

    def __init__(self, file_format: str, size_in_bytes: int):
        """
        :param file_format: Dateiformat, z.B. 'jpeg' oder 'png'
        :param size_in_bytes: Größe des Bildes in Byte
        """
        self.file_format = file_format
        self.size_in_bytes = size_in_bytes

    def validate_image(self) -> bool:
        """
        Überprüft, ob das Bild ein unterstütztes Format hat
        und die maximale Dateigröße von 5 MB nicht überschreitet.

        :return: True, wenn das Bild valide ist, sonst False
        """
        supported_formats = ["jpeg", "png"]
        max_size = 5 * 1024 * 1024  # 5 MB

        # Format-Check
        if self.file_format.lower() not in supported_formats:
            return False

        # Größen-Check
        if self.size_in_bytes > max_size:
            return False

        return True
