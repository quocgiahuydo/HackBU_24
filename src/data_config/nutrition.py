import requests
import os
from src.api_key import API
import json


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
                self.list.append(response.text[0]) 
                self.x = response.text.replace("]\n[",",")
                self.x = json.loads(self.x)
                if self.x != []:
                    self.cal_pro_list.append([self.x[0]["name"], self.x[0]["calories"], self.x[0]["protein_g"]])
