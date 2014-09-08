from subprocess import call

from commands.base import BaseCommand, action


class GitCommand(BaseCommand):

    def __init__(self, parser):
        subparser = parser.add_parser('git')
        subparser.add_argument('option', nargs='*')
        subparser.set_defaults(func=self.call_to_action)

    @action
    def pull(cls):
        """Git pull from the current branch"""

        # Print the pulling message
        print('Pulling with: git pull --prune')

        # Set the command string
        command = 'git pull --prune'

        # Run the command to git pull
        call(command, shell=True)

    @action
    def graph(cls):
        """Display a graph of commits in a tree view"""
        # Set the command string
        command = 'git log --graph'

        # Run the command to display the git graph
        call(command, shell=True)

    @action
    def log(cls):
        """Display a log of the commits"""
        # Set the command string
        command = ('git log --graph --pretty=format:\'%Cred%h%Creset %an: %s '
                   '- %Creset %C(yellow)%d%Creset %Cgreen(%cr)%Creset\' '
                   '--abbrev-commit --date=relative')

        # Run the command to display the git graph
        call(command, shell=True)

    @action
    def pushia(cls):
        """Git add everything, print status, commit, pull and push"""
        # Set the commands strings
        commands = ['git add .', 'git status -sb',
                    'git commit -a', 'pmgit git pull', 'git push']

        for command in commands:
            # Run every command on the list
            call(command, shell=True)
