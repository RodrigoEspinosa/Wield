from commands.base import BaseCommand, action
from models.profile import Profile


class ProfileCommand(BaseCommand):

    def __init__(self, parser):
        subparser = parser.add_parser('profile')
        subparser.add_argument('option', nargs='*')
        subparser.set_defaults(func=self.call_to_action)

    @action
    def new():
        Profile.create(name='Rodrigo')
