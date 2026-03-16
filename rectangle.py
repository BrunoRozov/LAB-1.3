from shape import Shape

class Rectangle(Shape):

    def __init__(self, pikkus, kõrgus):
        self.pikkus = pikkus
        self.kõrgus = kõrgus

    @property
    def area(self):
        return self.pikkus * self.kõrgus

    def __str__(self):
        return f"Rectangle(pikkus={self.pikkus}, kõrgus={self.kõrgus})" # <-- Eta width ja eta height == pikkus ja suurus BLAAAAA ALALALALALALLALA ÄLVEEEE!!!