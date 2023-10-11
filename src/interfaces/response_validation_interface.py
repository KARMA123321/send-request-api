import abc


class ResponseValidationInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "schema") and callable(subclass.schema)

    @abc.abstractmethod
    def schema(self, schema):
        raise NotImplementedError
