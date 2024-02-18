from bs4 import BeautifulSoup
import os
import requests
from datetime import date
import os


class Dining_Hall_File:
    def __init__(self,name,link):
        self.link = str(link)
        self.name = str(name)
    def get_hall_file(self):
        current_day = date.today().strftime('%A')
        folder_path = 'food_menus/'
        pdf_path = os.path.join(folder_path, f'{self.name}.pdf')
        pdf_link = None
        soup = BeautifulSoup(requests.get(f'{self.link}').text, "html.parser")
        foodmenu_divs = soup.find('div', class_='rtf').find_all('div')
        for foodmenu_div in foodmenu_divs:
            for h_link in foodmenu_div.find_all('a'):
                if current_day in h_link.text:
                    pdf_link = 'https:' + h_link.get('href')
                    break
            if pdf_link:
                break
        with open(pdf_path, 'wb') as pdf_file: pdf_file.write(requests.get(pdf_link).content)
        return pdf_path
        
        