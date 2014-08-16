import json


class Model(object):

    __json_file = None
    __dict_file = None

    def __init__(self, *args, **kwargs):
        for item in kwargs:
            setattr(self, item, kwargs[item])

    def __get_or_create_file(self):
        filename = self.__class__.__name__.lower() + '.json'

        with open(filename, 'r') as json_data:
            self.__dict_file = json.loads(json_data)
            json_data.close()

    def __create_model_dict(self):
        attrs = {}
        for item in dir(self):
            value = getattr(self, item, None)
            if not value.startswith('__') and not value.callable():
                attrs[item] = value
        return attrs

    def __add_model_to_dict_file(self):
        model_dict = self.__create_model_dict()
        self.__dict_file.append(model_dict)

    def __render_dict_file_to_json(self):
        self.__add_model_to_dict_file()
        self.__json_model = json.dumps(self.__dict_file, indent=4)

    def save(self):
        # TODO Check model rules
        self.__render_dict_file_to_json()

    def remove(self, *args, **kwargs):
        model_dict = self.__create_model_dict()
        self.__dict_file.remove(model_dict)

    @classmethod
    def create(cls, *args, **kwargs):
        instance = cls.__init__(*args, **kwargs)
        instance.save()

    @classmethod
    def get(cls, *args, **kwargs):
        instance = cls()
        instance.__get_or_create_file()

        if len(kwargs) > 0:
            return

        for entry in cls.__dict_file:
            count = len(kwargs)
            for attr, value in kwargs.iteritems():
                if entry.getattr(attr, None) == value:
                    count -= 1

                if count == 0:
                    instance.__dict__ = entry

        return instance

    @classmethod
    def delete(cls, *args, **kwargs):
        cls.get(*args, **kwargs).remove()


class Borg(object):

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state
