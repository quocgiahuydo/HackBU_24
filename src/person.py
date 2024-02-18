from src.constants import Constants as C
class Person:
    def __init__(self,age,weight,height,sex):
        self.age = int(age)
        self.weight = int(weight)
        self.height = int(height)
        self.sex = sex


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
                return self.weight_status
            
            

        

        









    def print(self):
        print(self.age)
        print(self.weight)
        print(self.height)
        print(self.sex)
