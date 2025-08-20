import os

from pathlib import Path
from PIL import Image
from PIL import UnidentifiedImageError


class Album:
    """A class that holds the images to be analyzed."""

    def __init__(self, format: str | list, image_store: str):
        """Instantiates an 'Album' object to search for a specific
        image format.
        ---
        Parameters:
            format, str | list: The file format(s) that 'Album' will look for.
            image_store, str: The root directory that contains all the images to be loaded.
        """

        self.format = format
        self.image_store = image_store
        self.photos = {}
        self.edited_photos = {}

    def make_album(self):
        """
        Collects all images of the specific format provided.
        """

        if isinstance(self.format, str):
            self.format = [self.format]

        for format in self.format:
            self.photos[format] = {}
            for p in Path(self.image_store).glob(os.path.join("**", f"*.{format}")):
                try:
                    self.photos[format][p.name] = Image.open(p)
                except UnidentifiedImageError:
                    print(f"Could not open {p}.")  # TODO: Change to logging.
                    pass


if __name__ == "__main__":
    album = Album(
        format=["png", "bmp"],
        image_store=r"/mnt/myshare/Hubby/School/Grad/Research/Borys/Data/Optical_Microscopy",
    )

    album.make_album()
    print(album.album)
