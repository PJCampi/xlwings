from framework import Converter, accessors


OBJECT_ID = 'object_id'


class KeyValuePair(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class ObjectConverter(Converter):

    cache = {}

    @classmethod
    def read_value(cls, value, options):
        try:
            return cls.cache[value]
        except KeyError:
            raise KeyError('Object of id {} is not not present in the object cache.'.format(value))

    @classmethod
    def write_value(cls, key_val, options):

        if not isinstance(key_val, KeyValuePair):
            raise TypeError("The return value must be of type {}.".format(KeyValuePair.__name__))

        cls.cache[key_val.key] = key_val.value
        return key_val.key


accessors.register(object, ObjectConverter)
