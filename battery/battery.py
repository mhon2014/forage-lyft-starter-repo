from abc import ABC, abstractmethod

'''
Interface for battery class
'''


class Battery(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass
