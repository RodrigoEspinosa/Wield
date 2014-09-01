import subprocess


class Git(object):

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
