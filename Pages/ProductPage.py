from playwright.sync_api import Page, expect

class ProductPage:

    def __init__(self, page:Page):

        self.page = page
        self.sort_select = page.locator("[data-test='product-sort-container']")
        self.menu_btn = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.locator("[data-test='logout-sidebar-link']")


    def add_inventory(self, product_name):

        product = f"#add-to-cart-{product_name}"
        add_to_cart_btn = self.page.locator(product)
        expect(add_to_cart_btn).to_be_visible()
        add_to_cart_btn.click()

    def remove_inventory(self, product_name):
        self.page.locator(f"#remove-{product_name}").click()

    def sort_products(self, option):
        self.sort_select.select_option(option)

    def logout(self):
        self.menu_btn.click()
        self.logout_link.click()
