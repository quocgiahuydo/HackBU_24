import requests
import os


class Nutrition:
    def __init__(self,food):
        self.food = str(food)
    def values(self):
        query = self.food
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': os.getenv('nutrition_api')})
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            print("Error") 
food = Nutrition("scrambled eggs")
print(food.values())
