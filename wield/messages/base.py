from getpass import getpass

from colorama import Fore, Style
from messages import console


class BaseMessages(object):
    palette = {'error': Fore.RED, 'success': Fore.GREEN, 'info': Fore.CYAN}

    @classmethod
    def error(cls, msg=''):
        style = cls.palette['error'] + Style.BRIGHT + 'Error: ' + Style.NORMAL
        return style + msg + Fore.RESET

    @classmethod
    def success(cls, msg=''):
        return cls.palette['success'] + msg + Fore.RESET

    @classmethod
    def info(cls, msg=''):
        return cls.palette['info'] + msg + Fore.RESET

    @classmethod
    def yes_no_prompt(msg, default='yes'):
        # Prompt the input with the message
        helper = 'Y/n' if default == 'yes' else 'y/N'
        val = raw_input(msg + ' ({}) '.format(helper))

        return val not in 'no'

    @classmethod
    def prompt(cls, func, msg, required=True, expected_type=str):
        while True:
            # Prompt the function with his message
            response = func(msg)

            # Check if the input is not empty
            is_empty = response.strip() == ''
            is_expected_type = response is expected_type

            # If required is True, repeat until the response is not empty
            # and has the expected type
            if not required or not (is_empty or is_expected_type):
                # Exit the loop
                break

            elif is_empty:
                # Print the empty response error
                cls.error('The response is required')

            elif is_expected_type:
                # Print the not expected type error
                cls.error('The response is not a {}'.format(expected_type))

        # Return the user response
        return response

    @classmethod
    def question(cls, msg, default=None, expected_type=str):
        # Append the question ending to the message
        msg += ': '
        return cls.prompt(raw_input, msg)

    @classmethod
    def question_url(cls, msg, default=None):
        # Prompt the question and get the user response
        response = cls.question(msg, default)

        # Check if the response starts with a http or https protocol
        if not response.startswith(('http://', 'https://')):
            # Add http as default protocol for the response
            response = 'http://' + response

        # Return the corrected response
        return response

    @classmethod
    def password(cls, msg, required=True):
        # Append the question ending to the message
        msg += ': '
        return cls.prompt(getpass, msg, required)

    @classmethod
    def table(cls, data):
        """ Based on https://gist.github.com/lonetwin/4721748 """

        # Get the console terminal size
        width, height = console.getTerminalSize()

        # Extend the headers with values in a list
        data.extend([i.values() for i in data])

        # - figure out column widths
        widths = [len(max(columns, key=len)) for columns in zip(*data)]

        # - print the header
        header, data = data[0], data[1:]
        print(' | '.join(format(title, '%ds' % width)
              for width, title in zip(widths, header)))

        # - print the separator
        print('-+-'.join('-' * width for width in widths))

        # - print the data
        for row in data:
            print(' | '.join(format(cdata, '%ds' % width)
                  for width, cdata in zip(widths, row)))

    @classmethod
    def choose(cls, msg, options):
        # Print the title message
        print msg

        # Print each option
        for i in range(len(options)):
            print '{:>4} - {}'.format(str(i + 1), options[i])

        # Set a loop controler. Number of posible tries.
        i = 10

        while True:
            # Decrese the loop controler.
            i -= 1

            # Loop controler check. If there is no tries left, break the loop.
            if i < 0:
                break

            # Get for the user input
            response = raw_input()

            if int(response) < len(options) + 1:
                return options[i - 1]

            cls.error('The input is not on the range. Try again.')

        return None
