from src.person import Person
from src.diet import Diet
from src.constants import Constants as C
from src.data_config.dining_hall_file import Dining_Hall_File
#from src.data_config.nutrition import Nutrition
from src.data_config.pdf_to_txt import Pdf_To_Txt

class Driver():
    def __init__ (self):
        pass


    def config_data(self):
        #for i in range(len(C.hall_links)):
           temp = Dining_Hall_File(C.hall_links[0][0],C.hall_links[0][1])
           txt = Pdf_To_Txt(temp.get_hall_file())
           

    def run(self):
        dining 
        asindis
        sdjisdj

    

    