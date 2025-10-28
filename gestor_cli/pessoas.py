import click
from .ui import console, show_menu, pause


def menu():
    while True:
        show_menu(
            "=== Menu Pessoas ===",
            ["Listar membros do time", "Gerar matriz de skills", "Voltar"],
        )

        opcao = click.prompt("Escolha uma opção", type=int)

        if opcao == 1:
            console.print("[bold]Listando membros do time...[/]")
            pause()
        elif opcao == 2:
            console.print("[bold]Gerando matriz de skills...[/]")
            pause()
        elif opcao == 3:
            break
        else:
            console.print("[red]Opção inválida.[/]")
            pause()
