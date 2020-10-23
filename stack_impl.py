class Stack:
    def __init__(self):
        self.stk = []

    def push(self,item):
        self.stk.append(item)

    def is_empty(self):
        return self.stk == []

    def pop(self):
        return self.stk.pop()

    def size(self):
        return len(self.stk)

    def peek(self):
        return self.stk[len(self.stk) - 1]


m = Stack()
print(m.push('x'))
print(m.push('y'))
print(m.push('z'))
while not m.is_empty():
    print(m.pop())
    print(m.pop())
