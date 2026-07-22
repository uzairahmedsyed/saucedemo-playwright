from playwright.sync_api import Page

class OrderConfirmationPage:

    def __init__(self, page:Page):

        self.page = page
        self.finish_btn = self.page.get_by_text("Finish")


    def finish_checkout(self):

        self.finish_btn.click()