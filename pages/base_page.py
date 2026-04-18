from playwright.sync_api import sync_playwright, Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page  = page

        