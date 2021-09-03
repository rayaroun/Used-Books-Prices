import csv
from bs4 import BeautifulSoup   
from selenium import webdriver


#chrome driver

driver = webdriver.Chrome()

url = "https://www.amazon.ca/"

# driver.get(url)

def get_url(search_term : str):
    #https://www.amazon.ca/s?k=978-0195626438&ref=nb_sb_noss

    template = "https://www.amazon.ca/s?k={}&ref=nb_sb_noss"
    search_term = search_term.replace(" " , "+")
    return template.format(search_term)


url = get_url('978-0195626438')
driver.get(url)
