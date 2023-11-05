from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Chrome()
action = ActionChains(driver)
login = "sag64129@zslsz.com"
password = 'ziomek123'
ulr = 'https://lepolek.pl/logowanie'

driver.get(ulr)
driver.maximize_window()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
loginBox = driver.find_element(By.NAME, 'username')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
passwordBox = driver.find_element(By.NAME, 'password')

cookiesAcceptButton = driver.find_element(By.XPATH, '*//button[@id="rcc-confirm-button"]')
cookiesAcceptButton.click()

loginBox.send_keys(login)
passwordBox.send_keys(password)
passwordBox.send_keys(Keys.ENTER)
sleep(2)
driver.get('https://lepolek.pl/nauka')
sleep(5)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "*//input[contains(@id,'list-item-checkbox')]")))

test = "*//main/div[7]/div/form/div/div[2]/div[1]/div/div/div/div/div"

allCheckbox = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/main/div[7]/div/form/div/div[2]/div[1]/div/div/div/div/div//input")
c = 1
for checkbox in allCheckbox:

    print(c)
    print(checkbox.get_attribute("id"))
    c = c+1


comboBoxesOnRigtSite = driver.find_elements(By.XPATH, "*//div[@class = 'dropdownIndicator__DropdownIndicatorStyled-sc-1pzr9y6-0 kuQVZE']")
comboBoxForLDEKLabels = comboBoxesOnRigtSite[1]
comboBoxForLDEKLabels.click()

sleep(3)

checkAllExamsCheckbox = driver.find_element(By.XPATH, "//div[@class='styled__RightUpperStyled-g86x8t-11 fmQatT']")
checkAllExamsCheckbox.click()
sleep(5)
allCheckbox[0].click()



sleep(3)
confirmButton = driver.find_element(By.XPATH, '//button[@class="button__BaseButtonWrapper-sc-13jeiy3-1 dTIkKH styled__BaseButtonStyled-f1adih-3 gvjJnE"]')
confirmButton.click()
sleep(10)

#Scrollowanie po stronie i printowanie pytań i odpowiedzi
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '*//div[@class = "sc-1a0xt0b-0 hYYdyS"]')))
questionsOnSite = driver.find_elements(By.XPATH, '*//div[@class = "sc-1a0xt0b-0 hYYdyS"]')
for oneQuestion in questionsOnSite:
    action.move_to_element(oneQuestion).perform()
    question = oneQuestion.find_element(By.XPATH, '*//p')
    print(question.get_attribute("innerText"))
    try:
        listInQuestion = oneQuestion.find_element(By.XPATH, '*//ol')
        print(listInQuestion.get_attribute('innerText'))
    except:
        print('brak listy')
    answers = oneQuestion.find_elements(By.XPATH, '*//span[@class = "ltqprq-5 gTyLTL"]')
    a=1
    for answer in answers:
        print(str(a) + ") " + answer.get_attribute("innerText"))
        a=a+1
