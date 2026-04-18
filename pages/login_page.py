import re
from pages.base_page import BasePage

class FazerLogin(BasePage):
    def acessar_site(self):
        self.page.goto("https://automationexercise.com/")
    
    def clicar_login(self):
        self.page.get_by_role("link", name="Signup / Login").click()
    
    def add_email(self, email):
        self.page.locator('input[data-qa="login-email"]').fill(email)

    def senhas(self, senha):
        self.page.locator('input[data-qa="login-password"]').fill(senha)

    def click_botao_login(self):
        self.page.get_by_role("button", name=re.compile(r"login", re.IGNORECASE)).first.click()
