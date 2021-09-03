#Git - git remote add UsedBooks https://github.com/rayaroun/Used-Books-Prices.git

import csv
from bs4 import BeautifulSoup   
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

class scraper: 


    def __init__(self,isbn : str) -> None:
        self.isbn = isbn
        self.driver = webdriver.Chrome(options=chrome_options)
        print(self.isbn)

    #chrome driver

    # driver = webdriver.Chrome()

    # url = "https://www.amazon.ca/"

    # driver.get(url)

    def get_url(self):
        #https://www.amazon.ca/s?k=978-0195626438&ref=nb_sb_noss

        template = "https://www.amazon.ca/s?k={}&ref=nb_sb_noss"

        self.url =  template.format(self.isbn)
        print(self.url)
        self.driver.get(self.url)
        



    # self.url = get_url()
    # driver.get(url)




khushwant = scraper("978-0195626438")
khushwant.get_url()