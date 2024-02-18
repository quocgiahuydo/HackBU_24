import convertapi
from food import Food
convertapi.api_secret = 'mP6YytAVdPNN76aK'
convertapi.convert('txt', {
    'File': 'food_menus/Resident Dining Menus_Day8_C4_tcm207-130090.pdf'
}, from_format = 'pdf').save_files('test')
