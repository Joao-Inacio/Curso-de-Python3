"""
    Selenium - Automatizando tarefas no navegador
"""
from selenium import webdriver
from time import sleep

"""
import os
 
PASTA_QUE_ESTOU = os.path.dirname(__file__)
CAMINHO_CHROME_DRIVER = os.path.join(PASTA_QUE_ESTOU, 'chromedriver.exe')
 
print(CAMINHO_CHROME_DRIVER)
"""


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir=C:\Users\joaoi\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome(
            self.driver_path
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print(f'Erro ao clicar em Sign in: {e}')

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil: ', e)

    def faz_logout(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print(f'Erro ao fazer log out {e}')

    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_css_selector('#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button')
            input_login.send_keys('Usuario do Github')
            input_password.send_keys('Senha do github')
            sleep(3)
            btn_login.click()
        except Exception as e:
            print(f'Erro ao logar {e}')


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    sleep(3)

    chrome.clica_sign_in()
    chrome.faz_login()

    sleep(2)

    chrome.clica_perfil()
    # chrome.verifica_usuario('Joao-Inacio')

    sleep(2)

    chrome.faz_logout()

    sleep(3)

    chrome.sair()
