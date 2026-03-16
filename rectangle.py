from shape import Shape

class Rectangle(Shape):

    def __init__(self, pikkus, kõrgus):
        self.pikkus = pikkus
        self.kõrgus = kõrgus

    @property
    def area(self):
        return self.pikkus * self.kõrgus

    def __str__(self):
        return f"Rectangle(width={self.pikkus}, height={self.kõrgus})"