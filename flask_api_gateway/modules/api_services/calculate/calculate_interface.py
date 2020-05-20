from abc import ABCMeta, abstractmethod


class CalculateInterface(metaclass=ABCMeta):
    @abstractmethod
    def health_check_request(self):
        raise NotImplementedError

    @abstractmethod
    def calculate_request(self):
        raise NotImplementedError
