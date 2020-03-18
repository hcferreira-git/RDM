from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "RDM Transportes"
        # Altere o nome dos grupos aqui
        self.grupos = ["GRUPO DA FAMÍLIA", "GRUPO DE VENDAS"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        #self.driver.get('https://web.whatsapp.com')
        self.driver.get('https://api.whatsapp.com/send?phone=5562998398457')
        time.sleep(10)
        #<a class="_36or _2y_c _2z0c _2z07" title="Compartilhe no WhatsApp" id="action-button">Enviar mensagem</a>
        # <a class="_36or" href="https://web.whatsapp.com/send?phone=5562998398457">use o WhatsApp Web</a>
        btnEnviar = self.driver.find_element_by_id('action-button')
        btnEnviar.click()
        time.sleep(2)

#        ActionChains.send_keys(Keys.ENTER)

#        btnWeb = self.driver.find_elements_by_link_text('use o WhatsApp Web')
#        btnWeb.click()
#        time.sleep(2)
#        for grupo in self.grupos:
#            grupo = self.driver.find_element_by_xpath(
#                f"//span[@title='{grupo}")
#            time.sleep(3)
#            grupo.click()
#        chat_box = self.driver.find_element_by_class_name('_13mgZ')
        time.sleep(3)
#        chat_box.click()
#            chat_box.send_keys(self.mensagem)
#            botao_enviar = self.driver.find_element_by_xpath(
#                "//span[@data-icon='send']")
#            time.sleep(3)
#            botao_enviar.click()
#            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()
