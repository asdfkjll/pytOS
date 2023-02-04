print("default_events.py - OK")
"""
in this code go all the default events of the PytOS system
"""
import global_vars as gv
import os

def validateLevelRoot(): #!important
  # return print(gv._rootUser["level"])
  if gv.users[gv.session][2] != "root":
    print("You do not have the necessary level to perform this action.")
    return False
  return True

def sayHello():
  return print("Hello, everyone!")

def help():
  return print("""
-------------------------------
• sayHello : is in charge of greeting.
• help : help.
• end : finish the loop of program and ends its execution.
• clear: clear the console.
• new username [value required]: change username. 
• new password [value required]: change password.
• info : show info.
• show session : show session.
• ___level up___ [only root] : upgrade to root a account.
• all accounts [only root] : show all accounts.
• print [value required] : print text to console. Example : 
event > print
text > Hello, world!
-------------------------------
""")

def endLoop():
  gv.LOOP = False

def clear():
  return os.system("clear")

def write(txt):
  return print(txt)

def systemInfo():
  return print(gv.show_info(gv.session))

def levelUp_root():
  showAccounts()
  # gv._rootUser["level"] = "root"
  selection = selectAccount()
  gv.users[int(selection)][2] = "root"
  return print("You've leveled up, congratulations! :D")

# [inicia] todo lo reacionados con el sistema de cuentas:
  
# se encarga de cambiar y validar el nombre de usuario root
def vLengthUserName(userName): #validateLengthOfUserName
  minLen = 5
  maxLen = 20
  if len(userName) < minLen or len(userName) > maxLen:
    if len(userName) < minLen:
      print("• El nombre de usuario debe contener al menos", minLen ,"caracteres.")
    elif len(userName) > maxLen:
      print("• El nombre de usuario no puede contener más de", maxLen ,"caracteres.")
    return False
  return True

def vCaractersUserName(userName): #validateCaractersOfUserName
  # &, $, @, -, %, * y espacio en blanco
  # invalidCaracters = ["&", "$", "@", "-", "%", "*", " "]
  invalidCaracters = "&$@-%* "
  # for x in invalidCaracters.length:
  #   print(invalidCaracters[x])
  for char in invalidCaracters:
    if char in userName:
      print("• el nombre no puede contener ninguno de los siguientes caracteres: ", invalidCaracters, "tampoco el espacio.")
      return False
  return True

def validateUserName(userName):
  validate1 = vLengthUserName(userName)
  validate2 = vCaractersUserName(userName)
  
  if validate1 and validate2:
    print("nombre de usuario valido")
    return True
  print("nombre de usuario no valido")
  print("no valid user name, fuck you!")
  return False

# def inputUserName():
#   userName = input("Ingrese el nombre de usuario: ")
#   return userName

def changeUserName(newUserName):
  nameCheck = validateUserName(newUserName)
  if nameCheck == True:
    gv.users[gv.session][0] = newUserName
    return print("Username:",gv.users[gv.session][0])
  return print("Username:",gv.users[gv.session][0])

#se encarga de validar la contraseña elegida por el usuario
def vLengthPassword(password): #validateLengthOfPassword
  if len(password) < 6:
    print("• La contraseña no es segura, debe de contener mas de 6 caracteres.")
    return False
  return True

def vContentPassword(password):
  caracters = "&$@-%*"
  if " " in password:
    print("• La contraseña no puede contener espacios.")
    return False
  x = False
  for char in caracters:
    if char in password:
      x = True
  if x == True:
    return True
  print("• La contraseña debe de contener alguno de los siguientes caracteres:", caracters)
  return False

def validatePassword(password):
  validate1 = vLengthPassword(password)
  validate2 = vContentPassword(password)
  
  if validate1 and validate2:
    print("contraseña valida")
    return True
  print("contraseña no valida")
  print("no valid password, fuck you!")
  return False

def changePassword(newPassword):
  passwordCheck = validatePassword(newPassword)
  if passwordCheck == True:
    gv.users[gv.session][1] = newPassword
    return print("Password:",gv.users[gv.session][1])
  return print("Password:",gv.users[gv.session][1])
########

# cuenta
def infoAllAccounts():
  for account in gv.users:
    print(account)

def showSession():
  return print(gv.session)
  
# acceder a una cuenta
def showAccounts():
  i = 1
  while i < len(gv.users):
    print("[",(i),"]",":", gv.users[i][0])
    i += 1

def selectAccount():
  print("-------------------")
  selection = input("select an account > ")
  return selection

def startAccount(account):
  gv.session = int(account)
  return print("Session started - successfully:", gv.users[gv.session][0])

def enterPassword():
  password = input("password > ")
  return password

def login():
  showAccounts()
  select = selectAccount()
  selectName = gv.users[int(select)][0]
  selectPass = gv.users[int(select)][1]
  print("----", selectName ,"--------------")
  if enterPassword() == selectPass:
    startAccount(select)
    welcome() 
    return
  print("--Incorrect password.------")
  endLoop()

# [termina] todo lo reacionados con el sistema de cuentas:

def welcome():
  print("""-------------------
Hello, world! welcome to pytOS.
Write [help] for more information.
-------------------""")
  