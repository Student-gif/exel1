
class cashStack:
    def __init__(self):
        self.stack=[]
    def push(self,data,):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed
    def data(self):
        print(self.stack)
        return True
stack = cashStack()