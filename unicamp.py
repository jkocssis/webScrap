from selenium import webdriver
url = 'https://www.siarh.unicamp.br/concurso/LoginInscricao.jsf;jsessionid=C77E7A6C8A3536700BD4A84BE45F0A6E?modoParam=MANUTENCAO'
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('firefox')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'/usr/local/bin/geckodriver')

driver.get(url)
cpfElem = driver.find_element_by_name('formulario:cpf')
cpfElem.send_keys('SEU CPF')
buttonBuscar = driver.find_element_by_class_name("rh-btn")
buttonBuscar.click()
senha = driver.find_element_by_name('formulario:senha')
senha.send_keys('SUA SENHA')
buttonBuscar = driver.find_element_by_class_name("rh-btn")
buttonBuscar.click()
