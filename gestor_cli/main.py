import click
from . import pessoas, produtividade, ia

def main():
    while True:
        click.clear()
        click.echo(click.style("========================", fg="cyan"))
        click.echo(click.style(" CENTRAL CLI - v0.1.0", fg="yellow", bold=True))
        click.echo(click.style("========================\n", fg="cyan"))

        click.echo("1. Pessoas")
        click.echo("2. Produtividade")
        click.echo("3. IA")
        click.echo("4. Sair\n")

        opcao = click.prompt("Escolha uma opção", type=int)

        if opcao == 1:
            pessoas.menu()
        elif opcao == 2:
            produtividade.menu()
        elif opcao == 3:
            ia.menu()
        elif opcao == 4:
            click.echo("\nSaindo... até logo!")
            break
        else:
            click.echo("Opção inválida.")
            click.pause()
