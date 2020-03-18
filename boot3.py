from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import csv

arq_msg = open('C:/Temp/Msg.csv', 'r')
text = arq_msg.read().split('\n')
arq_msg.close()

arq_listas = open('C:/Temp/Contatos.csv', 'r')
moblie_no_list = arq_listas.read().split('\n')
arq_listas.close()

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")

sleep(10) #wait time to scan the code in second

def send_whatsapp_msg(phone_no,text):
    
    driver.get("https://web.whatsapp.com/send?phone=55{}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for tx in text:
            txt_box.send_keys(tx)
            txt_box.send_keys(Keys.SHIFT, Keys.ENTER)
        
        txt_box.send_keys(Keys.BACKSPACE)
        txt_box.send_keys("\n")

    except Exception as e:
        print("invailid phone no :"+str(phone_no))

for moblie_no in moblie_no_list:
    try:
        if moblie_no != "":
            send_whatsapp_msg(moblie_no, text)

    except Exception as e:
        sleep(10)
        is_connected()
