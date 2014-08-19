#! /usr/bin/env python
from __future__ import absolute_import  # noqa

# import sys
import argparse


from core.config import ConfigurationFile
from models.base import Borg

"""
from redmine import Redmine
from redmine import exceptions as redmine_exceptions

from commands import GitCommand
from core import Base, Core, Profile, Project
from messages import HelpMessages, ProfileMessages
from exceptions import ProfileDoesNotExist, ProjectDoesNotExist


class App(object):

    def __init__(self):
        # Parse the command line arguments
        self.args = self.args_parser()

        # Load the specificated profile
        self.profile = self.load_profile()

        try:
            # Check if 'help' is in the command arguments
            if self.args.main == 'help':
                HelpMessages.display_help()

            # Check if 'git' is in the command arguments
            if self.args.main == 'git':
                try:
                    GitCommand.call(sys.argv[sys.argv.index('git') + 1])

                except IndexError:
                    HelpMessages.display_git_help()

            # Get the redmine connection
            self.redmine = self.connect_to_redmine()

            # Set the actual project
            self.set_actual_project()

            # Set the core motor
            self.core = Core(redmine=self.redmine, profile=self.profile,
                             args=self.args)
            Base.core = self.core

            # Run the commands
            self.core.register()

        except redmine_exceptions.ServerError:
            print 'ServerError: Redmine returned internal error'

    def autodiscover_commands(self):
        from commands import __all__ as commands_all

        return [c.replace('_', '') for c in commands_all]

    def args_parser(self):
        # Create the parser and subparser instance
        self.parser = argparse.ArgumentParser()
        subparsers = self.parser.add_subparsers()

        # Add verbose optional argument
        self.parser.add_argument('-v', '--verbose', action='store_true',
                                 help='Increase output verbosity')

        # Add profile optional argument
        self.parser.add_argument('-p', '--profile', nargs=1, default='default',
                                 type=str, help='Specify a profile')

        # Add argument for creating a new profile with a prompt
        self.parser.add_argument('--new-profile', action='store_true',
                                 help='Specify a profile')

        # Get all the commands from the autodiscover
        commands = self.autodiscover_commands()

        # Add every command to the subparser
        for command in commands:
            print command
            subparsers.add_parser(command)

        args = self.parser.parse_args()

        return args

    def load_profile(self):
        # Check if the user wants to create a new profile
        if self.args.new_profile:
            # TODO Refactor the profile creation method
            sys.exit()

        # Check if the profile argument value is a list
        if type(self.args.profile) is list:
            # Set the profile to the first value
            self.args.profile = self.args.profile[0]

        try:
            # Load the the specificated profile
            self.profile = Profile().load(self.args.profile)

        except ProfileDoesNotExist:
            ProfileMessages.not_exist()
            sys.exit()

        # Return the ready profile
        return self.profile

    def connect_to_redmine(self):
        # Get the current profile
        profile = self.profile

        # Return the new redmine connection instance
        return Redmine(profile.host, username=profile.username,
                       password=profile.password)

    def set_actual_project(self):
        # Get the actual project from the enviroment
        try:
            project = Project()

        except ProjectDoesNotExist:
            # TODO Show prompt to create project
            print ('Looks like there is no project '
                   'referenced to the current directory')
            sys.exit()

        # Get the redmine project
        project = self.redmine.project.get(project.redmine_reference)
        # Set the self instance current project
        self.current_project = project

        # Return the project
        return project
"""


class App(Borg):

    def __init__(self, *args, **kwargs):
        ConfigurationFile().ensure_directory_exist()

        call_to_action = self.create_command_parser().parse_args()
        call_to_action.func(call_to_action)

        super(App, self).__init__(*args, **kwargs)

    def autodiscover_commands(self):
        import commands

        modules = map(__import__, ['commands.' + c for c in commands.__all__])

        response = []
        response.append(modules[0].git.GitCommand)
        response.append(modules[0].profile.ProfileCommand)

        return response

    def create_command_parser(self):
        # Create the parser and subparser instance
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers()

        commands = self.autodiscover_commands()

        for command in commands:
            command(subparsers)

        return parser

if __name__ == '__main__':
    app = App()
