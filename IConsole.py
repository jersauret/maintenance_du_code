from abc import abstractmethod


class IConsole():
    @abstractmethod
    
    def write(self, text):
        pass
            
            
class StringBuilder (IConsole):
    def __init__(self):
        self._string = ""
        
    def toString(self):
        return self._string
    
    def write(self, text):
        IConsole.write(self, text)
        with open("output.txt", 'w') as f:
            f.write(text)
        