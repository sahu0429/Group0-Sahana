
from rich.console import Console
from rich.table import Table

from .client import fetch_live_data

console = Console()


def main():
    try:
        result = fetch_live_data()

        table = Table(title="Stripe Account Balance")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")

        for key, value in result.items():
            table.add_row(key.replace("_", " ").title(), str(value))

        console.print(table)

    except Exception as error:
        console.print(f"[bold red]Error:[/bold red] {error}")


if __name__ == "__main__":
    main()
