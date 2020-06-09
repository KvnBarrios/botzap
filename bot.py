import random
import time

from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class zapbot:
    # O local de execução do nosso script
    dir_path = os.getcwd()
    # O caminho do chromedriver
    opts = webdriver.ChromeOptions()
    opts.add_argument("start-maximized")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option('useAutomationExtension', False)
    opts.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=opts)
    chromedriver = os.path.join(dir_path, "chromedriver.exe")
    # Caminho onde será criada pasta profile
    profile = os.path.join(dir_path, "profile", "wpp")
    action = ActionChains(driver)
    ultimamsg_id = ""
    ultimamsg_looping = ""

    def __init__(self):
        # Abre o whatsappweb
        self.driver.get("https://web.whatsapp.com/")
        # Aguarda alguns segundos para validação manual do QrCode
        self.driver.implicitly_wait(15)

    def abre_conversa(self, contato):
        """ Abre a conversa com um contato especifico """
        try:
            # Seleciona a caixa de pesquisa de conversa
            self.caixa_de_pesquisa = self.driver.find_element_by_css_selector(".\_2S1VP")
            # Digita o nome ou numero do contato
            self.caixa_de_pesquisa.send_keys(contato)
            sleep(5)
            # Seleciona o contato
            self.contato = self.driver.find_element_by_xpath("span[.='{}']".format(contato))
            # Entra na conversa
            self.contato.click()
            self.caixa_de_pesquisa.clear()
        except Exception as e:
            raise e

    def envia_msg(self, msg):
        """ Envia uma mensagem para a conversa aberta """
        try:
            sleep(1)
            # Seleciona acaixa de mensagem
            self.caixa_de_mensagem = self.driver.find_element_by_css_selector(".\_2WovP > .\_2S1VP")
            # Digita a mensagem
            self.caixa_de_mensagem.send_keys(msg)
            self.caixa_de_mensagem.send_keys(Keys.ENTER)
            self.caixa_de_mensagem.send_keys(Keys.ENTER)
            # sleep(1)
            # Seleciona botão enviar
            # self.botao_enviar = self.driver.find_element_by_css_selector(".\_35EW6 > span")
            # Envia msg
            # self.botao_enviar.click()
            # sleep(1)
        except:
            pass

    def ultima_msg(self):
        """ Captura a ultima mensagem da conversa """
        try:
            post = self.driver.find_elements_by_class_name("_3_7SH")
            ultimo = len(post) - 1
            # O texto da ultima mensagem
            texto = post[ultimo].find_element_by_css_selector(
                "span.selectable-text").text
            return texto
        except Exception as e:

            print("Erro ao ler msg, tentando novamente!")

    def repassar_msg_option_burra(self):
        try:
            post = self.driver.find_elements_by_class_name("_3_7SH")
            ultimo = len(post) - 1
            try:
                texto = post[ultimo].find_element_by_css_selector(
                    "span.selectable-text").text
                ## repassar
                if (self.ultimamsg != texto):
                    try:
                        x = random.randint(0, 3000000)
                        a = self.driver.save_screenshot(rf"C:\Users\kevin\Desktop\fotos\foto{x}.png")
                        # Seleciona a caixa de pesquisa de conversa
                        self.caixa_de_pesquisa = self.driver.find_element_by_css_selector(".\_2S1VP")
                        # Digita o nome ou numero do contato
                        self.caixa_de_pesquisa.send_keys("Grupo que recebe a msg")
                        sleep(2)
                        # Seleciona o contato
                        self.contato = self.driver.find_element_by_css_selector(".matched-text")
                        # Entra na conversa
                        self.contato.click()
                        try:
                            # Clica no botão adicionar
                            self.driver.find_element_by_css_selector("span[data-icon='clip']").click()
                            # Seleciona input
                            attach = self.driver.find_element_by_css_selector("input[type='file']")
                            # Adiciona arquivo
                            attach.send_keys(rf"C:\Users\kevin\Desktop\fotos\foto{x}.png")
                            sleep(3)
                            # Seleciona botão enviar
                            send = self.driver.find_element_by_xpath("//div[contains(@class, 'yavlE')]")
                            # Clica no botão enviar
                            send.click()
                        except Exception as e:
                            print("Erro ao enviar media", e)
                        try:
                            sleep(1)
                            # Seleciona acaixa de mensagem
                            self.caixa_de_mensagem = self.driver.find_element_by_css_selector(".\_2WovP > .\_2S1VP")
                            # Digita a mensagem
                            self.caixa_de_mensagem.send_keys(texto)
                            self.caixa_de_mensagem.send_keys(Keys.ENTER)
                            self.caixa_de_mensagem.send_keys(Keys.ENTER)
                            self.ultimamsg = texto

                        except:
                            pass
                    except Exception as e:
                        raise e
            except:
                try:
                    x = random.randint(0, 3000000)
                    a = self.driver.save_screenshot(rf"C:\Users\kevin\Desktop\fotos\foto{x}.png")
                    # Seleciona a caixa de pesquisa de conversa
                    self.caixa_de_pesquisa = self.driver.find_element_by_css_selector(".\_2S1VP")
                    # Digita o nome ou numero do contato
                    self.caixa_de_pesquisa.send_keys("Grupo que recebe a msg")
                    sleep(2)
                    # Seleciona o contato
                    self.contato = self.driver.find_element_by_css_selector(".matched-text")
                    # Entra na conversa
                    self.contato.click()
                    try:
                        # Clica no botão adicionar
                        self.driver.find_element_by_css_selector("span[data-icon='clip']").click()
                        # Seleciona input
                        attach = self.driver.find_element_by_css_selector("input[type='file']")
                        # Adiciona arquivo
                        attach.send_keys(rf"C:\Users\kevin\Desktop\fotos\foto{x}.png")
                        sleep(3)
                        # Seleciona botão enviar
                        send = self.driver.find_element_by_xpath("//div[contains(@class, 'yavlE')]")
                        # Clica no botão enviar
                        send.click()
                    except Exception as e:
                        print("Erro ao enviar media", e)
                    try:
                        sleep(1)
                        # Seleciona acaixa de mensagem
                        self.caixa_de_mensagem = self.driver.find_element_by_css_selector(".\_2WovP > .\_2S1VP")
                        # Digita a mensagem
                        self.caixa_de_mensagem.send_keys(texto)
                        self.caixa_de_mensagem.send_keys(Keys.ENTER)
                        self.caixa_de_mensagem.send_keys(Keys.ENTER)
                        self.ultimamsg = texto
                    except:
                        pass
                except Exception as e:
                    raise e
        except Exception as a:
            print(a)

    def envia_media(self, fileToSend):
        """ Envia media """
        try:
            # Clica no botão adicionar
            self.driver.find_element_by_css_selector("span[data-icon='clip']").click()
            # Seleciona input
            attach = self.driver.find_element_by_css_selector("input[type='file']")
            # Adiciona arquivo
            attach.send_keys(fileToSend)
            sleep(3)
            # Seleciona botão enviar
            send = self.driver.find_element_by_xpath("//div[contains(@class, 'yavlE')]")
            # Clica no botão enviar
            send.click()

        except Exception as e:
            print("Erro ao enviar media", e)

    def repassar_msg(self):
        id_msg = self.driver.find_elements_by_css_selector(
        "div[class*='vW7d1']")
        ultima_id_msg = id_msg[len(id_msg) - 1].get_attribute("data-id")
        while self.ultimamsg_looping != ultima_id_msg:
            id_msg = self.driver.find_elements_by_css_selector(
                "div[class*='vW7d1']")
            ultima_id_msg = id_msg[len(id_msg) - 1].get_attribute("data-id")
            if ultima_id_msg != self.ultimamsg_id:
                menu = self.driver.find_elements_by_css_selector("span[data-icon='menu']")
                menu[1].click()
                selecionar_msg = self.driver.find_elements_by_css_selector("li[data-animate-dropdown-item='true']")
                selecionar_msg[2].click()
                time.sleep(2)
                x = 1
                for c in range(len(id_msg)):
                    if self.ultimamsg_id != "":
                        while id_msg[len(id_msg) - x].get_attribute("data-id") != self.ultimamsg_id:
                            if id_msg[len(id_msg) - x].get_attribute("data-id").startswith("album"):
                                break
                            elif id_msg[len(id_msg) - x].get_attribute("data-id").startswith("grouped-sticker"):
                                break
                            else:
                                botao_pra_enviar = self.driver.find_elements_by_class_name("_3I_df")
                                botao_pra_enviar[len(botao_pra_enviar) - x].click()
                                x += 1
                            self.ultimamsg_looping = id_msg[len(id_msg) - 1].get_attribute("data-id")
                    else:
                        botao_pra_enviar = self.driver.find_elements_by_class_name("_3I_df")
                        botao_pra_enviar[len(botao_pra_enviar) - 1].click()
                        self.ultimamsg_looping = id_msg[len(id_msg) - 1].get_attribute("data-id")
                        break
                time.sleep(5)
                print(self.ultimamsg_looping,ultima_id_msg)
                if self.ultimamsg_looping != ultima_id_msg:
                    self.driver.find_element_by_css_selector("span[data-icon='x']").click()
                    bot.repassar_msg()
                self.driver.find_element_by_css_selector("span[data-icon='forward']").click()
                time.sleep(1)
                self.driver.find_elements_by_css_selector("div[contenteditable='true']")[0].send_keys(
                    "grupo que recebe a msg")
                time.sleep(1)
                self.driver.find_element_by_class_name("_1mFmt").click()
                self.driver.find_element_by_css_selector("span[data-icon='send']").click()
                self.ultimamsg_id = ultima_id_msg
                """ Abre a conversa com um contato especifico """
                time.sleep(0.5)
                try:
                    # Seleciona a caixa de pesquisa de conversa
                    self.caixa_de_pesquisa = self.driver.find_element_by_css_selector(".\_2S1VP")
                    # Digita o nome ou numero do contato
                    self.caixa_de_pesquisa.send_keys("#19 CDI CUPONS, DESCONTOS")
                    sleep(1)
                    # Seleciona o contato
                    self.contato = self.driver.find_element_by_css_selector(".matched-text")
                    # Entra na conversa
                    self.contato.click()
                    self.caixa_de_pesquisa.clear()
                except Exception as e:
                    raise e
                print(ultima_id_msg, self.ultimamsg_id)



if __name__ == '__main__':
    bot = zapbot()  # Inicia o objeto zapbot
    bot.abre_conversa("#19 CDI CUPONS, DESCONTOS")  # Passando o numero ou o nome do contato

    x = False
    while x != True:
        bot.repassar_msg()
        time.sleep(12)
