from bs4 import BeautifulSoup
import os
import requests
from datetime import date
import os


class Dining_Hall_Menu:
    def __init__(self,name,link):
        self.link = str(link)
        self.name = str(name)
    def get_hall_menu(self,link,name):
        current_day = date.today().strftime('%A')
        folder_path = 'food_menus/'
        pdf_path = os.path.join(folder_path, f'{name}.pdf')
        pdf_link = None
        soup = BeautifulSoup(requests.get(f'{link}').text, "html.parser")
        foodmenu_divs = soup.find('div', class_='rtf').find_all('div')
        for foodmenu_div in foodmenu_divs:
            for link in foodmenu_div.find_all('a'):
                if current_day in link.text:
                    pdf_link = 'https:' + link.get('href')
                    break
            if pdf_link:
                break
        with open(pdf_path, 'wb') as pdf_file: pdf_file.write(requests.get(pdf_link).content)
        return pdf_path
        
        