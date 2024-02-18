from bs4 import BeautifulSoup
import os
import requests
from datetime import date
import os



def get_c4_menu():
    current_day = date.today().strftime('%A')
    folder_path = 'food_menus/'
    pdf_path = os.path.join(folder_path, 'c4.pdf')
    pdf_link = None
    soup = BeautifulSoup(requests.get('https://binghamton.sodexomyway.com/dining-near-me/c4-dining-hall').text, "html.parser")
    foodmenu_divs = soup.find('div', class_='rtf').find_all('div')
    for foodmenu_div in foodmenu_divs:
        for link in foodmenu_div.find_all('a'):
            if current_day in link.text:
                pdf_link = 'https:' + link.get('href')
                break
        if pdf_link:
            break
    with open(pdf_path, 'wb') as pdf_file: pdf_file.write(requests.get(pdf_link).content)
    print(pdf_link)
        
         

get_c4_menu()