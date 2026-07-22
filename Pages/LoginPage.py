from playwright.sync_api import Page

class LoginPage:

    URL = "https://www.saucedemo.com"
    
    
    def __init__(self, page:Page):

        self.page = page
        self.username = self.page.get_by_placeholder("Username")
        self.password = self.page.get_by_placeholder("Password")
        self.login_btn = self.page.get_by_role("button", name="Login")


    def goto_website(self):
        self.page.goto(self.URL)


    def login(self, entered_username, entered_password):
        self.username.fill(entered_username)
        self.password.fill(entered_password)
        self.login_btn.click()
