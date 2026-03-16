from rectangle import Rectangle
from square import Square

if __name__ == "__main__":

    r = Rectangle(2, 3) # <-- Muuda seda jama, et saada teine ruut
    s = Square(5) # <-- See ka!

    print(r)
    print(s)

    print(f"Rectangle area: {r.area}")
    print(f"Square area: {s.area}")