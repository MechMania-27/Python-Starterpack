class position:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

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