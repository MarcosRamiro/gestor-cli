import click
import time

def menu():
    while True:
        click.clear()
        click.echo(click.style("=== Menu Produtividade ===", fg="blue", bold=True))
        click.echo("1. Iniciar foco (25 min)")
        click.echo("2. Voltar\n")

        opcao = click.prompt("Escolha uma opção", type=int)

        if opcao == 1:
            click.echo("Iniciando foco de 25 minutos...")
            for i in range(5):  # simulação curta pra teste
                click.echo(f"{i+1} minuto(s)...")
                time.sleep(1)
            click.echo(click.style("Tempo encerrado! Faça uma pausa. ☕", fg="yellow"))
            click.pause()
        elif opcao == 2:
            break
        else:
            click.echo("Opção inválida.")
            click.pause()