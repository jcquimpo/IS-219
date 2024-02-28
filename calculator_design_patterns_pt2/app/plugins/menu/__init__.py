import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print(f'List of all commands: ')
        print(f'greet')
        print(f'goodbye')
        print(f'menu')
        print(f'generate')