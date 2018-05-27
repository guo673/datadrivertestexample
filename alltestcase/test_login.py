import unittest
import os
import time
from common.manage_dir import getPngfilename
from common.create_driver import getDriver

class UserActionTest(unittest.TestCase):

    driver= getDriver()
    # dirname = os.path.dirname(os.path.abspath(__file__))
    # filename = os.path.join(dirname,"01.png")

    def setUp(self):
        self.driver.maximize_window()
        self.driver.get('http://118.31.19.120:3000/')

    def tearDown(self):
        self.driver.save_screenshot(getPngfilename())
        self.driver.delete_all_cookies()

    @classmethod
    def setUpClass(cls):
        pass   

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    def test_register(self):
       self.driver.find_element_by_link_text('注册').click()
       self.driver.get('http://118.31.19.120:3000/signup')
       self.driver.find_element_by_id('loginname').send_keys('testuser555')
       self.driver.find_element_by_id('pass').send_keys('123456')
       self.driver.find_element_by_id('re_pass').send_keys("123456")
       self.driver.find_element_by_id('email').send_keys('123456@123.com')
       self.driver.find_element_by_id('pass').submit()
    
    def test_login(self):

       self.driver.find_element_by_link_text('登录').click()
       self.driver.find_element_by_id('name').send_keys('testuser3')
       self.driver.find_element_by_id('pass').send_keys('123456')
       self.driver.find_element_by_id('pass').submit()      
       okurl = self.driver.current_url
       self.assertEqual(okurl,'http://118.31.19.120:3000/')
       loginName = self.driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text
       self.assertEqual(loginName,'testuser3')

if __name__ == "__main__":
    unittest.main()
