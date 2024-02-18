import requests
import os
from src.api_key import API



class Nutrition:
    def __init__(self,file):
        self.file = file
        self.list = []
        self.cal_pro_list =[]
    def values(self):
        with open(self.file, 'r') as f:
            for aline in f:
                query = str(aline)
                api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
                response = requests.get(api_url, headers={'X-Api-Key': f"{API.nutrition_api}"})
                self.list.append(response.text[0]) #[["calories",dict[0]['calories']],["fat",dict[0]["fat_total_g"]],["protein",dict[0]["protein_g"]],["carbohydrates",dict[0]["carbohydrates_total_g"]],["fiber",dict[0]["fiber_g"]]]
                self.x = response.text.strip("[]")
                print(self.x)
                self.x = ast.literal_eval(self.x)
                print(type(self.x))

            #[{"name": "turkey", "calories": 193.1, "serving_size_g": 100.0, "fat_total_g": 7.4, "fat_saturated_g": 2.2, "protein_g": 28.6, "sodium_mg": 104, "potassium_mg": 226, "cholesterol_mg": 110, "carbohydrates_total_g": 0.1, "fiber_g": 0.0, "sugar_g": 0.0}]