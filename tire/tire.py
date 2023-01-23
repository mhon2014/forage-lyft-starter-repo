from abc import ABC, abstractmethod

'''
Interface for tire class
'''

class Tire(ABC):

    @abstractmethod
    def needs_service(self)-> bool:
        pass