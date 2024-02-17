from constants import Constants as C
class Diet():
    def __init__(self,age,bmi,weight,weight_status,sex,exercise,height):
        self.bmi = bmi
        self.weight = weight 
        self.height = height
        self.weight_status = weight_status
        self.sex = sex
        self.exercise = exercise
        self.age = age

    def calories(self):
        self.daily_cal = (4.5*self.weight)+(self.height*15.6) -(5*self.age)
        if self.sex == "male":
            self.daily_cal += 5
        else:
            self.daily_cal -= 161
        
        return self.daily_cal

    def nutrients(self):
        self.carb_range = 

    
