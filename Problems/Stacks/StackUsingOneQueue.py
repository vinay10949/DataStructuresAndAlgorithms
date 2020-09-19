
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.q.append(x)
        q_len = len(self.q)
        while q_len > 1:
            self.q.append(self.q.popleft())
            q_len -= 1
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self):
        """
        Get the top element.
        """
        return self.q[0]
        

    def empty(self) :
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0
