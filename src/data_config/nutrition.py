import requests
import os
from src.api_key import API

class Nutrition:
    def __init__(self,food):
        self.food = str(food)
    def values(self):
        query = self.food
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': f"{API.nutrition_api}"})
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            print("Error") 
food = Nutrition("Country Style Scrambled Eggs")
print(food.values())
