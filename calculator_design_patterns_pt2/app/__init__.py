from app.commands import CommandHandler
# from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.menu import MenuCommand
from app.commands.generate import GenerateCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        # put goodbye and exit command together
        # self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("generate", GenerateCommand())
        
        print("Type 'goodbye' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())