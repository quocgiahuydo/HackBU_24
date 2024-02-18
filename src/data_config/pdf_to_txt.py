import convertapi
from src.food import Food
from src.api_key import API

class Pdf_to_Txt(self,file):
    convertapi.api_secret = f'{API.pdf_2_text}'
    convertapi.convert('txt', {
        'File': file
    }, from_format = 'pdf').save_files('src.data_config')
