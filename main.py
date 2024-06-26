import tkinter as tk
import json
import os


class Account:
    def __init__(self, name, src, isProtected, passw):
        self.name = name
        self.src = src
        self.isProtected = isProtected
        self.passw = passw

    def getName(self):
        return self.name
    
    def getSrc(self):
        return self.src
    
    def getIsProtected(self):
        return self.isProtected
    
    def getPassw(self):
        return self.passw

    def getObject(self):
        return {
            'name': self.name,
            'src': self.src,
            'isProtected': self.isProtected,
            'passw': self.passw
        }

class AccountsDB:
    def __init__(self):
        self.accounts = self.loadFromFile()

    def loadFromFile(self):
        try:
            with open('./Accounts.json', 'r') as file:
                data = json.load(file)
                return [Account(value['name'], value['src'], value['isProtected'], value['passw']) for value in data]
        except FileNotFoundError:
            return []
        
    def saveToFile(self):
        with open('./Accounts.json', 'w') as file:
            json.dump([account.getObject() for account in self.accounts], file, indent=2)

    def createAccount(self, name, passw = ""):
        if self.isNameFree(name):
            #if the password is empty, the isProtected property will be set to false
            isProtected = True
            if passw == "":
                isProtected = False
            #the src is generated using the name, spaces are replaced with '-'
            src = name.replace(' ', '-')
            self.accounts.append(Account(name, src, isProtected, passw))
            #saving to file automatically when change is made (account created)
            self.saveToFile()
            #create a folder for the account
            #TODO: check if the folder doesnt already exist!
            os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), src))
            return True
        return False

    def isNameFree(self, name):
        for account in self.accounts:
            if account.getName() == name:
                return False
        return True
    
    def getAccounts(self):
        return self.accounts
    
    def getAccount(self, name):
        for account in self.accounts:
            if name == account.getName():
                return account
        return 0




# #######################################################
class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Login to Clients & Services Manager')
        self.geometry('500x400')
        self.resizable(False, False)

        self.header = tk.Label(self, text='Login to CSM', font=('Lato', 24))
        self.header.pack(pady=16)





# def main():
#     _ACCOUNT = None
#     accounts = AccountsDB()

#     while not _ACCOUNT:
#         print("Choose account")
#         for account in accounts.getAccounts():
#             print(account.getName())
#         name = input("Enter name: ")
#         if not accounts.isNameFree(name):
#             if input("Enter password: ") == accounts.getAccount(name).getPassw():
#                 _ACCOUNT = accounts.getAccount(name)
#                 break
#             print("Invalid password.")
#             continue
#         print("Invalid name.")

#     print(f"You're logged in as {_ACCOUNT.getName()}.")
        




    

if __name__ == "__main__":
    # main()
    loginForm = LoginForm()
    loginForm.mainloop()