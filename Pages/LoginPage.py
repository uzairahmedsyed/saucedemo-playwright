from playwright.sync_api import Page, expect
from config import BASE_URL

class LoginPage:

    def __init__(self, page:Page):

        self.page = page
        self.username = self.page.get_by_placeholder("Username")
        self.password = self.page.get_by_placeholder("Password")
        self.login_btn = self.page.get_by_role("button", name="Login")


    def goto_website(self):
        self.page.goto(BASE_URL)


    def login(self, entered_username, entered_password):
        expect(self.username).to_be_visible()
        self.username.fill(entered_username)
        self.password.fill(entered_password)
        self.login_btn.click()
