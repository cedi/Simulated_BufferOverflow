from argparse import ArgumentParser
from collections import namedtuple
from getpass import getuser


def cmd_parsing():
    parser = ArgumentParser()
    parser.add_argument("-u", "--user", dest="user", type=str, help="\
        alternative login to system login")
    parser.add_argument("-p", "--password", dest="password", type=str, help="\
        password for accessing the application")

    args = parser.parse_args()

    user = str()
    password = str()

    if args.user:
        user = args.user
    else:
        user = getuser()

    if args.password:
        password = args.password

    if user == "":
        print("please enter a valid user to enter the system")
        exit(2)

    if password == "":
        print("please enter a valid password to enter the system")
        exit(2)

    if len(user) > 256:
        print("you entered a invalid username. Usernames are at maximum 256 \
characters long")
        exit(3)

    if len(password) > 256:
        print("you entered a invalid password. Passwords are at maximum 256 \
characters long")

        # mising exit(3) here - this is "the" bug

    user_pass = namedtuple("UserPass", ["user", "password"])
    return user_pass(user=user, password=password)
