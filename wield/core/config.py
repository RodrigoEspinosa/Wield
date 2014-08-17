from __future__ import absolute_import  # noqa

import os
import json

try:
    from wield.exceptions import NoConfigurationFileError
except ImportError:
    pass


class ConfigurationFile(object):

    CONFIGURATION_DIRECTORY_NAME = '.wield'
    DEFAULT_CONFIGURATION_FILE_NAME = 'wield.json'

    conf_directory = None
    conf_filename = None

    def __init__(self, **kwargs):
        # Get the configuration directory
        self.conf_directory = os.path.join(os.getenv('HOME'),
                                           self.CONFIGURATION_DIRECTORY_NAME)

        # Get the configuration file
        if 'filename' in kwargs:
            self.conf_filename = kwargs['filename']
        else:
            self.conf_filename = self.DEFAULT_CONFIGURATION_FILE_NAME

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

    def ensure_directory_exist(self):
        # Check if the directory exists
        if not os.path.exists(self.conf_directory):
            # Create the configuration directory
            os.makedirs(self.conf_directory)

    def create_file(self, content):
        # Ensure the directory exist. If not create it.
        self.ensure_directory_exist()

        # Open the new file
        with open(self.conf_file, 'w') as conf:
            conf.write(content)
