def action(func=None):
    if func is not None:
        return staticmethod(func)

    return func


class BaseCommand(object):

    def __init__(self, parser):
        raise NotImplementedError()

    def call_to_action(self, action):
        for opt in [i for i in action.option if hasattr(self, i)]:
            getattr(self.__class__, opt)()
