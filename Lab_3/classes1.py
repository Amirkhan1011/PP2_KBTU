class String:
    def getString(self):
        self.userInput = str(input())
    def printString(self):
        print(self.userInput.upper())

smth = String()
smth.getString()
smth.printString()