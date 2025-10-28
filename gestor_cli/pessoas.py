import click

def menu():
    while True:
        click.clear()
        click.echo(click.style("=== Menu Pessoas ===", fg="green", bold=True))
        click.echo("1. Listar membros do time")
        click.echo("2. Gerar matriz de skills")
        click.echo("3. Voltar\n")

        opcao = click.prompt("Escolha uma opção", type=int)

        if opcao == 1:
            click.echo("Listando membros do time...")
            click.pause()
        elif opcao == 2:
            click.echo("Gerando matriz de skills...")
            click.pause()
        elif opcao == 3:
            break
        else:
            click.echo("Opção inválida.")
            click.pause()

