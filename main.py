import default_events as default
import global_vars as gv

def input_event():
  command = input("event > ")
  return command

def input_value(value_name):
  txt = str(value_name + " > ")
  value = input(txt)
  return value

def call_event(input_event): 
  """
To add a call to a custom event, place inside the match : 
---------------------------------------------------------------------
case "invocation name":
    return modulo_name.function_name(input_value("value name"))
    
-----index-----------------------------------------------------------
    modulo_name = name of the module or file where your function is located.
    funtion_name = is the name of the function.
    input_value("value name") [optional] = this if your function takes arguments, indicates what arguments are          going to be passed to it
  """
  match input_event:
    case "sayHello":
      return default.sayHello()
    case "help":
      return default.help()
    case "end":
      return default.endLoop()
    case "clear":
      return default.clear()
    case "new username":
      return default.changeUserName(input_value("new username"))
    case "new password":
      return default.changePassword(input_value("new password"))
    case "info":
      return default.systemInfo()
    case "___level up___":
      if default.validateLevelRoot():
        return default.levelUp_root()
    case "all accounts":
      if default.validateLevelRoot():
        return default.infoAllAccounts()
    case "print":
      return default.write(input_value("text"))
    case "show session":
      return default.showSession()
    case _:
      return print(input_event + ": invalid event name, please verify the name:")
  
def loop():
  while gv.LOOP:
    call_event(input_event())

def main():
  if gv.LOOP == False:
    gv.LOOP = True
  print("-------------------")
  default.login()
  loop()

main()
