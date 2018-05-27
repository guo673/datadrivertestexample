import unittest
from selenium import webdriver

def add(x,y):
    return x+y

driver = webdriver.Chrome()
# user = 'testuser7'
# passwd = '123456'

class userActionTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('It is beginning')

    @classmethod
    def tearDownClass(cls):
        driver.quit()
    
    def test_add(self):
        expect_val = 3
        self.assertEqual(add(1,2),expect_val)
    
    def test_login(self):  
        driver.get('http://118.31.19.120:3000/signin')
        driver.find_element_by_id('name').send_keys('testuser7')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_id('pass').submit()
        okurl = driver.current_url

        self.assertEqual(okurl,'http://118.31.19.120:3000/')

        loginName = driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text

        self.assertEqual(loginName,'testuser7')

if __name__ == "__main__":
    unittest.main()
