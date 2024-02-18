from src.constants import Constants as C
class Person:
    def __init__(self,age,weight,height,sex,exercise):
        self.age = int(age)
        self.weight = int(weight)
        self.height = int(height)
        self.sex = sex
        self.exercise = exercise


    def bmi_calc(self):
        #Checks Age to direct to proper formula 
        if self.age >= 20:
            return self.adult_bmi()
        elif self.age >= 2:
            return self.child_bmi()
        else:
            return "bmi cannot be calculated accuratly for children under 2 years old"


    def adult_bmi(self):
        self.bmi = (self.weight/(self.height**2)* 703)
        #checks which range the bmi falls into and returns the weight classifcation 
        for i in range(len(C.BMI_RANGES)):
            if C.BMI_RANGES[i][1] <= self.bmi <= C.BMI_RANGES[i][2]:
                self.weight_status = C.BMI_RANGES[i][0]
                return self.bmi ,self.weight_status

    def calories(self):
        self.daily_cal = (4.5*self.weight)+(self.height*15.6) -(5*self.age)
        if self.sex == "male":
            self.daily_cal += 5
        else:
            self.daily_cal -= 161
        if self.exercise != 0:
            self.daily_cal += 100 * self.exercise

    def macro_nut(self,low,high,cal_per_g):
        low_num = int(float(self.daily_cal) * low /cal_per_g)
        high_num = int(float(self.daily_cal) * high / cal_per_g)
        return low_num,high_num

    
    def nutrients(self):
        self.carbs_g = self.macro_nut(C.CARB_PERCENT_RANGE[0],CARB_PERCENT_RANGE[1],4)
        self.fats_g = self.macro_nut(C.FAT_PERCENT_RANGE[0],FAT_PERCENT_RANGE[1],9)
        self.fiber_g = int(self.daily_cal / 1000 *14)
        self.protein_g = int(self.weight *.5)
            

        


