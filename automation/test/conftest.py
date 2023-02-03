import pytest

@pytest.fixture()
def set_up_tear_down(page)-> None:
    page.set_viewport_size({"width":1550, "height": 800})
    page.goto("https://www.saucedemo.com/")
    
    yield page
