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

    def macro_nut(self,low,high,cal_per_g):
        low_num = self.calories * low /cal_per_g
        high_num = self.calories * high / cal_per_g
        return low_num,high_num





    def nutrients(self):
        self.carbs_g = self.macro_nut(.45,.65,4)
        self.fats_g = self.macro_nut(.20,.35,9)
        self.fiber_g = self.daily_cal / 1000 *14
        self.protein_g = 0



    
