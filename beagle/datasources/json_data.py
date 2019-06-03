import os
import json
from typing import Dict, Generator, List

from beagle.datasources.base_datasource import DataSource
from beagle.transformers import GenericTransformer


class JSONData(DataSource):
    """A generic data source which returns events from a JSON file.
    """

    name = "JSON Data"
    transformers = [GenericTransformer]
    category = "Generic Data"

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def metadata(self) -> dict:
        return {"filename": os.path.basename(self.file_path)}

    def events(self) -> Generator[dict, None, None]:

        handle = open(self.file_path)

        first_char = handle.read(1)

        handle.seek(0)

        if first_char == "[":
            data: List[Dict] = json.load(open(self.file_path))

            for event in data:
                yield event
        else:
            for line in open(self.file_path).readlines():
                yield json.loads(line)
