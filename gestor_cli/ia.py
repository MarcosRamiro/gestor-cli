import click

def menu():
    while True:
        click.clear()
        click.echo(click.style("=== Menu IA 🤖 ===", fg="magenta", bold=True))
        click.echo("1. Gerar resumo inteligente")
        click.echo("2. Voltar\n")

        opcao = click.prompt("Escolha uma opção", type=int)

        if opcao == 1:
            click.echo("Gerando resumo usando IA (simulação)...")
            click.echo("👉 'Resumo: nova jornada de login aumentou conversão em 12%.'")
            click.pause()
        elif opcao == 2:
            break
        else:
            click.echo("Opção inválida.")
            click.pause()

