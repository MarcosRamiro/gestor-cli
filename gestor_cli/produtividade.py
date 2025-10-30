import click
import time
from .ui import console, show_menu, pause


def menu():
    while True:
        show_menu("=== Menu Produtividade ===", ["Iniciar foco (25 min)", "Voltar"])

        opcao = click.prompt("Escolha uma opção", type=int)

        if opcao == 1:
            console.print("[bold]Iniciando foco de 25 minutos...[/]")
            for i in range(5):  # simulação curta pra teste
                console.print(f"{i + 1} minuto(s)...")
                time.sleep(1)
            console.print("[yellow]Tempo encerrado! Faça uma pausa. ☕[/]")
            pause()
        elif opcao == 0:
            break
        else:
            console.print("[red]Opção inválida.[/]")
            pause()
