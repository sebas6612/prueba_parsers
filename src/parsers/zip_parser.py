import zipfile
from .base_parser import BaseParser


class ZipFileParser(BaseParser):

    def __init__(self, origin: str, destiny: str) -> None:
        super().__init__(origin, destiny)

    def parse(self) -> None:
        with zipfile.ZipFile(self.origin, "r") as zip_ref:
            zip_ref.extractall(self.destiny)
