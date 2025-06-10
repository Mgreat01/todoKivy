from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.snackbar import Snackbar

class TodoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('app.kv')

    def add_task(self):
        task_input = self.root.ids.task_input
        task = task_input.text.strip()
        if task:
            self.root.ids.task_list.add_widget(OneLineListItem(text=task))
            task_input.text = ''
        else:
            Snackbar(text="Veuillez entrer une tâche !").open()

if __name__ == "__main__":
    from kivy.lang import Builder
    TodoApp().run()
