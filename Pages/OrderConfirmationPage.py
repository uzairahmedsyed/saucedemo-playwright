
class OrderConfirmation:

    def __init__(self, browserTab):

        self.browser = browserTab
    
    def finish_checkout(self):

        self.browser.get_by_text("Finish").click()