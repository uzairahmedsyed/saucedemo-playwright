from playwright.sync_api import Page

class CartPage:

    def __init__(self, page:Page):
        
        self.page = page
        self.cart_icon = self.page.locator(".shopping_cart_link")
        self.checkout_btn = self.page.get_by_role("button", name="Checkout")
    
    
    def open_cart(self):
        self.cart_icon.click()

    
    def proceed_to_checkout(self):
        self.checkout_btn.click()
        