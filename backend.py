from ClientInfo import *
import re
import smtplib, ssl
from random import randint

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'    #will be used to check if an email address is valid
_client = Client(None, None, None)

    
def checkForUser(userName, password=None, email=None):
  global _client
  with open("UserDB.txt", "r") as db:
    for data in db:
      userdata = data.split(" ")
      userdata[-1] = userdata[-1].replace("\n", "")

      #For forgot password override purposes 
      if userName == "LoginOverride" and userdata[0] == email:
        return [userdata[0], userdata[1], userdata[2]]
      
      #For login purposes 
      if email == None:

        if userdata[1] == userName and userdata[2] == password:
          return [userdata[0], userdata[1], userdata[2]]

        elif userdata[1] == userName and userdata[2] != password:
          return "wrong"

      #For checking dupe userName and email purposes
      elif userdata[0] == email or userdata[1] == userName:
        return "found"

    else:
      return "not found"


def createUser(email, userName, password):
  global _client
  if email == "" or userName == "" or password == "": #CHecks if textbox is blank
    return "blank"
  
  elif ((" " in email) or (" " in userName) or (" " in password)): 
    return  "space"
  
  elif re.search(regex, email) == None:
    return "invalid"

  elif checkForUser(userName,email=email) == "not found":
    _client = Client(email, userName, password)
    _client.storeToDB()
    _client = Client(None, None, None)
    return "success"

  else:
    return "dup"      #return value, signal pop up


def login(userName, password):
  global _client
  data = checkForUser(userName, password=password)
  if isinstance(data, list):
    _client = Client(data[0], data[1], data[2])
    return True
  else:
    return False      #return boolean, signal pop up

def logout():
  global _client
  _client = Client(None, None, None)


def recoveryEmail(email):
  global _client
  data = checkForUser("LoginOverride", email=email)
  
  if data == "not found":
    return "not found"

  tempPassword = randint(10000000, 99999999)
  _client = Client(data[0], data[1], tempPassword)
  _client.changeInfoInDB()

  port = 465
  sender = "hhacketthon@gmail.com"
  password = "dgGYgf3627"
  recieve = email

  message = f"""Subject: Reset Password\n\n
Dear {_client.userName},

You are receiving this email because we received a forget password request for your account.

Here is your temporary password: {tempPassword} 

Login your account with this password and change your password according to your preference.

If you did not request a temporary password, no further action is required.

Regards,
Locker"""
  #message = f"Subject: Reset Password\n\n{text}"
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recieve, message)
  logout()