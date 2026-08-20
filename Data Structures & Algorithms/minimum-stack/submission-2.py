class MinStack:
    """
    "MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"
    [1 2 0 ]
    return 0
    [1 2 ]
    return 2

    """

    def __init__(self):
        self.stack = []
        self.minis = []
        

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if not self.minis: 
            self.minis.append(val)
        else:
            if (val == min(self.minis[-1], val)):
                self.minis.append(val)

    def pop(self) -> None:
        if self.stack.pop()== self.minis[-1]:
            self.minis.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.minis: return 0
        return self.minis[-1]
        
