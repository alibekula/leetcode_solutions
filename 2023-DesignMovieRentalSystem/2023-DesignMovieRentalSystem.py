# Last updated: 23.09.2025, 16:40:32
from collections import defaultdict
from sortedcontainers import SortedList

class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.price = {}
        self.stock = defaultdict(SortedList)
        self.rented = SortedList()
        
        for shop, movie, p in entries:
            self.price[(shop, movie)] = p
            self.stock[movie].add((p, shop))
    
    def search(self, movie: int) -> list[int]:
        return [shop for p, shop in self.stock[movie][:5]]
    
    def rent(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        self.stock[movie].remove((p, shop))
        self.rented.add((p, shop, movie))
    
    def drop(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        self.rented.remove((p, shop, movie))
        self.stock[movie].add((p, shop))
    
    def report(self) -> list[list[int]]:
        return [[shop, movie] for p, shop, movie in self.rented[:5]]
