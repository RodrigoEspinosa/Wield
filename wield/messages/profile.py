from messages.base import BaseMessages


class ProfileMessages(BaseMessages):
    """ List of messages for profile """

    username_msg = '@ Tell me your redmine username'
    password_msg = '# Thanks! Now your redmine password'
    host_msg = 'Yey! What\'s the redmine host (http://..)'

    @staticmethod
    def no_configuration():
        print 'Aww men! There is no configuration file yet!'
        print 'I\'m going to create one now.'

    @classmethod
    def not_exist(cls):
        print cls.error('The profile does not exists')

    @classmethod
    def create_prompt(cls):
        # Initialize the user reponse dictionary
        response = {}

        # Prompt the username, password and host form
        response['username'] = cls.question(cls.username_msg)
        response['password'] = cls.password(cls.password_msg)
        response['host'] = cls.question_url(cls.host_msg)

        # Return the response dictonary
        return response
