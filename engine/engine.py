from abc import ABC, abstractmethod

'''
Interface for engine class
'''

class Engine(ABC):

    @abstractmethod
    def needs_service(self)-> bool:
        pass
