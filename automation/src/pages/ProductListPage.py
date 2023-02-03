

class ProductListPage:
    
    def __init__(self, page):
        self.page = page
        self._product_page_title = page.locator("span.title")
    
    @property
    def product_header(self):
        return self._product_page_title
