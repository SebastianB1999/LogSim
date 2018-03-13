import unittest
from Logfunc import ANDGATE
class Test_test1(unittest.TestCase):

    def testcase_01(self):
        a = ANDGATE()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, "Class ANDGATE: Testcase 1 failed.")

    def testcase_02(self):
        a = ANDGATE()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, "Class ANDGATE: Testcase 2 failed.")

    def testcase_03(self):
        a = ANDGATE()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertFalse(a.gebeOutput, "Class ANDGATE: Testcase 3 failed.")

    def testcase_04(self):
        a = ANDGATE()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertFalse(a.gebeOutput, "Class ANDGATE: Testcase 4 failed.")

    def testcase_05(self):
        a = ANDGATE()
        a.setzeInput0(False)
        a.setzeInput1(False)
        a.execute()
        self.assertFalse(a.gebeOutput, "Class ANDGATE: Testcase 5 failed.")

    def testcase_06(self):
        a = ANDGATE()
        a.setzeInput0(True)
        a.setzeInput1(False)
        a.execute()
        self.assertFalse(a.gebeOutput, "Class ANDGATE: Testcase 6 failed.")

    def testcase_07(self):
        a = ANDGATE()
        a.setzeInput0(False)
        a.setzeInput1(True)
        a.execute()
        self.assertFalse(a.gebeOutput, "Class ANDGATE: Testcase 7 failed.")

    def testcase_08(self):
        a = ANDGATE()
        a.setzeInput0(True)
        a.setzeInput1(True)
        a.execute()
        self.assertTrue(a.gebeOutput, "Class ANDGATE: Testcase 8 failed.")


if __name__ == '__main__':
    unittest.main()                    # führt automatisch alle Methoden aus die mit testcase_ beginnen
