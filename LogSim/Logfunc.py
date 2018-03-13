__version__ ="1.5"
__author__ = "Sebastian Bensing"

class ANDGATE(object):
    """description of class"""


    def __init__(self, *args, **kwargs):
        self.__Input0 = False
        self.__Input1 = False
        self.__Output = False
        self.__Name = "AndGate"
        return super().__init__(*args, **kwargs)

    def execute(self):
        if __Input0 == True:
            if __Input1 == True:
                self.__Output = False

    def show(self):
        print("Die Bedingungen sind: "+__str__(self.__Output))

    def __str__(self,wert):
        return str(wert)
        return super().__str__()

    # property()

    def setzeInput0(self,wert):
        self.__Input0 = wert

    def setzeInput1(self,wert):
        self.__Input1 = wert

    def gebeInput0(self):
        return self.__Input0

    def gebeInput1(self):
        return self.__Input1

    def gebeName(self):
        return self.__Name

