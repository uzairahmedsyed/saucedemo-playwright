
class ProductPage:

    def __init__(self, browserTabProductPage):

        self.browser_ProductPage = browserTabProductPage
    
    def add_inventory(self):

        self.browser_ProductPage.locator("#add-to-cart-sauce-labs-backpack").click()