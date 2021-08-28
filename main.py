from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CostManagerApp(MDApp):
    def build(self):
        return MDLabel(text='Hello Manager', halign="center")


CostManagerApp().run()