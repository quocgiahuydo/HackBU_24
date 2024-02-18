from src.person import Person
from src.diet import Diet
from src.constants import Constants as C
from src.data_config.dining_hall_file import Dining_Hall_File
from src.data_config.nutrition import Nutrition

class Driver():
    def __init__ (self):
        pass


    def config_data(self):
        for i in range(len(C.hall_links)):
           temp = Dining_Hall_File(C.hall_links[i][0],C.hall_links[i][1])
           temp.get_hall_file()
           

    def run(self):
        dining 
        asindis
        sdjisdj

    

    