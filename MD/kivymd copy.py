from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView



example="""
MDTextField:
    hint_text:"Please input user name"
    helper_text:"Remember just to put the number"
    pos_hint:{'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:300
"""
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style="Dark"
        screen=Screen()
        input=MDTextField(text='Please input user name', pos_hint={'center_x':0.5,'center_y':0.5},size_hint_x=None,width=300)
        #screen.size=(23,23)
        #button=MDRoundFlatButton(text='Checking', pos_hint={'center_x':0.5,'center_y':0.4}, on_release=self.takedata)
        #screen.add_widget(button)
        label=MDLabel(font_style='H1',text='hello',halign='center', theme_text_color='Custom',text_color=(0,1,0,1))  
        #self.input=Builder.load_string(example)
        list_view=MDList()
        scroll=ScrollView()
        #item1= OneLineListItem(text='Female')
        #item2= OneLineListItem(text='Male')
        #list_view.add_widget(item1)
        #list_view.add_widget(item2)
        #scroll.add_widget(list_view)
        #screen.add_widget(button)
        #screen.add_widget(self.input)
        screen.add_widget(scroll)
        return screen
    #def takedata(self,obj):
        #print(self.input.text)
 
MainApp().run()