import pandas as pd
from colorama import Fore  # prints warnings in red


class Reader:
    """
        Class that reads a file and creates a CSV object.

        Arguments:
            docpath: Path to the input file
    """

    path: str
    type: str

    def __init__(self, docpath: str) -> None:
        self.path = docpath
        self.initialise_type()

    def initialise_type(self) -> None:
        self.type = self.path[self.path.rfind(".")+1:].lower()

        if len(self.type) > 4:
            raise Exception("Please enter a complete path with datatype-prefix!")

    def read(self) -> pd.DataFrame:
        """
            Reads the input and returns a CSV object.
        """

        if self.type == "csv":
            try:
                file = open(self.path, 'r', encoding='utf-8')
                return pd.read_csv(file)

            except FileNotFoundError:
                raise Exception("Warning: There is no CSV file on this path.")

        else:
            raise Exception("Warning: Unknown File-Type!")
        
        return pd.DataFrame({})