from colorama import Fore, Style

from messages.base import BaseMessages
from messages.console import getTerminalSize


class HelpMessages(BaseMessages):

    @classmethod
    def command_help(cls, name, help):
        # Get the terminal width
        width, height = getTerminalSize()

        # Set the column width to be the halt of the console width
        column_width = width // 2

        # Set the command name and help format
        command_format = ('{:>' + str(column_width) + '} '
                          '{:<' + str(column_width) + '}')

        # Get the command name and help string with the command format
        msg = command_format.format(Style.BRIGHT + name + Style.NORMAL,
                                    Fore.YELLOW + help + Fore.RESET)

        # Return the centered command name and string with it format
        return ('{:^' + str(width) + '}').format(msg)
