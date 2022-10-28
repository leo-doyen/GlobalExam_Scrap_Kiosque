import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from readArticle import read
from logs import getEmail


# on recupere l'email
mail = getEmail()

# cette fonction permet d'empecher de rentrer un mot de passe vide
def checkPassword():
    print('passsword for global exam ?')
    searchInput = input()
    if searchInput == '':
        print('You must enter a search term')
        checkPassword()
    else:
        return searchInput

# cette fonction est utilisée pour vérifier si le mot de passe n'est pas vide puis retourne l'entrée
password = checkPassword()
print(password)

driver = webdriver.Chrome()
driver.get("https://exam.global-exam.com/")
time.sleep(3)



# on implemente le mail dans le champ email
email = driver.find_element(By.ID, 'email')
email.send_keys(mail)


# on implemente le mot de passe dans le champ password
passw = driver.find_element(By.ID, 'password')
passw.send_keys(password)


# on valide le formulaire de connexion
button = driver.find_element(By.CLASS_NAME, 'button-solid-primary-big.mb-6')
button.click()


time.sleep(1)

# permet de valider les cookies
cookies = driver.find_element(By.ID, 'axeptio_btn_acceptAll').click()

# on recupere les la liste des articles de la section kioske
articleDiv = driver.find_element(By.ID, 'tns-articles').find_elements(By.TAG_NAME, 'a')
print(articleDiv)

articleUrl = []
for art in articleDiv:
    # pour chaque article on stocke le lien vers celui ci
    articleUrl.append(art.get_attribute('href'))

# on apelle la methode pour lire les articles en lui passant une liste d'url et le driver courant
read(articleUrl, driver)



time.sleep(1)
driver.get('https://exam.global-exam.com/stats')