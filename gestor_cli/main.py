import click
from . import pessoas, produtividade, ia
from .ui import console, show_menu


def main():
    while True:
        show_menu("🙋 GESTOR CLI  - v0.1.0", ["Pessoas", "Produtividade", "IA", "Sair"])

        opcao = click.prompt("Escolha uma opção", type=int)

        if opcao == 1:
            pessoas.menu()
        elif opcao == 2:
            produtividade.menu()
        elif opcao == 3:
            ia.menu()
        elif opcao == 0:
            console.print("\n[bold yellow]Saindo... até logo![/]")
            break
        else:
            console.print("[red]Opção inválida.[/]")
            click.pause()


if __name__ == "__main__":
    main()
