class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] = self.points.get((x, y), 0) + 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (px, py), cnt_diag in self.points.items():
            if px == x or py == y:
                continue
            if abs(px - x) != abs(py - y):
                continue

            c1 = self.points.get((x, py), 0)
            c2 = self.points.get((px, y), 0)
            total += cnt_diag * c1 * c2

        return total
