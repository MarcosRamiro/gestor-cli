import click
from .ui import console, show_menu, pause
from .util.configuration_db import get_config


def menu():
    while True:
        show_menu("=== 🤖 Menu IA ===", ["Gerar resumo inteligente", "Voltar"])

        opcao = click.prompt("Escolha uma opção", type=int)

        if opcao == 1:
            console.print("[bold]Gerando resumo usando IA (simulação)...[/]")

            resumo = get_config("ultimo_resumo_ia")
            if resumo:
                console.print(f"👉 [italic]Resumo salvo anteriormente: '{resumo}'[/]")
            else:
                console.print(
                    "👉 [italic]'Resumo: nova jornada de login aumentou conversão em 12%.'[/]"
                )
            # set_config("ultimo_resumo_ia", "Resumo: nova jornada de login aumentou conversão em 12%.")
            pause()
        elif opcao == 0:
            break
        else:
            console.print("[red]Opção inválida.[/]")
            pause()
