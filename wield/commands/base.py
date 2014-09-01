from messages.help import HelpMessages

# Initialize the actions descriptions as an empty list
actions_list = []


# Action decorator for command methods
def action(func=None):
    if func is None:
        return func

    # Append the command description to the actions list
    actions_list.append((func.__name__, func.__doc__))

    # Set the function to be a class method
    return classmethod(func)


class BaseCommand(object):

    def __init__(self, parser):
        # Require the command to implement a contructor with a parser argument
        raise NotImplementedError()

    @action
    def help(cls):
        """Print this message"""

        # Get each command with his help from the action list
        for name, help in actions_list:
            # Check if the command exists on the current class
            if hasattr(cls, name):
                # Print the commmand with the help command format
                print HelpMessages.command_help(name, help)

    def call_to_action(self, action):
        # Check if there is no option selected and the class has a help method
        if not action.option and hasattr(self, 'help'):
            # Call the help method
            self.help()

        # Loop through each argument option which method is defined
        for opt in [i for i in action.option if hasattr(self, i)]:
            # Call the argument option method
            getattr(self.__class__, opt)()
