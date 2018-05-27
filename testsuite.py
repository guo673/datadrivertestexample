import unittest
from alltestcase.test_login import UserActionTest

def suite():
    login = unittest.TestLoader().loadTestsFromTestCase(UserActionTest)
    return unittest.TestSuite([login])

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


# import unittest
# from alltestcase.test_login import UserActionTest

# def suite():
#     suite = unittest.TestLoader().loadTestsFromTestCase()
#     suite.addTest(UserActionTest('test_login'))
#     suite.addTest(UserActionTest('test_register'))
#     return suite

# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite())
