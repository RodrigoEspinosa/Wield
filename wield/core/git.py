import subprocess


class Git(object):

    @staticmethod
    def pull():
        """Git pull from the current branch"""
        # Print the pulling message
        print 'Pulling with: git pull --prune'

        # Set the command string
        command = 'git pull --prune'

        # Run the command to git pull
        subprocess.call(command, shell=True)

    @staticmethod
    def graph():
        """Display a graph of commits in a tree view"""
        # Set the command string
        command = 'git log --graph'

        # Run the command to display the git graph
        subprocess.call(command, shell=True)

    @staticmethod
    def log():
        """Display a log of the commits"""
        # Set the command string
        command = ('git log --graph --pretty=format:\'%Cred%h%Creset %an: %s '
                   '- %Creset %C(yellow)%d%Creset %Cgreen(%cr)%Creset\' '
                   '--abbrev-commit --date=relative')

        # Run the command to display the git graph
        subprocess.call(command, shell=True)

    @staticmethod
    def pushia():
        """Git add everything, print status, commit, pull and push"""
        # Set the commands strings
        commands = ['git add .', 'git status -sb',
                    'git commit -a', 'pmgit git pull', 'git push']

        for command in commands:
            # Run every command on the list
            subprocess.call(command, shell=True)

    @staticmethod
    def create_new_feature(name):
        # Print the creating branch message
        print 'Creating new feature branch {}'.format(name)

        # Set the command string
        command = 'git flow feature start {}'.format(name)

        # Run the command to create a hotfix
        subprocess.call(command, shell=True)

    @staticmethod
    def create_new_hotfix(name):
        # Print the creating branch message
        print 'Creating new hotfix branch {}'.format(name)

        # Set the command string
        command = 'git flow hotfix start {}'.format(name)

        # Run the command to create a hotfix
        subprocess.call(command, shell=True)

    @staticmethod
    def finish_feature(name):
        # Set the command string
        command = 'git flow feature finish {}'.format(name)

        # Run the command to create a hotfix
        subprocess.call(command, shell=True)

    @staticmethod
    def finish_hotfix(name):
        # Set the command string
        command = 'git flow hotfix finish {}'.format(name)

        # Run the command to create a hotfix
        subprocess.call(command, shell=True)
