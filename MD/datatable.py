from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class mainApp(MDApp):
    def build(self):
        screen=Screen()
        table=MDDataTable(check=True,
            pos_hint={'center_x':0.5,'center_y':0.5}
                          ,column_data=[
                        ("Food",dp(30)),
                        ("Calories",dp(30))
        ],
        row_data=[
            ("Burger","300"),
            ("Fries","200")
        ])
        screen.add_widget(table)
        return screen
mainApp().run()