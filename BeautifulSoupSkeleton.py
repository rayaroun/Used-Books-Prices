import csv
import requests
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



    def get_url(self):
        #https://www.amazon.ca/s?k=978-0195626438&ref=nb_sb_noss

        template = "https://www.amazon.ca/s?k={}&ref=nb_sb_noss"

        self.url =  template.format(self.isbn)
        print(self.url)
        self.driver.get(self.url)
        return self.url



    def get_used_books_link(self):


        self.soup = BeautifulSoup(self.driver.page_source,'html.parser')

        self.results = self.soup.find_all('span', {'class' : 'a-declarative'})

        print(self.results)


    
    def get_soup(self,url):
        response = requests.get(url)
        if response.ok:
            return BeautifulSoup(response.text, features="html.parser")

    def get_links(self,soup):
        links = []
        for tag in soup.findAll("a", href=True):
            if img := tag.img:
                img = img.get("src")
            links.append(dict(url=tag.get("href"), text=tag.text, img=img))
        return links

        



    # self.url = get_url()
    # driver.get(url)




khushwant = scraper("978-0195626438")
url = khushwant.get_url()
khushwant.get_used_books_link()

