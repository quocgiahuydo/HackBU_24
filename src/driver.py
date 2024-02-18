from src.person import Person
from src.constants import Constants as C
from src.data_config.dining_hall_file import Dining_Hall_File
from src.data_config.nutrition import Nutrition
from src.data_config.pdf_to_txt import Pdf_To_Txt
from src.data_config.txt_process import Txt_Process
from src.meal_options import Meals

class Driver:
    def __init__ (self):
        pass


    def config_data(self):
        #for i in range(len(C.hall_links)):
           temp = Dining_Hall_File(C.hall_links[0][0],C.hall_links[0][1])
           Pdf_To_Txt(temp.get_hall_file())


    def person_setup(self):
        age = input("please enter your age ")
        weight = input("please enter your weight in lbs ")
        height = input("please enter your height in inches ")
        sex = input("please enter your sex, male or female ")
        exercise = int(input("please enter your exercise level on a scale of 1-10"))-5
        self.person = Person(age,weight,height,sex, exercise)
        self.person.bmi_calc()
        self.person.calories()
        self.person.nutrients()
        print(self.person.carbs_g)
        print(self.person.fats_g)
        print(self.person.fiber_g)
        print(self.person.protein_g)


    


           

    def run(self):
        #self.config_data()
        self.person_setup()
        x = Txt_Process("c4.txt","c4_output.txt")
        food = Nutrition("c4_output.txt")
        food.values()
        meal1 = Meals(self.person.daily_cal,self.person.protein_g,food.cal_pro_list)
        meal1.meal_combos()
        meal2 = Meals(self.person.daily_cal,self.person.protein_g,food.cal_pro_list)
        meal3 = Meals(self.person.daily_cal,self.person.protein_g,food.cal_pro_list)
        print(f"{meal1.meal_items}this set of meal has daily cals {meal1.cal_sum} and total protien {meal1.pro_sum} grams")
        
        
       
        


    

    