from shape import Shape

class Square(Shape):

    def __init__(self, suurus):
        self.suurus = suurus

    @property
    def area(self):
        return self.suurus * self.suurus

    def __str__(self):
        return f"Square(size={self.suurus})"