from abc import ABCMeta, abstractmethod

class CalculateInterface(metaclass=ABCMeta):
    @abstractmethod
    def health_check(self):
        raise NotImplementedError

    @abstractmethod
    def calculate(self):
        raise NotImplementedError
