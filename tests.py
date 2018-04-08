import unittest
import sys
from src import variablen

class SetupTest(unittest.TestCase):
	def testEnviroment(self):
		python_version = sys.version
		info = "Python version 2.7.X is needed. Found Python " + python_version
		assert python_version.startswith("2.7"), info

class VariableTest(unittest.TestCase):
    def testVar1(self):
        assert variablen.var1 == 4

    def testVar2(self):
        assert variablen.var2 == 5

    def testVar3(self):
        assert variablen.var3 == 9

    def testS1(self):
        assert variablen.s1 == "ATCG"

    def testS2(self):
        assert variablen.s2 == "GCTA"

    def testS3(self):
        assert variablen.s3 == "ATCGGCTA"

    def testS4(self):
        assert variablen.s4 == "ATCG4"

if __name__ == "__main__":
	unittest.main()
