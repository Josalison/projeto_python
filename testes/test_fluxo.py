import os
from dotenv import load_dotenv
from playwright.sync_api import expect
from pages.login_page import FazerLogin
from pages.produto import Product
from pages.remover_cart import Remover
from pages.checkout import Checkout
from pages.pagamento import Pagamento
load_dotenv()

def test_fluxo_de_compra(page):
    login = FazerLogin(page)
    produto = Product(page)
    delete = Remover(page)
    check = Checkout(page)
    pagar = Pagamento(page)

    email = os.getenv("USER_EMAIL")
    senha = os.getenv("USER_PASSWORD")
    nome = "João Silva"
    number = "4539 2746 1182 5931"
    cvcs = "254"
    meses = "07"
    anos = "2029"

    login.acessar_site()
    login.clicar_login()
    login.add_email(email)
    login.senhas(senha)
    login.click_botao_login()
    
    produto.acessar_produto()
    produto.add_carrinho()
    
    delete.remover_pro_cart()

    check.clicar_checkout()
    expect(page).to_have_url("https://automationexercise.com/checkout")
    check.teste_caracteres("A" * 5000)
    #expect(page.locator(".form-control")).to_have_value("A" * 5000)
    
    
    pagar.dados_cliente()
    pagar.finalizar_compra()
    pagar.download()
    pagar.continuar()
    #page.wait_for_timeout(20000)
