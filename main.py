from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class ResultApp(App):

    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.title = Label(text="📊 Result Checker", font_size=28)

        self.obtained = TextInput(hint_text="Obtained Marks", multiline=False)
        self.total = TextInput(hint_text="Total Marks", multiline=False)

        self.result = Label(text="Enter marks and press check", font_size=18)

        self.btn = Button(text="Check Result", on_press=self.check_result)

        self.layout.add_widget(self.title)
        self.layout.add_widget(self.obtained)
        self.layout.add_widget(self.total)
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.result)

        return self.layout

    def play_sound(self, file):
        sound = SoundLoader.load(file)
        if sound:
            sound.play()

    def check_result(self, instance):
        try:
            obtained = float(self.obtained.text)
            total = float(self.total.text)

            if total <= 0:
                self.result.text = "Invalid Total Marks"
                return

            percent = (obtained / total) * 100

            if percent >= 60:
                self.result.text = f"PASS ✅ ({percent:.2f}%)"
                self.play_sound("pass.wav")

            elif percent >= 50:
                self.result.text = f"NEAR PASS ⚠️ ({percent:.2f}%)"
                self.play_sound("near.wav")

            else:
                self.result.text = f"FAIL ❌ ({percent:.2f}%)"
                self.play_sound("fail.wav")

        except:
            self.result.text = "Enter valid numbers"


if __name__ == "__main__":
    ResultApp().run()
