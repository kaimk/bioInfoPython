import unittest
import sys

class SimpleTestCase(unittest.TestCase):
	def testEnviroment(self):
		python_version = sys.version
		info = "Python version 2.7.X is needed. Found Python " + python_version
		assert python_version.startswith("2.7"), info
if __name__ == "__main__":
	unittest.main()
