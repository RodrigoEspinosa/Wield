from models.profile import Profile
from messages.profile import ProfileMessages
from commands.base import BaseCommand, action


class ProfileCommand(BaseCommand):

    def __init__(self, parser):
        subparser = parser.add_parser('profile')
        subparser.add_argument('option', nargs='*')
        subparser.set_defaults(func=self.call_to_action)

    @action
    def new(cls):
        response = ProfileMessages.create_prompt()

        if 'name' not in response:
            response['name'] = 'default'

        Profile.create(**response)

    @action
    def list(cls):
        # Print a table list with every profile
        ProfileMessages.list(Profile.all())
