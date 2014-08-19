from commands.base import BaseCommand, action


class ProfileCommand(BaseCommand):

    def __init__(self, parser):
        subparser = parser.add_parser('profile')
        subparser.add_argument('option', nargs='*')
        subparser.set_defaults(func=self.call_to_action)

    @action
    def new():
        raise NotImplementedError()
