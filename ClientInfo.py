class Client():


  def __init__(self, email, userName, password):
    self.email = email
    self.userName = userName 
    self.password = password
  

  #Create a function to change username and password
  def changePassword(self, password):
    self.password = password

    
  def storeToDB(self):
    with open("UserDB.txt", "a") as db:
      db.write(f"{self.email} {self.userName} {self.password} \n")
  
  def changeInfoInDB(self):
    tempDB = open("UserDB.txt", "r") 
    dbInfo = tempDB.readlines() 
    for x in range(len(dbInfo)):
      if dbInfo[x].split(" ")[0] == f"{self.email}":
        dbInfo[x] = f"{self.email} {self.userName} {self.password} \n"
        break
    tempDB.close()

    tempDB = open("UserDB.txt", "w")
    for lines in range(len(dbInfo)):
      tempDB.write(dbInfo[lines])
    tempDB.close()
    
