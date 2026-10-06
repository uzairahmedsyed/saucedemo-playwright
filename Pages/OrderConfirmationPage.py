from playwright.sync_api import Page, expect

class OrderConfirmationPage:

    def __init__(self, page:Page):

        self.page = page
        self.finish_btn = self.page.get_by_text("Finish")


    def finish_checkout(self):

        expect(self.finish_btn).to_be_visible()
        self.finish_btn.click()