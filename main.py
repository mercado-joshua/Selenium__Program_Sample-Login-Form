#===========================
# Imports
#===========================

import pyinputplus as pyip
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

#===========================
# Main App
#===========================

class Login_Form:
    def __init__(self, username, password):
        self.driver = wd.Firefox(executable_path=r'C:\\Python\\Selenium\\Firefox\\geckodriver.exe')
        self.target_url = 'https://login.metafilter.com'
        self.username = username
        self.password = password
        self.run()

    def run(self):
        username_element = self.driver.find_element_by_id('user_name')
        username_element.send_keys(self.username)

        password_element = self.driver.find_element_by_id('user_pass')
        password_element.send_keys(self.password)
        password_element.submit()

def main():
    username = pyip.inputStr('Username: ')
    password = pyip.inputPassword('Password: ')
    app = Login_Form(username, password)

#===========================
# Start App
#===========================

if __name__ == '__main__':
    main()