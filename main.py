import backend
import pop_ups
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.window import Window

Window.size = (800, 600)  #Vishwas Puri Finally Found it, so we dont hv to keep resizing!

class tabs(TabbedPanel):
	def Print(self, string):
		print(string)

	def get_login_info(self):
		if not backend.login(str(self.usernameLogin.text), str(self.password.text)):
			pop_ups.noInvalidValuePlz()
		else:
			kv2.current = "inside"

	def get_create_account_info(self):
		createUserFunc = backend.createUser(str(self.email.text), str(self.username.text), str(self.passwordSignUp.text))
		if createUserFunc == "success":
			return "success"
		elif createUserFunc == "dup":
			pop_ups.noDupPlz()
		elif createUserFunc == "space":
			pop_ups.noSpacePlz()
		elif createUserFunc == "blank":
			pop_ups.noBlankPlz()
		elif createUserFunc == "invalid":
			pop_ups.noInvalidEmailPlz()

class CreateAccountWindow(Screen):
  username = ObjectProperty(None)
  email = ObjectProperty(None)
  password = ObjectProperty(None)
	#Defines these as object properties so we can get them from the ui

  def clear_text_inputs(self):
    username.text = ""
    email.text = ""
    password.text = ""

class ForgotWindow(Screen):
  def forgot_password(self, email):
    report = backend.recoveryEmail(email)
    if report == "not found":
      pop_ups.noInvalidPasswordResetEmailPlz()
    else:
      pop_ups.successfullySentEmail()
      self.manager.current = "main"

class LoginWindow(Screen):
	login_label = ObjectProperty(None)
	usernameLogin = ObjectProperty(None)
	password = ObjectProperty(None)
  
	def get_login_info(self):

		if not backend.login(str(self.usernameLogin.text), str(self.password.text)):
			pop_ups.noInvalidValuePlz()
		else:
			kv2.current = "inside"

def forget_password(self, email):
  backend.recoveryEmail(email)

class InsideWindow(Screen):
	def logout(self):
		backend.logout()
    #here

class WelcomeWindow(Screen):
	pass

class MainWindow2(Screen):
	pass

class ChangeWindow(Screen):
  def change_password(self, password, password_confirm):
    if (" " in password) or (" " in password_confirm):
      pop_ups.noPasswordSpacePlz()
    elif password == password_confirm:
      backend._client.changePassword(password)
      backend._client.changeInfoInDB()
      return True
    else:
      pop_ups.sameNewPasswordPlz()

class WindowManager(ScreenManager):
	_username = ""
	_password = ""

	def backend_login(self, username, password):
		backend.login(username, password)

#kv = Builder.load_file("test.kv")
kv2 = Builder.load_file("test2.0.kv")

class TestApp(App):
	def build(self):
		return kv2

TestApp().run()