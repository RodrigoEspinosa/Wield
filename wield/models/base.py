import json
from os import path

from core.config import ConfigurationFile


class Model(object):

    __json_file = None
    __dict_file = None

    def __init__(self, *args, **kwargs):
        for item in kwargs:
            setattr(self, item, kwargs[item])

    def __get_or_create_file(self, create=False):
        # Get the configuration file instance for the configuration directory
        configuration_file = ConfigurationFile()

        # Get the filename based on the model class name
        filename = self.__class__.__name__.lower() + '.json'

        # Set the absolute path for the file
        absolute_path = path.join(configuration_file.conf_directory, filename)

        # Set the opening mode for the file
        open_mode = 'r' if not create else 'w'

        with open(absolute_path, open_mode) as json_data:
            if create:
                print self.__json_model
                json_data.write(self.__json_model)
            else:
                self.__dict_file = json.loads(json_data)

            json_data.close()

    def __create_model_dict(self):
        attrs = {}
        for item in dir(self):
            value = getattr(self, item)
            if not item.startswith('_') and not callable(value):
                attrs[item] = value
        return attrs

    def __add_model_to_dict_file(self):
        model_dict = self.__create_model_dict()

        if self.__dict_file is None:
            self.__dict_file = []

        self.__dict_file.append(model_dict)

    def __render_dict_file_to_json(self):
        self.__add_model_to_dict_file()
        self.__json_model = json.dumps(self.__dict_file, indent=4)

    def save(self):
        self.__render_dict_file_to_json()
        self.__get_or_create_file(True)

    def remove(self, *args, **kwargs):
        model_dict = self.__create_model_dict()
        self.__dict_file.remove(model_dict)

    @classmethod
    def create(cls, *args, **kwargs):
        instance = cls(*args, **kwargs)
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

    def __str__(self):
        return self.state
