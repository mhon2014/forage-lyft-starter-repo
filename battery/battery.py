from abc import ABC, abstractmethod

from datetime import datetime

'''
Interface for battery class
'''


class Battery(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass