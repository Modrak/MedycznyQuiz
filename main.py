from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd


Questions = pd.DataFrame(columns=["category_id","question_text","ans_1","ans_2","ans_3","ans_4","ans_5","hint_1","hint_2","hint_3","hint_4","hint_5","correct_ans","LDEK_CEM"])
Categories = pd.DataFrame()
new_row = {}


def doesElementExist(webElement: WebElement):
    return WebElement.size != 0

def accept_cookies():
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '*//button[@id="rcc-confirm-button"]')))
    cookiesAcceptButton = driver.find_element(By.XPATH, '*//button[@id="rcc-confirm-button"]')
    cookiesAcceptButton.click()

def log_in():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
    loginBox = driver.find_element(By.NAME, 'username')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
    passwordBox = driver.find_element(By.NAME, 'password')
    loginBox.send_keys(login)
    passwordBox.send_keys(password)
    passwordBox.send_keys(Keys.ENTER)

def prepare_and_log_in():
    driver.get(ulr)
    driver.maximize_window()
    accept_cookies()
    log_in()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1")))
    sleep(1)

def select_all_exams_and_confirm():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "*//div[@class = 'dropdownIndicator__DropdownIndicatorStyled-sc-1pzr9y6-0 kuQVZE']")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='styled__RightUpperStyled-g86x8t-11 fmQatT']")))
    combo_boxes_on_rigt_site = driver.find_elements(By.XPATH, "*//div[@class = 'dropdownIndicator__DropdownIndicatorStyled-sc-1pzr9y6-0 kuQVZE']")
    combo_box_for_ldek_labels = combo_boxes_on_rigt_site[1]
    combo_box_for_ldek_labels.click()
    sleep(1)
    check_all_exams_checkbox = driver.find_element(By.XPATH, "//div[@class='styled__RightUpperStyled-g86x8t-11 fmQatT']")
    check_all_exams_checkbox.click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/main/div[7]/div/form/div/div[2]/div[1]/div/div/div/div/div//input")))
    allCheckbox = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/main/div[7]/div/form/div/div[2]/div[1]/div/div/div/div/div//input")
    for checkbox_of_single_type_of_exam in allCheckbox:
        checkbox_of_single_type_of_exam.click()
    sleep(3)
    confirmButton = driver.find_element(By.XPATH, '//button[@class="button__BaseButtonWrapper-sc-13jeiy3-1 dTIkKH styled__BaseButtonStyled-f1adih-3 gvjJnE"]')
    confirmButton.click()

def switch_to_single_question_per_view():
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//fieldset[@role='radiogroup' and @class='styled__WrapperStyled-sc-1an04d2-0 dElMTf']//label[@for]")))
    singleQuestionButton = driver.find_elements(By.XPATH, "//fieldset[@role='radiogroup' and @class='styled__WrapperStyled-sc-1an04d2-0 dElMTf']//label[@for]")[0]
    singleQuestionButton.click()

def find_question_on_site():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'styled__ContentWrapStyled-sc-1nz0tmd-0 hCoAeg']")))
    single_question = driver.find_element(By.XPATH, "//div[@class = 'styled__ContentWrapStyled-sc-1nz0tmd-0 hCoAeg']")
    return single_question

def get_text_of_question(question: WebElement):
    div_with_question_text = question.find_element(By.XPATH, ".//div[@class = 'sc-15f9xfp-0 iBLmhG']")
    text = div_with_question_text.get_property("innerText")
    return text

def get_hints_from_question(question: WebElement):
    hints = []
    allAnswersDiv = question.find_element(By.XPATH, './/div[@class = "ltqprq-0 uqgwj"]')
    answerDiv = allAnswersDiv.find_elements(By.XPATH, './div')
    x = 1
    for answer in answerDiv:
        sleep(1)
        answer.click()
        if (answer.get_attribute("class") == "ltqprq-1 fmBuQq" or answer.get_attribute("class") == "ltqprq-1 iontpb"):
            print("Odpowiedź błędna")
        else:
            print("Odpowiedź poprawna")
        answerHint = answer.find_element(By.XPATH, './div[2]').get_property("innerText")[:-20]
        print("______HINT______")
        print(answerHint)
        x = x+1
        hints = hints + [answerHint]
    print(hints)
    return hints

def get_answers_from_question(question: WebElement):
    answers = []
    allAnswersDiv = question.find_element(By.XPATH, './/div[@class = "ltqprq-0 uqgwj"]')
    answerDiv = allAnswersDiv.find_elements(By.XPATH, './div')
    x = 1
    for answer in answerDiv:
        sleep(1)
        answer.click()
        if (answer.get_attribute("class") == "ltqprq-1 fmBuQq" or answer.get_attribute("class") == "ltqprq-1 iontpb"):
            print("Odpowiedź błędna")
        else:
            print("Odpowiedź poprawna")
        answerText = answer.find_element(By.XPATH, './div[1]').get_property("innerText")[4:-5]
        answerHint = answer.find_element(By.XPATH, './div[2]').get_property("innerText")[:-20]
        print("______TEXT______")
        print(answerText)
        print("______HINT______")
        print(answerHint)
        x = x+1
        answers = answers + [answerText]
    print(answers)
    return answers

#TODO zrobione zbieranie odpowiedzi do listy - trzeba zrobić zbieranie z listy i przypisywanie je do nowego wiersza + poprawić nazwy w metodzie^^
#TODO zrobić osobną metode do wyjmowania Hintów - dokladnie tak samo jak jest metoda od wyjmowania odpowiedzi


def define_category_by_text(text):
    if text == "Stomatologia zachowawcza":
        return 1
    elif text == "Endodoncja":
        return 2
    elif text == "Stomatologia dziecięca":
        return 3
    elif text == "Chirurgia stomatologiczna":
        return 4
    elif text == "Protetyka":
        return 5
    elif text == "Periodontologia":
        return 6
    elif text == "Ortodoncja":
        return 7
    elif text == "Medycyna ratunkowa, anestezjologia i intensywna terapia":
        return 8
    elif text == "Orzecznictwo":
        return 9
    elif text == "Bioetyka i prawo medyczne":
        return 10
    elif text == "Zdrowie publiczne":
        return 11
    else: return 12

# def get_list_of_answers_from_questions(question: WebElement):
# question


driver = webdriver.Chrome()
action = ActionChains(driver)
login = "ecv70944@omeie.com"
password = 'ziomek123'
ulr = 'https://lepolek.pl/logowanie'


prepare_and_log_in()
driver.get('https://lepolek.pl/nauka')
select_all_exams_and_confirm()
sleep(3)
switch_to_single_question_per_view()

print(get_text_of_question(find_question_on_site()))

answers_in_list = get_answers_from_question(find_question_on_site())
hints_in_list = get_hints_from_question(find_question_on_site())

new_row = dict({'ans_1' : answers_in_list[0],
           "ans_2" : answers_in_list[1],
           "ans_3" : answers_in_list[2],
           "ans_4" : answers_in_list[3],
           "ans_5" : answers_in_list[4],
           "hint_1" : answers_in_list[0],
           "hint_2" : answers_in_list[1],
           "hint_3" : answers_in_list[2],
           "hint_4" : answers_in_list[3],
           "hint_5" : answers_in_list[4]})

print(new_row)


#____________Trzeba sprawdzic czy to konieczne do zdobycia tabeli z pytania___________
# try:
#     listInQuestion = single_question.find_element(By.XPATH, '*//ol')
#     print(listInQuestion.get_property('innerText')+ "testtt")
# except:
#     print()


next_question_button = driver.find_element(By.XPATH, "//button[@class='sc-1tepzgd-2 iKgyQ mbnl6g-1 drIMVw']")
next_question_button.click()
sleep(70)
