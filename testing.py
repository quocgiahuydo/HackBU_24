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
from kivy.app import App

state = "start"

age= """
MDTextField:
    hint_text:"Please input your age"
    helper_text:"Remember just to put the number"
    pos_hint:{'center_x':0.6,'center_y':0.8}
    size_hint_x:None
    width:200
"""


weight= """
MDTextField:
    hint_text:"Please input user weight"
    helper_text:"Remember to use lbs"
    pos_hint:{'center_x':0.6,'center_y':0.70}
    size_hint_x:None
    width:200
"""


height= """
MDTextField:
    hint_text:"Please input user height"
    helper_text:"Remember just to put the number"
    pos_hint:{'center_x':0.6,'center_y':0.6}
    size_hint_x:None
    width:200
"""




exercise= """
MDTextField:
    hint_text:"Please enter user exercise level "
    helper_text:"on a scale of 1-10"
    pos_hint:{'center_x':0.6,'center_y':0.4}
    size_hint_x:None
    width:200
"""
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'
        MDLabel:
            text: "Calories Tracker"
            halign:center
            font_style:Subtitle1
            pos_hint:{"center_x":0.5,"center_y":0.9}
        MDTextField:
            hint_text:"Please input your age"
            helper_text:"Remember just to put the number"
            pos_hint:{'center_x':0.6,'center_y':0.8}
            size_hint_x:None
            width:200
        MDLabel:
            text:"Age: "
            halign:"center"
            font_style:"Subtitle2"
            pos_hint:{"center_x":0.3,"center_y":0.8}
        MDTextField:
            hint_text:"Please input user weight"
            helper_text:"Remember to use lbs"
            pos_hint:{'center_x':0.6,'center_y':0.70}
            size_hint_x:None
            width:200
        MDLabel:
            text:"Weight: "
            halign:"center"
            font_style:"Subtitle2"
            pos_hint:{"center_x":0.3,"center_y":0.70}
        MDTextField:
            hint_text:"Please input user height"
            helper_text:"Remember just to put the number"
            pos_hint:{'center_x':0.6,'center_y':0.6}
            size_hint_x:None
            width:200
        MDLabel:
            text:"Height: "
            halign:"center"
            font_style:"Subtitle2"
            pos_hint:{"center_x":0.3,"center_y":0.6}
            


        MDLabel:
            text:"Gender: "
            halign:"center"
            font_style:"Subtitle2"
            pos_hint:{"center_x":0.3,"center_y":0.5}
            
        MDTextField:
            hint_text:"Please enter user exercise level "
            helper_text:"on a scale of 1-10"
            pos_hint:{'center_x':0.6,'center_y':0.4}
            size_hint_x:None
            width:200

        MDLabel:
            text:"Exercise: "
            halign:"center"
            font_style:"Subtitle2"
            pos_hint:{"center_x":0.3,"center_y":0.4}
        

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass    

class SettingsScreen(Screen):
    pass

class TestApp(MDApp):
    def build(self):
        # Create the MenuScreen manager
        sm = ScreenManager()
        self.gender=[]
        
        label=MDLabel(text="Calories Tracker", halign="center", font_style="Subtitle1",pos_hint={"center_x":0.5,"center_y":0.9})
        self.input_age=Builder.load_string(age)
        self.input_weight=Builder.load_string(weight)
        self.input_height=Builder.load_string(height)
        self.input_exercise=Builder.load_string(exercise)
        self.button=MDRoundFlatButton(text='Submit'
                                , pos_hint={'center_x':0.5,'center_y':0.2}
                                , on_release=self.takedata)
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


        #self.button2=MDRoundFlatButton(text='Continue'
                                ## , on_press=sm.current('test'))
        #MenuScreen.add_widget(self.button2)
        sm.add_widget(MenuScreen)
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm
    def male(self,obj):
        self.gender.append('male')
    def female(self,obj):
        self.gender.append('female')
    def moveto(self,obj):
        print("testing")
    def takedata(self,obj):
        person = Person(float(self.input_age.text),float(self.input_weight.text),float(self.input_height.text),self.gender[-1],float(self.input_exercise.text))
        person.bmi_calc()
        person.calories()
        person.nutrients()
        print(person.carbs_g)
        print(person.fats_g)
        print(person.fiber_g)
        print(person.protein_g)

       

if __name__ == '__main__':
    TestApp().run()





