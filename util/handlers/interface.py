from abc import ABC, abstractmethod

from interface import ArgConfig


class IHandler(ABC):
    def __init__(self, action: str):
        self.action = action

    @abstractmethod
    def handle(self, config: ArgConfig):
        raise NotImplementedError()
