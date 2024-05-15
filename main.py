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

    def isNameFree(self, name):
        for account in self.accounts:
            if account.getName() == name:
                return False
        return True





def main():
    accounts = AccountsDB()





    

if __name__ == "__main__":
    main()