from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)                 # add to back
        # rotate every earlier element behind the new one,
        # so the new element ends up at the FRONT
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()          # front is the newest → LIFO

    def top(self) -> int:
        return self.q[0]                 # peek front only

    def empty(self) -> bool:
        return len(self.q) == 0