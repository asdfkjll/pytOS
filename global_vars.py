print("global_vars.py - OK")
LOOP = True
"""
to access user data use: 
users[a][b,c,d]
---- index -----
[a][x] = user
[b][0] = username
[c][1] = password
[d][2] = level
"""
users = [
  ["null", "null", "root"],
  ["test", "123", "normal_user"],
  ["test_2", "456", "normal_user"],
  ["Daniel_PytOS", "daniel es proo", "root"],
  ["di que eres mi perra >:U", "soy tu perra", "root"]
]

# _rootUser = {
#   "username": "root",
#   "password": "root",
#   "level": "root" #privilege level
# }

session = 0

def show_info(session):
  info = users[session]
  system_info = """
pytOS version 0.01
created 29/01/2023
---user-info------------
""" + str(info) + "\n"
  return system_info
