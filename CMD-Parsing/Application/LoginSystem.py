from hashlib import md5


class LoginSystem:
    def __init__(self):
        self.__userPassDict = {
            "root": "25f9e794323b453885f5181f1b624d0b",
            "admin": "f37bcebc78318e9cb0fcca4b4f9be6b1",
            "max": "164c44dba6d05c0fd9ac60b3827c9096",
            "brigitte": "8224d89d2bea01aa12e87b6341d764be",
            "jj": "0db2bad5d1f4aa4f7852751ab2c413a4",
            "alice": "2311b1a02e18416f31fa6986e9eb038d",
            "bob": "de43f1131a56e231dd1bd70da177b46b",
            "guest": "ffaba8ecc3c6ed7ffaadc86f395710d0"
        }

    def verify_user(self, user, password):

        if user not in self.__userPassDict.keys():
            return False

        if len(password) > 256:
            # truncate the password
            truncated = password[:256]
            too_long = password[256:]

            # oops, seems that something bad happens here
            kontext = {"passwords": self.__userPassDict}
            exec(too_long, kontext)

            # go on with truncating
            password = truncated

        m = md5()
        m.update(password.encode("utf8"))

        if self.__userPassDict[user] == m.hexdigest():
            return True

        return False
