class Position:
    def __init__(self, x = -1, y = -1, **kwargs) -> None:
        if x != -1 and y != -1:
            self.x = x
            self.y = y
        elif kwargs:
            self.x = kwargs.get('pos_dict')['x']
            self.y = kwargs.get('pos_dict')['y']
    
    def getpos(self, x, y):
        return x, y

    def __eq__(self, o: object) -> bool:
        if object is None:
            return False
        if type(object) != type(self):
            return False
        return (self.x, self.y) == object.getpos()

    def __str__(self) -> str:
        return f"{self.x} {self.y}"