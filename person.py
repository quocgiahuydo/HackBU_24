class Person:
    def __init__(self,age,weight,height,sex,metric):
        self.age = int(age)
        self.weight = int(weight)
        self.height = int(height)
        self.sex = sex
        self.metric = metric


    def bmi_calc(self):
        #Checks Age to direct to proper formula 
        if self.age >= 20:
            return self.adult_bmi()
        elif age >= 2:
            return self.child_bmi()
        else:
            return "bmi cannot be calculated accuratly for children under 2 years old"


    def adult_bmi(self):
        #checks if numbers are in metric and then calculates 
        if self.metric:
            self.bmi = self.weight/((self.height*100)**2)
        else:
            self.bmi = (self.weight/(self.height**2)* 703)
        









    def print(self):
        print(self.age)
        print(self.weight)
        print(self.height)
        print(self.sex)
