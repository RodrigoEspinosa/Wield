def action(func=None):
    if func is None:
        return func

    # Set the function to be a class method
    return classmethod(func)


class BaseCommand(object):

    def __init__(self, parser):
        # Require the command to implement a contructor with a parser argument
        raise NotImplementedError()

    @action
    def help(cls):
        print 'help'

    def call_to_action(self, action):
        # Check if there is no option selected and the class has a help method
        if not action.option and hasattr(self, 'help'):
            # Call the help method
            self.help()

        # Loop through each argument option which method is defined
        for opt in [i for i in action.option if hasattr(self, i)]:
            # Call the argument option method
            getattr(self.__class__, opt)()
