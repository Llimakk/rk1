from abc import ABC, abstractmethod
class Geom(ABC):
    @abstractmethod
    def get_area(self):
        ...

    @abstractmethod
    def repr(self):
        ...
