__version__ ="1.5"
__author__ = "Sebastian Bensing"

class ANDGATE(object):
    """description of class"""


    def __init__(self, *args, **kwargs):
        self.Input0 = False
        self.Input1 = False
        self.Output = False
        self.Name = "AndGate"
        return super().__init__(*args, **kwargs)

    def execute(self):
        if Input0 == True:
            if INput1 == True:
                self.Output = False

    def show(self):
        print("Die Bedingungen sind: "+__str__(self.Output))

    def __str__(self,wert):
        return str(wert)
        return super().__str__()