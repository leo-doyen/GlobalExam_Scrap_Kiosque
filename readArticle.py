import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def read(articleUrl, driver):

    # on boucle pour chaque url
    for url in articleUrl:
        # on se connecte a l'url courrant
        driver.get(url)

        time.sleep(1)

        y = 20
        # cette boucle permet de scroller lentement pendeant 10 minutes
        for timer in range(0,700):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += 20  
            time.sleep(1)   

