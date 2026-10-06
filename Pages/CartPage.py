from playwright.sync_api import Page, expect

class CartPage:

    def __init__(self, page:Page):

        self.page = page
        self.cart_icon = self.page.locator(".shopping_cart_link")
        self.checkout_btn = self.page.get_by_role("button", name="Checkout")


    def open_cart(self):
        expect(self.cart_icon).to_be_visible()
        self.cart_icon.click()


    def proceed_to_checkout(self):
        expect(self.checkout_btn).to_be_visible()
        self.checkout_btn.click()

    def remove_product(self, product_id):
        self.page.locator(f"#remove-{product_id}").click()
