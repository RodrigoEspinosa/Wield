from commands.base import BaseCommand, action

"""
from wield.commands import BaseCommand
from wield.core.git import Git


class GitCommand(BaseCommand):

    @staticmethod
    def call(subcommand):
        # Get the method if exists
        git_method = getattr(Git, subcommand, None)

        # Check if the subcommand is indeed a method
        if callable(git_method):
            # Call the method
            git_method()
"""


class GitCommand(BaseCommand):

    def __init__(self, parser):
        subparser = parser.add_parser('git')
        subparser.add_argument('option', nargs='*')
        subparser.set_defaults(func=self.call_to_action)


    @action
    def pull():
        """Git command"""
        print 'hola'
