import convertapi
from src.food import Food
from src.api_key import API

class Pdf_to_Txt:
    def __init__(self,file):
        convertapi.api_secret = f'{API.pdf_2_text}'
        convertapi.convert('txt', {
            'File': file
        }, from_format = 'pdf').save_files('src.data_config')
