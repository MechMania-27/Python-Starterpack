from abc import ABCMeta, abstractmethod

class ActionDecision(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        pass

    @abstractmethod
    def engine_str(self) -> str:
        pass
