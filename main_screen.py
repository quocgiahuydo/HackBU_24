from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from src.driver import Driver 
from src.person import Person
from kivy.uix.button import Button



age= """
MDTextField:
    hint_text:"Please input your age"
    helper_text:"Remember just to put the number"
    pos_hint:{'center_x':0.6,'center_y':0.8}
    size_hint_x:None
    width:200
"""
age_label="""
MDLabel:
    text:"Age: "
    halign:"center"
    font_style:"Subtitle2"
    pos_hint:{"center_x":0.3,"center_y":0.8}
       
"""

weight= """
MDTextField:
    hint_text:"Please input user weight"
    helper_text:"Remember to use lbs"
    pos_hint:{'center_x':0.6,'center_y':0.70}
    size_hint_x:None
    width:200
"""
weight_label="""
MDLabel:
    text:"Weight: "
    halign:"center"
    font_style:"Subtitle2"
    pos_hint:{"center_x":0.3,"center_y":0.70}
       
"""

height= """
MDTextField:
    hint_text:"Please input user height"
    helper_text:"Remember just to put the number"
    pos_hint:{'center_x':0.6,'center_y':0.6}
    size_hint_x:None
    width:200
"""
height_label="""
MDLabel:
    text:"Height: "
    halign:"center"
    font_style:"Subtitle2"
    pos_hint:{"center_x":0.3,"center_y":0.6}
       
"""


gender_label="""
MDLabel:
    text:"Gender: "
    halign:"center"
    font_style:"Subtitle2"
    pos_hint:{"center_x":0.3,"center_y":0.5}
       
"""

exercise= """
MDTextField:
    hint_text:"Please enter user exercise level "
    helper_text:"on a scale of 1-10"
    pos_hint:{'center_x':0.6,'center_y':0.4}
    size_hint_x:None
    width:200
"""
exercise_label="""
MDLabel:
    text:"Exercise: "
    halign:"center"
    font_style:"Subtitle2"
    pos_hint:{"center_x":0.3,"center_y":0.4}
       
"""



gender_label="""
MDLabel:
    text:"Gender: "
    halign:"center"
    font_style:"Subtitle2"
    pos_hint:{"center_x":0.3,"center_y":0.5}
 """      
class mainApp(MDApp,Driver):
    Window.size=(360,600)
    def build(self):

        self.sm=ScreenManager()
        self.screen=Screen(name='input')
        self.gender=[]
        self.theme_cls.primary_palette="Green"
        
        self.label=MDLabel(text="Calories Tracker", halign="center", font_style="Subtitle1",pos_hint={"center_x":0.5,"center_y":0.9})
        self.input_age=Builder.load_string(age)
        self.input_age_tag=Builder.load_string(age_label)
        self.input_weight=Builder.load_string(weight)
        self.input_weight_tag=Builder.load_string(weight_label)
        self.input_height=Builder.load_string(height)
        self.input_height_tag=Builder.load_string(height_label)
        self.input_exercise=Builder.load_string(exercise)
        self.input_exercise_tag=Builder.load_string(exercise_label)
        self.button=MDRoundFlatButton(text='Submit'
                                 , pos_hint={'center_x':0.5,'center_y':0.2}
                                 , on_release=self.second_phase)
        self.male_input=MDRoundFlatButton(
                          text='Male',
                          halign='center', 
                          theme_text_color='Custom',
                          text_color=(0,1,0,1),
                          pos_hint={'center_x':0.55,'center_y':0.5},
                          size_hint=(0.05,0.05),
                          on_release=self.male)
        
        self.female_input=MDRoundFlatButton(text='Female',
                        halign='center', 
                        theme_text_color='Custom',
                        text_color=(0,1,0,1),
                        pos_hint={'center_x':0.80,'center_y':0.5},
                        size_hint=(0.05,0.05),
                        on_release=self.female)
        
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.input_exercise)
        self.screen.add_widget(self.input_age)
        self.screen.add_widget(self.input_age_tag)

        self.screen.add_widget(self.input_weight)
        self.screen.add_widget(self.input_weight_tag)
        self.screen.add_widget(self.input_height)
        self.screen.add_widget(self.input_height_tag)
        self.screen.add_widget(self.male_input)
        self.screen.add_widget(self.female_input)

        self.input_gender_tag=Builder.load_string(gender_label)
        self.screen.add_widget(self.input_gender_tag)

        self.screen.add_widget(self.input_exercise_tag)
        self.screen.add_widget(self.button)

      

        
        self.sm.add_widget(self.screen)
        return self.sm
    
    def clean_canvas(self,obj):
        self.screen.canvas.clear()
        self.answer="exit"
    def male(self,obj):
        self.gender.append('male')
    def female(self,obj):
        self.gender.append('female')
    def moveto(self,obj):
        print("testing")
    def second_phase(self,obj):
        self.label2=MDLabel(text="Calories Tracker", halign="center", font_style="Subtitle1",pos_hint={"center_x":0.5,"center_y":0.9})
       
        self.clean_canvas(self)
        self.answer="submit"
        person = Person(float(self.input_age.text),float(self.input_weight.text),float(self.input_height.text),self.gender[-1],float(self.input_exercise.text))
        print(person.bmi_calc())
        person.calories(),person.nutrients()
        protein = person.protein_g
        BMI=MDLabel(text="Your BMI:  "+str(person.bmi_calc()),
                         halign="center",font_style="Subtitle2",
                         pos_hint={"center_x":0.5 ,"center_y":0.8})
        Cal=MDLabel(text="Your calories is:  "+str(person.daily_cal),
                         halign="center",font_style="Subtitle2",
                         pos_hint={"center_x":0.5 ,"center_y":0.7})
        Pro=MDLabel(text="The required protein is:  "+str(protein),
                         halign="center",font_style="Subtitle2",
                         pos_hint={"center_x":0.5 ,"center_y":0.6})
        self.screen.add_widget(self.label2)
        self.screen.add_widget(BMI)
        self.screen.add_widget(Pro)
        self.screen.add_widget(Cal)

        return self.sm


mainApp().run()  