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
