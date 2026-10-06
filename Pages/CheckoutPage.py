from playwright.sync_api import Page, expect

class CheckoutPage:

    def __init__(self, page:Page):

        self.page = page
        self.first_name = self.page.get_by_placeholder("First Name")
        self.last_name = self.page.get_by_placeholder("Last Name")
        self.postal_code = self.page.get_by_placeholder("Zip/Postal Code")
        self.continue_btn = self.page.get_by_text("Continue")


    def checkout_proceed(self, first_name, last_name, zip_code):

        expect(self.first_name).to_be_visible()
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(zip_code)
        self.continue_btn.click()