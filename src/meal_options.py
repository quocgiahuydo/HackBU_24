import numpy as np
from src.constants import Constants as C

class Meals:
    def __init__(self,cal,pro,nutri):
        self.cal = cal
        self.pro = pro
        self.nutri = nutri
    def meal_combos(self):
        CAL_TOLERANCE = self.cal/20
        self.cal_sum = 0
        self.pro_sum = 0
        self.meal_items = []
        repeat =0
        repeated_meals = []
        P_TOLERANCE = self.pro/20
        
        while not (self.cal - CAL_TOLERANCE < self.cal_sum < self.cal + CAL_TOLERANCE) and not (self.pro - P_TOLERANCE < self.pro_sum < self.pro + P_TOLERANCE):
            temp = np.random.randint(len(self.nutri))
            if self.nutri[temp][0] in self.meal_items:  
               repeat += 1 
               
            self.meal_items.append(self.nutri[temp][0])
            self.cal_sum += self.nutri[temp][1]
            self.pro_sum += self.nutri[temp][2]
            print(1)
        for i in self.meal_items:
            if self.meal_items.count(i) > 1:
                repeated_meals.append(f"{self.meal_items.count(i)} {i}")
                print(2)
                self.meal_items = [meals for meals in self.meal_items if meals != i]    
            self.meal_items += repeated_meals
            print(3)
            
            
            





