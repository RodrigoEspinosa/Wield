import os

from messages.base import BaseMessages


class ProjectMessages(BaseMessages):
    """ List of messages for project """

    @staticmethod
    def no_configuration():
        print 'What? Looks like there are no projects for you yet!'
        print 'I\'m going to create the project file now.'

    @staticmethod
    def create_prompt():
        # Prompt the username and password form
        name = raw_input('Tell me your project name: ')
        redmine = raw_input('# Thanks! Now what is project name on redmine: ')
        dire = raw_input('Yey! Is this the root to your project: ')

        # Check if the project directory input is blank
        if dire.strip() == '':
            # Set the project directory to the actual directory
            dire = os.getcwd()

        return (name, redmine, dire)
