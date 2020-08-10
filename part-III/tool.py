"""
Usage:
python tool.py add -x 1 -y 2
"""
import click

@click.group()
def cli():
    pass

@cli.command('add')
@click.option('-x')
@click.option('-y')
def add(x, y):
    print(int(x) + int(y))

if __name__ == '__main__':
    cli()
