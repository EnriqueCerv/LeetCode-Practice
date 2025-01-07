# %% Hacckerank editor

class Editor:
    def __init__(self):
        self.st = ''
        self.save = ''
        
    def append(self, W):
        self.save = self.st
        self.st += W
        
    def delete(self, k):
        self.save = self.st
        n = len(self.st)
        self.st = ''.join([self.st[i] for i in range(0, n - k)])
    
    def print(self, k):
        return self.st[k]
        
    def undo(self):
        self.st = self.save