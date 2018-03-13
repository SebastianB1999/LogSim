__version__ ="1.5"
__author__ = "Sebastian Bensing"

class ANDGATE(object):
    """description of class"""


    def __init__(self, *args, **kwargs):
        self.__Input0 = False
        self.__Input1 = False
        self.__Output = False
        self.__Name = "AndGate"
        # property
        self.Name = property(self.gebeName,self.setzeName)
        self.Input0 = property(self.gebeInput0,self.setzeInput0)

        return super().__init__(*args, **kwargs)




    def execute(self):
        if self.Input0 == True:
            if self.Input1 == True:
                self.Output = False

    def show(self):
        print("Die Bedingungen sind: "+__str__(self.__Output))

    def __str__(self,wert):
        return str(wert)
        return super().__str__()


    def setzeInput0(self,value):
        isinstance(value, bool)
        self.__Input0 = wert

    def setzeInput1(self,wert):
        self.__Input1 = wert

    def gebeInput0(self):
        return self.__Input0

    def setzeName(self, value):
        self.__Name = value

    def gebeInput1(self):
        return self.__Input1

    def gebeName(self):
        return self.__Name

    def gebeOutput(self):
        return self.__Output
