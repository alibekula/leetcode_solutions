# Last updated: 07.10.2025, 19:09:03
import bisect

class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [1] * n
        zeros = []             # индексы дней без дождя (аналог set<int> st)
        last_rain = {}         # {озеро: последний день дождя}

        for i, lake in enumerate(rains):
            if lake == 0:
                bisect.insort(zeros, i)  # поддерживаем отсортированные индексы
            else:
                ans[i] = -1
                if lake in last_rain:
                    # ищем день с 0, который > последнего дождя
                    idx = bisect.bisect_right(zeros, last_rain[lake])
                    if idx == len(zeros):  # нет подходящего дня для сушки
                        return []
                    dry_day = zeros.pop(idx)  # день, когда сушим
                    ans[dry_day] = lake
                last_rain[lake] = i
        return ans
