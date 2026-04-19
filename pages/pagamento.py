from .base_page import BasePage
import re

class Pagamento(BasePage):
    def dados_cliente(self):
        self.page.locator('input[data-qa="name-on-card"]').fill("João Silva")
        self.page.locator('input[data-qa="card-number"]').fill("4539 2746 1182 5931")
        self.page.locator('input[data-qa="cvc"]').fill("254")
        self.page.locator('input[data-qa="expiry-month"]').fill("07")
        self.page.locator('input[data-qa="expiry-year"]').fill("2029")

    def finalizar_compra(self):
        self.page.locator('button[data-qa="pay-button"]').click()
    
    def download(self):
        self.page.get_by_role("link", name=re.compile(r"download invoice",
        re.IGNORECASE)).click()

    def continuar(self):
        self.page.locator('[data-qa="continue-button"]').click()
