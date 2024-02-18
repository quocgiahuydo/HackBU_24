import convertapi
from src.api_key import API

class Pdf_To_Txt:
    def __init__(self,data):
        file , name = data
        convertapi.api_secret = f'{API.pdf_2_text}'
        convertapi.convert('txt', {
            'File': file
        }, from_format = 'pdf').save_files("food_menus/"+ name + ".txt")
