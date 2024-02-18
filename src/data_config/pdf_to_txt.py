import convertapi
from src.food import Food

class Pdf_to_Txt(self,file):
    convertapi.api_secret = 'mP6YytAVdPNN76aK'
    convertapi.convert('txt', {
        'File': file
    }, from_format = 'pdf').save_files('src.data_config')
