from getpass import getpass

from messages.base import BaseMessages


class ProfileMessages(BaseMessages):
    """ List of messages for profile """

    @staticmethod
    def no_configuration():
        print 'Aww men! There is no configuration file yet!'
        print 'I\'m going to create one now.'

    @classmethod
    def not_exist(cls):
        print cls.error('The profile does not exists')

    @staticmethod
    def create_prompt():
        # Initialize the user reponse dictionary
        response = {}

        # Prompt the username and password form
        response['username'] = raw_input('@ Tell me your redmine username: ')
        response['password'] = getpass('# Thanks! Now your redmine password: ')
        response['host'] = raw_input('Yey! What\'s the redmine host (http://..): ')

        if not response['host'].startswith(('http://', 'https://')):
            # Add the http to the host
            response['host'] = 'http://' + response['host']

        return response
