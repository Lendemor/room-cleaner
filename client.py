import os.path as op
import typer
import yaml
from yaml import Loader
from typing import Any
from sorter import FolderCleaner, __app_name__, __version__, start_cleaning
from rich import print

app = typer.Typer()


class Config:
    file: str
    data: dict[str, Any]

    def __init__(self) -> None:
        self.file = "cleaners.yaml"
        with open(self.file) as stream:
            self.data = yaml.load(stream, Loader=Loader)

    @property
    def cleaners(self):
        return list(self.data.keys())

    def get_cleaner(self, cleaner_name: str) -> dict:
        if cleaner_name in self.cleaners:
            return FolderCleaner(self.data.get(cleaner_name, {}))


@app.command()
def cleaners():
    conf = Config()
    print(f"Available cleaners (defined in {op.abspath(conf.file)}):")
    for cleaner in conf.cleaners:
        print(f"    - [bold yellow]{cleaner}[/bold yellow]")


@app.command()
def clean(cleaner_name: str):
    conf = Config()

    cleaner = conf.get_cleaner(cleaner_name)
    if not cleaner:
        print("[red]Unknown cleaner[/red]:\n")
        cleaners()
        exit()

    print(
        f"Starting cleaner [bold yellow]{cleaner_name}[/bold yellow] in {cleaner.path}"
    )
    cleaner.start()


@app.command()
def verify():
    print("[red]NOT IMPLEMENTED[/red]")
    print("Will check for conflict in cleaners.yaml")


if __name__ == "__main__":
    app()
