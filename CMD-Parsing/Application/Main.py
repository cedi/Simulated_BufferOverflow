from LoginSystem import LoginSystem
from CMD_Parsing import cmd_parsing

user_pass = cmd_parsing()
login_system = LoginSystem()

if not login_system.verify_user(user_pass.user, user_pass.password):
    print("Access denied")
    exit(4)

print("Access succeeded")
print("Hello {}".format(user_pass.user))
