import unittest
from testcypher import TestCypher
from testhelper import TestHelper
from testkeygenerator import TestPseudorandomKey

if __name__ == '__main__':
    # Specify test classes
    tests = [TestPseudorandomKey, TestHelper, TestCypher]

    # Load tests 
    loader = unittest.TestLoader()
    suite = [loader.loadTestsFromTestCase(test) for test in tests]
    runnable_suite = unittest.TestSuite(suite)

    # Run
    results = unittest.TextTestRunner().run(runnable_suite)