class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    def push(self, item):
        self.stack.append(item) # 添加元素
        self.size += 1 # 栈元素数量加 1
    def pop(self):
        pop = self.stack.pop() # 删除栈顶元素
        self.size -= 1 # 栈元素数量减 1
        return pop
    def isEmpty(self):
        return self.stack == []
    def sizes(self):
        return self.size
    def peek(self):
        return self.stack[-1]

    def __str__(self):
        return self.stack.__str__()
