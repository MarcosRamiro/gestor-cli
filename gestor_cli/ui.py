from __future__ import annotations

from typing import Sequence
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_menu(title: str, options: Sequence[str]) -> None:
    """Clear the screen and show a centered panel title and numbered options."""
    console.clear()
    console.print(Panel(f"[bold]{title}[/]", style="cyan"), justify="center")

    table = Table(box=None, show_header=False, pad_edge=False)
    table.add_column("#", style="bold green", width=4)
    table.add_column("option")

    options_aux = options[:-1]
    ultimo_item = options[-1]
    options = options_aux

    for i, opt in enumerate(options, start=1):
        table.add_row(f"{i}.", opt)
    else:
        table.add_row("0.", ultimo_item)

    console.print(table)
    console.print()


def pause() -> None:
    """Pause the program (delegates to click.pause to keep behavior)."""
    click.pause()
