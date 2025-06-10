from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder

class TodoApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('app.kv')

    def add_task(self):
        task_input = self.root.ids.task_input
        task_text = task_input.text.strip()

        if not task_text:
            Snackbar(text="Veuillez entrer une tâche !").open()
            return

        task_list = self.root.ids.task_list
        if len(task_list.children) >= 50:
            Snackbar(text="Limite de 50 tâches atteinte. Supprimez-en une avant d'ajouter.").open()
            return

        # Création d'une tâche cliquable avec suppression au clic long
        item = OneLineListItem(text=task_text)
        item.bind(on_release=self.show_delete_dialog)
        task_list.add_widget(item)
        task_input.text = ''

        Snackbar(text=f"Tâche ajoutée : {task_text}").open()

    def show_delete_dialog(self, instance_item):
        # Popup confirmation suppression
        self.dialog = MDDialog(
            title="Supprimer la tâche",
            text=f"Voulez-vous supprimer :\n'{instance_item.text}' ?",
            buttons=[
                MDFlatButton(text="Annuler", on_release=self.close_dialog),
                MDFlatButton(text="Supprimer", on_release=lambda x: self.delete_task(instance_item))
            ],
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def delete_task(self, item):
        self.root.ids.task_list.remove_widget(item)
        self.dialog.dismiss()
        Snackbar(text=f"Tâche supprimée : {item.text}").open()

if __name__ == "__main__":
    TodoApp().run()
