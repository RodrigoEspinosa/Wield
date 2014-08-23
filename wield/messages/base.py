from colorama import Fore, Style


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
    def question(cls, msg, default=None, expected_type=str):
        question = raw_input(msg)

        if question.strip() == '':
            return default

        if question.strip() is expected_type:
            return question.strip()
        else:
            cls.error('The response is not a {}'.format(expected_type))

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
