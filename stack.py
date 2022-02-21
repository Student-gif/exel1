class cashStack:
    def __init__(self) -> None:
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        removed = self.stack.pop()
        return removed