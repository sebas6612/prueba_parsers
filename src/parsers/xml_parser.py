import os
import csv
import xml.etree.ElementTree as ET
from .base_parser import BaseParser


class XmlToCsvParser(BaseParser):
    """
    XmlToCsvParser is a parser that converts XML files to CSV format.
    Args:
        origin (str): Path to the input XML file.
        destiny (str): Directory path where the CSV file will be saved.
    Methods:
        parse():
            Parses the XML file and writes its contents to a CSV file.
            The output filename will be the same as the input file with .csv extension.
    Raises:
        Any exceptions raised by file I/O, XML parsing, or CSV writing will propagate.
    """

    def __init__(self, origin: str, destiny: str) -> None:
        # Get the original filename and change extension to .csv
        original_filename = os.path.basename(origin)
        csv_filename = os.path.splitext(original_filename)[0] + ".csv"
        final_destiny = os.path.join(destiny, csv_filename)
        super().__init__(origin, final_destiny)

    def parse(self) -> None:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(self.destiny), exist_ok=True)

        tree = ET.parse(self.origin)
        root = tree.getroot()

        with open(self.destiny, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            headers = [elem.tag for elem in root[0]]
            writer.writerow(headers)

            for elem in root:
                row = [child.text for child in elem]
                writer.writerow(row)
