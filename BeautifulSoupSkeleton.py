import csv
import re
import requests
from bs4 import BeautifulSoup   
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

class scraper: 
    def __init__(self,isbn : str) -> None:
        self.isbn = isbn
        self.condition_array = []
        self.price_array = []
        self.condition_price_dict = {}

        # self.driver = webdriver.Chrome(options=chrome_options)
        print(self.isbn)



    def get_url(self):
        #https://www.amazon.ca/s?k=978-0195626438&ref=nb_sb_noss

        template = "https://www.amazon.ca/s?k={}&ref=nb_sb_noss"

        self.url =  template.format(self.isbn)
        print(self.url)

        


        # self.driver.get(self.url)
        return self.url



    def get_used_books_link(self):

        # html = requests.get(url)


        with open('webtxt.html', 'r') as f:

            contents = f.read()


        soup = BeautifulSoup(contents,'html.parser')



        self.results = soup.find("a", string=re.compile("offers"))

        return self.results



    def get_used_prices_from_link(self):

        # with open('usedpagelink.html', 'r') as f:

        #     contents = f.read()

        with open('usedpagelink.html', encoding="utf8") as f:
            contents = f.read()
        
        soup = BeautifulSoup(contents,'html.parser')

        div_results_condition = soup.find_all("div",{"id": "aod-offer-heading"})
        div_results_price = soup.find_all( "span",{"class": "a-price-whole"} )

       
        # for x in div_results_condition:
            # tempCondition = x.text.strip().split()
            # key = " ".join(tempCondition)

        for condition,price in div_results_condition , div_results_price:
            tempCondition = condition.text.strip().split()
            key = " ".join(tempCondition)

            value = int(price.text.rstrip('.'))

            self.condition_price_dict[key].append(value)

        print()
        #     self.condition_price_dict[]
            # print(x.text.rstrip('.'))
    



        



    # self.url = get_url()
    # driver.get(url)




khushwant = scraper("978-0195626438")
url = khushwant.get_url()
link_results = khushwant.get_used_books_link()
time.sleep(3)
khushwant.get_used_prices_from_link()


# The following gets the page where the used prices are listed
# (link_results['href']) 

#saving the page manually for now and opening it here 






