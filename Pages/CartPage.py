
class CartPage:

    def __init__(self, cartTab):
        
        self.cartpagebrowser = cartTab

    def open_cart(self):
        self.cartpagebrowser.locator(".shopping_cart_link").click()

    def proceed_to_checkout(self):
        self.cartpagebrowser.get_by_role("button", name="Checkout").click()
        