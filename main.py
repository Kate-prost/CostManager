from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CostManagerApp(MDApp):
    def build(self):
        return MDLabel(text='Hello Kate', halign="center")


CostManagerApp().run()