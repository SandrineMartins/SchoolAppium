from cgitb import text
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
#app='/Users/runner/work/SchoolAppium/apk/app-curso-appium.apk'
caps["platformName"] = "Android"
caps["appium:deviceName"] = "emulator-5554"
caps["appium:appPackage"] = "com.example.cursoappium"
caps["appium:app"] = 'apk/app-curso-appium.apk'
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

btnCadastrarPessoa = "button_cadastrar"
textInputNome = "TextInputNome"
textInputEmail = "TextInputEmail"
btnCadastrar = "BotaoCadastrar"
btnGender = "radioButton_mulher"
btnEstados = "spinner_estados"
barraTexto = "snackbar_text"

class CadastroPessoa():

    def teste_cadastroPessoaOk():
        cadastrar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, btnCadastrarPessoa)))
        cadastrar.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, textInputNome)))
        driver.find_element(by=AppiumBy.ID, value=textInputNome).send_keys("enirdnas")
        driver.find_element(by=AppiumBy.ID, value=textInputEmail).send_keys("sandrine@sandrine.com")
        driver.find_element(by=AppiumBy.ID, value=btnGender).click()
        driver.find_element(by=AppiumBy.ID, value=btnEstados).click()
        estadoSelecionado = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[11]")
        estadoSelecionado.click()
        driver.find_element(by=AppiumBy.ID, value=btnCadastrar).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, barraTexto)))

        cadastroOk= driver.find_element(by=AppiumBy.ID, value=barraTexto).text
        assert cadastroOk == "Cadastro realizado com sucesso"

    teste_cadastroPessoaOk()

    def teste_ErroCadastroSemNome():
   
        driver.find_element(by=AppiumBy.ID, value=textInputEmail).send_keys("semNome@sandrine.com")
        driver.find_element(by=AppiumBy.ID, value=btnGender).click()

        driver.find_element(by=AppiumBy.ID, value=btnEstados).click()
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(606, 2133)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(606, 729)
        actions.w3c_actions.pointer_action.release()
        actions.perform()    
        estadoPB = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]")
        estadoPB.click()
    
        driver.find_element(by=AppiumBy.ID, value=btnCadastrar).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'textinput_error')))

        erroSemNome= driver.find_element(by=AppiumBy.ID, value='textinput_error').text
        assert erroSemNome == "Insira o nome completo"

    teste_ErroCadastroSemNome()

    def teste_ErroCadastroSemEmail():  

        driver.find_element(by=AppiumBy.ID, value=textInputNome).send_keys("enirdnas")
        driver.find_element(by=AppiumBy.ID, value=textInputEmail).send_keys("")
        driver.find_element(by=AppiumBy.ID, value=btnGender).click()    
        driver.find_element(by=AppiumBy.ID, value=btnCadastrar).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'textinput_error')))

        erroSemEmail= driver.find_element(by=AppiumBy.ID, value='textinput_error').text
        assert erroSemEmail == "Insira um email válido"

    teste_ErroCadastroSemEmail()

