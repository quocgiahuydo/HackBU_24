import requests
import os
from src.api_key import API


class Nutrition:
    def __init__(self,file):
        self.file = file
        self.list = []
    def values(self):
        for aline in self.file:
            query = aline
            api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
            response = requests.get(api_url, headers={'X-Api-Key': f"{API.nutrition_api}"})
            self.list.append(response.text) #[["calories",dict[0]['calories']],["fat",dict[0]["fat_total_g"]],["protein",dict[0]["protein_g"]],["carbohydrates",dict[0]["carbohydrates_total_g"]],["fiber",dict[0]["fiber_g"]]]
            print(aline)
            #print(self.list)

            