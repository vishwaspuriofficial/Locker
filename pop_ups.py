from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
  
def sameNewPasswordPlz():
  pop = Popup(title = "Unsuccessful password reset", size_hint = (0.4,0.6), content = Label(text = "Make sure you typed \nyour new password correctly", halign = "center"))
  pop.open()


def noPasswordSpacePlz():
  pop = Popup(title = "Unsuccessful password reset", size_hint = (0.4,0.6), content = Label(text = "Please do not include\n spaces in your new password", halign = "center"))
  pop.open() 


def noDupPlz():   #create user
  pop = Popup(title = "Unsuccessful Account Creation", size_hint = (0.4,0.6), content = Label(text = "This account has already \n been created", halign = "center"))
  pop.open()


def noSpacePlz():   #create user
  pop = Popup(title = "Unsuccessful Account Creation", size_hint = (0.4,0.6), content = Label(text = 
  """Please do not include
   any spaces in your
  - username
  - password
  - email"""))
  pop.open()


def noBlankPlz():   #create user
  pop = Popup(title = "Unsuccessful Account Creation", size_hint = (0.4,0.6), content = Label(text = "Please make sure you have\n filled in every blank", halign = "center"))
  pop.open()


def noInvalidValuePlz():    #login user
  pop = Popup(title = "Unsuccessful Login", size_hint = (0.4,0.4), content = Label(text = "Incorrect Username \nand/or Password\nClick anywhere to escape.", halign = "center"))
  pop.open()


def noInvalidEmailPlz(): 
  pop = Popup(title = "Unsuccessful register", size_hint = (0.4,0.6), content = Label(text = "Invalid email address \n try again please.", halign = "center"))
  pop.open()

def noInvalidPasswordResetEmailPlz():
  pop = Popup(title = "Email Unable to Send", size_hint = (0.4,0.6), content = Label(text = "Invalid email address \nPlease try again.", halign = "center"))
  pop.open()

def successfullySentEmail():
  pop = Popup(title = "Email Sent!", size_hint = (0.4,0.6), content = Label(text = "An email with your new temporary \npassword has been sent.", halign = "center"))
  pop.open()