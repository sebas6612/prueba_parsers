from abc import ABC, abstractmethod


class BaseParser(ABC):
    """
    Base class for all parsers.

    This class defines the interface for parser classes. Subclasses must implement
    the `parse` method to provide specific parsing logic.

    Attributes
    ----------
    origin : str
        Source path or location of the input data
    destiny : str
        Destination path or location for the parsed output

    Methods
    -------
    parse():
        Abstract method that must be implemented by subclasses to perform parsing.
    """

    def __init__(self, origin: str, destiny: str) -> None:
        """
        Initialize the parser with source and destination paths.

        Parameters
        ----------
        origin : str
            Source path or location of the input data
        destiny : str
            Destination path or location for the parsed output
        """
        self.origin = origin
        self.destiny = destiny

    @abstractmethod
    def parse(self) -> None:
        """
        Parses the input data.

        This method should be implemented by subclasses to define the parsing logic
        for specific data formats or sources.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")
