
from playwright.sync_api import Page, expect
from automation.src.pages.LogInPage import LogInPage

def test_login_with_standard_user(set_up_tear_down) -> None:
    page = set_up_tear_down 
    credentials =  {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LogInPage(page)
    product_page = login_p.do_login(credentials)
        
    expect(product_page.product_header).to_have_text("Products")
    
def test_login_with_invalid_username(set_up_tear_down) -> None:
    page = set_up_tear_down   
    credentials =  {'username': 'standard', 'password': 'secret_sauce'}
    login_p = LogInPage(page)
    login_p.do_login(credentials)   
    
    expect(login_p.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")   