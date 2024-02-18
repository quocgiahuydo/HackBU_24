from src.person import Person
from src.constants import Constants as C
from src.data_config.dining_hall_file import Dining_Hall_File
from src.data_config.nutrition import Nutrition
from src.data_config.pdf_to_txt import Pdf_To_Txt

class Driver:
    def __init__ (self):
        pass


    def config_data(self):
        #for i in range(len(C.hall_links)):
           temp = Dining_Hall_File(C.hall_links[0][0],C.hall_links[0][1])
           txt = Pdf_To_Txt(temp.get_hall_file())


    def person_setup(self):
        age = input("please enter your age ")
        weight = input("please enter your weight in lbs ")
        height = input("please enter your height in inches ")
        sex = input("please enter your sex, male or female ")
        exercise = int(input("please enter your exercise level on a scale of 1-10"))-5
        person = Person(age,weight,height,sex, exercise)
        person.bmi_calc()
        person.calories()
        person.nutrients()
        print(person.carbs_g)
        print(person.fats_g)
        print(person.fiber_g)
        print(person.protein_g)


    


           

    def run(self):
        self.config_data()
        self.person_setup()
        


    

    