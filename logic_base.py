from random import randint

Alphabet = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26, " " : 27}

ListOfKeys = list(Alphabet.keys()) #Save the Alphabet dict keys 
ListOfValues = list(Alphabet.values()) #Save the Alphabet dict values

CodeKeyList = list()
CodeKey = int()

MessageFList = list()

class rotors:
    def __init__(self, NumberOfRotation):
        self.NumberOfRotation = NumberOfRotation
        self.StartingLetter = int() #integer corresponding at the ID of the letter in the dict 
        self.Message = str()
        self.LetterID = int()
        self.NewLetterID = int()
        self.NewLetterKey = str()
        self.NewLetter = str()
        self.NewLetterIDNF = int()
        self.NewLetterIDNF2 = int()
        self.MessageNF = str()
        self.MessageF = str()
        self.NewLetterID2 = int()
        self.key = str()
        self.keyList = list()
        self.OldLetter = str()
        self.OldLetterID = int()
        self.OldMessageList = list()
        self.OldMessage = str()
        
    def encode(self):
        self.Message = input("Enter a message ")
        self.MessageNF = self.Message 
        MessageList = list()
        for j in range(self.NumberOfRotation):
            #Definition the ammount of rotation
            self.StartingLetterID = randint(0, 26)  
            # self.StartingLetter = ListOfKeys[self.StartingLetterID]
            # self.StartID = Alphabet[self.StartingLetter]
            
            for i in self.MessageNF:
                self.StartingLetter = ListOfKeys[self.StartingLetterID]
                self.StartID = Alphabet[self.StartingLetter]
                self.LetterID = Alphabet[i]
                self.NewLetterIDNF = self.LetterID + self.StartID
                self.NewLetterIDNF2 = self.NewLetterIDNF - 26
                self.NewLetterID = ListOfValues[self.NewLetterIDNF2 - 1]
                self.NewLetterKey = ListOfKeys[self.NewLetterID - 1]
                self.NewLetter = self.NewLetterKey 
                MessageList.append(self.NewLetter)
                CodeKeyList.append(str(self.StartingLetterID))   #create a key to decode the message 
                if self.StartingLetterID < 26:
                    self.StartingLetterID += 1
                else:
                    self.StartingLetterID = 0 
            
            #Front end part         
            self.MessageF = "".join(MessageList)
            self.MessageNF = self.MessageF
            MessageFList.append(self.MessageF) 
            self.MessageF = None 
            self.MessageF = str()
            MessageList = None 
            MessageList = list()
        
        # for i in range(self.NumberOfRotation - 1):
        #     MessageFList.pop()
        
        self.MessageF = MessageFList[-1]
        CodeKey = "/".join(CodeKeyList)
        print(self.MessageF)
        print(CodeKey)
    
    def decode(self):
        self.NumberOfRotation = int(input("Number of rotation: ")) 
        self.Message = input("Enter the message you want to decode: ")
        self.key = input("Enter the key to decrypt: ")
        self.keyList = self.key.split("/")
        for i in self.keyList:
            int(i)
        for i in range(self.NumberOfRotation):
            for j in self.Message:
                self.OldLetterID = Alphabet[j] - int(self.keyList[-i])
                self.OldLetterID -= i 
                self.OldLetter = ListOfValues[self.OldLetterID - 1] 
                self.OldMessageList.append(self.OldLetter)
                print(self.OldMessageList) 
        self.OldMessage = "".join(str(self.OldMessageList)) 
        self.OldMessage = "".join(self.OldMessage)
        for i in range(len(self.OldMessageList)):
            self.OldMessageList[i] - i         
        print(self.OldMessage)      
        print(self.OldMessageList)       