"""Command-line interface for receipt_itemizer."""

import typer

from receipt_itemizer import __version__

app = typer.Typer(help="OCR and line-item parsing of receipts.")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        callback=_version_callback,
        is_eager=True,
        help="Show the version and exit.",
    ),
) -> None:
    """receipt-itemizer CLI."""


if __name__ == "__main__":
    app()
