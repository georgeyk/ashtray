from xdg.DesktopEntry import DesktopEntry
from xdg.IconTheme import getIconPath

from ashtray.ui import TrayItem

import click


@click.group()
def cli():
    return 0


@cli.command()
@click.option(
    "-f",
    "--file",
    "desktop_file",
    default=None,
    help="Path to .desktop file",
    type=click.Path(exists=True)
)
def desktop(desktop_file):
    entry = DesktopEntry(desktop_file)
    icon_path = getIconPath(entry.getIcon())
    command = entry.getTryExec() or entry.getExec()

    TrayItem(icon_path, command).start()


if __name__ == "__main__":
    cli()
