#Bibliotecas necessárias para a automação: Selenium, Pandas, Time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchDriverException
import pandas as pd
import time

#Função definida que é responsável por toda automação
def startchallenge():
    try:
        driver = webdriver.Chrome()#Usa o Chrome como Browser
        driver.get("https://rpachallenge.com")#Define o site a ser acessado
        driver.maximize_window()#Maximiza a janela
        StartChallenge = driver.find_element(By.CLASS_NAME, "uiColorButton")#Inicia o desafio, usando o nome da classe
        StartChallenge.click()#Clica no elemento do botão para iniciar o desafio
        df = pd.read_excel("challenge.xlsx")#Leitura do arquivo "challenge.xlsx"

        if driver == NoSuchDriverException: #Verifica com os valores True ou False a abertura do navegador
            print("Ocorreu um erro na abertura do navegador")
        else:
            print("O navegador foi aberto com sucesso, operação em processo..")

        #Estrutura de repetição For Each
        for row, row in df.iterrows():
            Email = row["Email"]
            Nome = row["First Name"]
            SobreNome = row["Last Name "]
            Compania = row["Company Name"]
            Cargo = row["Role in Company"]
            Endereco = row["Address"]
            Numero = row["Phone Number"]

            try:
                digitar_nome = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")#Campo de Nome
                digitar_nome.send_keys(Nome)

                digitar_email = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")#Campo de Email
                digitar_email.send_keys(Email)

                digitar_celular = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")#Campo de Celular
                digitar_celular.send_keys(Numero)

                digitar_endereco = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")#Campo de Endereço
                digitar_endereco.send_keys(Endereco)

                digitar_sobrenome = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")#Campo de sobrenome
                digitar_sobrenome.send_keys(SobreNome)

                digitar_emprego = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")#Campo da compania
                digitar_emprego.send_keys(Compania)

                digitar_cargo = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")#Campo do cargo
                digitar_cargo.send_keys(Cargo)

                botao = driver.find_element(By.XPATH,"//input[@type='submit']")#Botão de submit
                botao.click()
            except NoSuchElementException:
                print("Um ou mais elementos não foram encontrados")
        driver.save_screenshot('C:\\Users\\João Bruno\\Pictures\\Saved Pictures\\Automacao.png')#Salva uma captura de tela do tempo total da automação
        time.sleep(10)#Pausa para verificar o tempo de conclusão
        driver.quit()#Encerra o navegador
        print("A operação foi concluida com sucesso, verifique suas fotos para ver o tempo da automação")        
    except TimeoutException:
        print("Erro: a automação não correspondeu a tempo")
    
rpachallenge = startchallenge()#Inicia a automação
