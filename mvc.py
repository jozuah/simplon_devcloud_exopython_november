class model:
    def __init__(self):
        pass

    def hello():
        print("hello Model")

    def getSentences(self):
        continueWrite = "y"
        listOfUserString = []

        while continueWrite == "y":
            print("Ajouter la phrase au fichier")
            userString = input()
            userString = self._upperCase(userString)
            userString = userString + "\n"
            listOfUserString.append(userString)
            print("Voulez vous continuer ? (y/n)")
            continueWrite = input()
        
        return listOfUserString
    
    def _upperCase(self, userString):
        return userString.upper()

class vue:
    def __init__(self):
        pass

    def hello():
        print("hello Vue")

    def readInFile():
        #Open file in Append only mode "a"
        file = open("userSenteces.txt","r")
        #Read file and write each line in a list
        eachLineInFileList = file.readlines()
        eacheLineInFileString = ''.join(eachLineInFileList)
        #Close file
        file.close()
        print(eacheLineInFileString)

class controller:
    def __init__(self):
        pass

    def hello():
        print("hello Controller")

    def writeInFile(listOfUserString):
        #Open file in Append only mode "a"
        file = open("userSenteces.txt","a")
        #Write in the file with a list
        file.writelines(listOfUserString)
        #Close file
        file.close()

#model.hello()
#vue.hello()
#controller.hello()

model = model()
my_list = model.getSentences()
controller.writeInFile(my_list)
vue.readInFile()

#y_string = "blabla"
#model = model()
#print(model._upperCase(my_string))
