from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.button import Button, ButtonBehavior
import json, glob, random
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, username, password):
        with open("users.json") as file:
            users = json.load(file)
        
        if (username in users and users[username]["password"] == password):
            self.manager.current = "login_success_screen"
        else:
            self.ids.idLoginFail.text = "Login fail! Username or password is incorrect!"

class SignUpScreen(Screen):
    def add_user(self, username, password):
        with open("users.json") as file:
            users = json.load(file)

        users[username] = {"username": username, "password": password, "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        with open("users.json", "w") as file:
            json.dump(users, file)

        self.manager.current = "sign_up_success_screen"

class SignUpSuccessScreen(Screen):
    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class LoginSuccessScreen(Screen):
    def logout(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feelingTxt):
        feeling = feelingTxt.lower()

        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]

        if (feeling in available_feelings):
            with open(f"quotes/{feeling}.txt", encoding="utf8") as file:
                data = file.readlines()
                self.ids.idTextResult.text = random.choice(data)
        else:
            self.ids.idTextResult.text = "There is no result"

class ImageButton(ButtonBehavior, Image, HoverBehavior):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()