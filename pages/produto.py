from .base_page import BasePage
import re

class Product(BasePage):
    def acessar_produto(self):
        self.page.get_by_role("link",name=re.compile(r"products", re.IGNORECASE)).click()

    def add_carrinho(self):
        self.page.locator('[data-product-id="2"]').first.click()
        self.page.get_by_role("button", name=re.compile(r"Continue Shopping", re.IGNORECASE)).click()
        self.page.locator('[data-product-id="1"]').first.click()
        self.page.get_by_role("button", name=re.compile(r"Continue Shopping", re.IGNORECASE)).click()

    