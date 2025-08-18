from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.config import Config
from kivy.core.window import Window

# Fix window size for desktop
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Window.clearcolor = (0, 0, 0, 1)  # black fallback

class TaskItem(BoxLayout):
    task_text = StringProperty()
    delete_callback = ObjectProperty()
    completed = BooleanProperty(False)

    def toggle_done(self, checkbox, value):
        self.completed = value
        if value:
            self.ids.label.text = f"[s]{self.task_text}[/s]"
            self.ids.label.color = (0.6, 0.6, 0.6, 1)
        else:
            self.ids.label.text = self.task_text
            self.ids.label.color = (1, 1, 1, 1)

    def delete_task(self, *_):
        self.delete_callback(self)

class TaskManager(BoxLayout):
    def add_task(self):
        txt = self.ids.task_input.text.strip()
        if txt:
            item = TaskItem(task_text=txt, delete_callback=self.remove_task)
            self.ids.task_grid.add_widget(item)
            self.ids.task_input.text = ''

    def remove_task(self, widget):
        self.ids.task_grid.remove_widget(widget)

class TaskApp(App):
    def build(self):
        return TaskManager()

if __name__ == '__main__':
    TaskApp().run()
