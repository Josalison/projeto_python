import re
from .base_page import BasePage

class Checkout(BasePage):
    def clicar_checkout(self):
        self.page.locator(".check_out").click()

    def teste_caracteres(self, texto):
        self.page.locator(".form-control").fill(texto)
        self.page.get_by_role("link", name="Place Order").click()