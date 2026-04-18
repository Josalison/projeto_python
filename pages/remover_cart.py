import re
from .base_page import BasePage

class Remover(BasePage):
    def remover_pro_cart(self):
        self.page.get_by_role("link", name="Cart").click()
        self.page.locator('a.cart_quantity_delete[data-product-id="2"]').click()