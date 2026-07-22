from playwright.sync_api import Page

class ProductPage:

    def __init__(self, page:Page):

        self.page = page
    

    def add_inventory(self, product_name):

        product = f"#add-to-cart-{product_name}"
        self.page.locator(product).click()