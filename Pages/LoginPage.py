
class LoginPage:

    def __init__(self, browserTab):

        self.browser = browserTab

    def goto_website(self):
        self.browser.goto("https://www.saucedemo.com")

    def login(self, username, userpassword):
        self.browser.get_by_placeholder("Username").fill(username)
        self.browser.get_by_placeholder("Password").fill(userpassword)
        self.browser.get_by_role("button", name="Login").click()
