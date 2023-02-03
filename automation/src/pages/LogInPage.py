
from automation.src.pages.ProductListPage import ProductListPage

class LogInPage:
    def __init__(self, page) :
        self.page = page
        self._username = page.locator("[data-test=\"username\"]")
        self._password = page.locator("[data-test=\"password\"]")
        self._login_btn = page.locator("[data-test=\"login-button\"]")
        self.error_message = page.locator("[data-test=\"error\"]")

    
    def enter_username(self, uname):
        self._username.clear()
        self._username.fill(uname)
        
    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)
        
    def click_login(self):
        self._login_btn.click()
        
    def do_login(self, credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login()
        
        return ProductListPage(self.page)
        
        
    
        


