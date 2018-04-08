import unittest
import sys
from src import variablen
from src import lists

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

class ListsTest(unittest.TestCase):
    def testList(self):
        for i in range(0, 8):
            assert lists.meine_liste[i] == i+1

    def testVar1(self):
        assert lists.var1 == lists.meine_liste[3]

    def testdict(self):
        assert lists.mein_dict["a"] == 4
        assert lists.mein_dict["b"] == 5
        assert lists.mein_dict["c"] == 6

    def testVar2(self):
        assert lists.var2 == lists.mein_dict["b"]

if __name__ == "__main__":
	unittest.main()
