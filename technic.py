from functools import total_ordering


@total_ordering
class Technic:
    __slots__ = ["title", "price", "availability"]

    def __init__(self, title: str, price: int, availability: bool):
        self.title = title
        self.price = price
        self.availability = availability

    def category(self):
        return 'Cheap' if 0 <= self.price <= 50000 else 'Expensive'

    def __eq__(self, other):
        if not isinstance(other, Technic):
            raise NotImplemented
        return len(self.title) == len(other.title)

    def __lt__(self, other):
        if not isinstance(other, Technic):
            raise NotImplemented
        return len(self.title) < len(other.title)
