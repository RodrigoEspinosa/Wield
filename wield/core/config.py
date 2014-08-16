import os
import json

from pmgit.exceptions import NoConfigurationFileError


class ConfigurationFile(object):
    conf_directory = None
    conf_filename = None

    def __init__(self, **kwargs):
        # Get the configuration directory
        self.conf_directory = os.path.join(os.getenv('HOME'), '.pmgit')

        # Get the configuration file
        if 'filename' in kwargs:
            self.conf_filename = kwargs['filename']
        else:
            self.conf_filename = 'pmgit.json'

        # Get the configuration file
        self.conf_file = os.path.join(self.conf_directory, self.conf_filename)

    def load_file(self):
        if not os.path.isfile(self.conf_file):
            # Raise an exception
            raise NoConfigurationFileError()

        # Open the configuration file
        with open(self.conf_file) as conf:
            self.data = json.load(conf)
            # Return the dictionary with the parse json data
            return self.data

    def create_file(self, content):
        # Check if the directory exists
        if not os.path.exists(self.conf_directory):
            # Create the configuration directory
            os.makedirs(self.conf_directory)

        # Open the new file
        with open(self.conf_file, 'w') as conf:
            conf.write(content)
