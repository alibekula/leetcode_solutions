# Last updated: 18.09.2025, 21:30:10
import heapq
from typing import List

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.heap = []  # (-priority, -taskId, taskId, userId)
        self.task_info = {}  # taskId -> (priority, userId)

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId, taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        _, userId = self.task_info[taskId]
        self.task_info[taskId] = (newPriority, userId)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, negTaskId, taskId, userId = heapq.heappop(self.heap)
            if taskId in self.task_info:
                curPriority, curUser = self.task_info[taskId]
                if curPriority == -priority and curUser == userId:
                    del self.task_info[taskId]
                    return userId
        return -1
