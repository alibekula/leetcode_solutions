# Last updated: 09.10.2025, 17:18:05
from typing import List
import math

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def cross(o: Point, a: Point, b: Point) -> int:
    # безопасное вычисление в 128-битном диапазоне
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def convex_hull_from_sorted(pts: List[Point]) -> List[Point]:
    n = len(pts)
    if n <= 1:
        return pts[:]

    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # удаляем последнюю точку, чтобы не дублировать
    lower.pop()
    upper.pop()
    return lower + upper


def max_dot_on_convex_polygon(hull: List[Point], A: int, B: int) -> int:
    H = len(hull)

    def val(i: int) -> int:
        return hull[i].x * A - hull[i].y * B

    # brute-force для малых оболочек
    if H <= 64:
        return max(val(i) for i in range(H))

    # тернарный поиск по индексу
    l, r = 0, H - 1
    while r - l > 3:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        if val(m1) < val(m2):
            l = m1
        else:
            r = m2

    return max(val(i) for i in range(l, r + 1))


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        if n == 0 or m == 0:
            return 0

        # префиксные суммы
        T = [0] * n
        T[0] = skill[0]
        for i in range(1, n):
            T[i] = T[i - 1] + skill[i]

        # точки P_j = (T_j, T_{j-1})
        pts = [Point(T[j], 0 if j == 0 else T[j - 1]) for j in range(n)]

        # оболочка
        hull = convex_hull_from_sorted(pts)

        cur_t = 0
        for i in range(1, m):
            A = mana[i - 1]
            B = mana[i]
            t = max_dot_on_convex_polygon(hull, A, B)
            cur_t += t

        return cur_t + T[-1] * mana[-1]
