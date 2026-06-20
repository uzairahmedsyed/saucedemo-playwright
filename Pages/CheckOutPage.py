
class CheckoutPage:

    def __init__(self, tabcheckout):

        self.checkoutTab = tabcheckout

    def checkout_proceed(self):

        self.checkoutTab.get_by_placeholder("First Name").fill("Buyer")
        self.checkoutTab.get_by_placeholder("Last Name").fill("Buyer")
        self.checkoutTab.get_by_placeholder("Zip/Postal Code").fill("90248")
        self.checkoutTab.get_by_text("Continue").click()
    