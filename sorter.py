import os, glob
import os.path as op
from rich import print
from rich.console import Console
from rich.table import Table

__app_name__ = "RoomCleaner"
__version__ = "0.0.1"


class FolderCleaner:
    _data: dict = {}
    _console = None
    result = None
    _cleaned = []

    def __init__(self, data: dict):
        self._data = data
        self._console = Console()
        self.result = Table("Target", "Result")

    @property
    def path(self):
        return self._data.get("path", "")

    @property
    def rules(self):
        return self._data.get("rules", [])

    def setup(self):
        os.chdir(op.expanduser(self.path))

    def setup_destination_dir(self, target):
        self._dest_dir = op.join(op.abspath(""), op.expanduser(target))
        if not op.exists(self._dest_dir):
            os.mkdir(self._dest_dir)

    def clean_file(self, _file):
        old_path = op.abspath(_file)
        new_path = op.join(self._dest_dir, _file)
        os.rename(old_path, new_path)
        self._cleaned.append((old_path, new_path))

    def show_result(self):
        self._console.print(self.result)
        for c in self._cleaned:
            print(f"{c[0]} ==> {c[1]}")

    def start(self):
        self.setup()
        print(f"Started cleaning with {len(self.rules)} rules")

        for target, patterns in self.rules.items():
            to_sorts = [file for pattern in patterns for file in glob.glob(pattern)]

            if not to_sorts:
                self.result.add_row(target, f"No match for patterns {patterns}")
                continue

            self.setup_destination_dir(target)

            self.result.add_row(
                target, f"{len(to_sorts)} files to clean for patterns {patterns}"
            )

            for to_sort in to_sorts:
                self.clean_file(to_sort)

        self.show_result()
