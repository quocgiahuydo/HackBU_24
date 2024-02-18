from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from driver import Driver 
from person import Person



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


class mainApp(MDApp,Driver):
    Window.size=(360,600)
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen=Screen()
       
        label=MDLabel(text="Calories Tracker", halign="center", font_style="Subtitle1",pos_hint={"center_x":0.5,"center_y":0.9})
        self.input_age=Builder.load_string(age)
        self.input_age_tag=Builder.load_string(age_label)
        self.input_weight=Builder.load_string(weight)
        self.input_weight_tag=Builder.load_string(weight_label)
        self.input_height=Builder.load_string(height)
        self.input_height_tag=Builder.load_string(height_label)
        self.input_exercise=Builder.load_string(exercise)
        self.input_exercise_tag=Builder.load_string(exercise_label)
        button=MDRoundFlatButton(text='Checking'
                                 , pos_hint={'center_x':0.5,'center_y':0.4}
                                 , on_release=self.takedata)
        self.male=MDRoundFlatButton(
                          text='Male',
                          halign='center', 
                          theme_text_color='Custom',
                          text_color=(0,1,0,1),
                          pos_hint={'center_x':0.55,'center_y':0.5},
                          size_hint=(0.05,0.05),
                          on_release=self.male)
        
        self.female=MDRoundFlatButton(text='Female',
                        halign='center', 
                        theme_text_color='Custom',
                        text_color=(0,1,0,1),
                        pos_hint={'center_x':0.80,'center_y':0.5},
                        size_hint=(0.05,0.05),
                        on_release=self.female)
        
        self.input_gender_tag=Builder.load_string(gender_label)
        
        screen.add_widget(label)
        screen.add_widget(self.input_age)
        screen.add_widget(self.input_age_tag)

        screen.add_widget(self.input_weight)
        screen.add_widget(self.input_weight_tag)
        screen.add_widget(self.input_height)
        screen.add_widget(self.input_height_tag)
        screen.add_widget(self.male)
        screen.add_widget(self.female)
        screen.add_widget(self.input_gender_tag)

        screen.add_widget(self.input_exercise)
        screen.add_widget(self.input_exercise_tag)
        return screen
    def male(self,obj):
        self.gender="male"
    def female(self,obj):
        self.gender="female"
    def takedata(self,obj):
        person = Person(self.input_age,self.input_weight,self.input_height,self.gender,self.input_exercise)
        person.bmi_calc()
        person.calories()
        person.nutrients()
        print(person.carbs_g)
        print(person.fats_g)
        print(person.fiber_g)
        print(person.protein_g)
mainApp().run()  