from random import randint

Alphabet = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}

ListOfKeys = list(Alphabet.keys()) #Save of the Alphabet keys 
ListOfValues = list(Alphabet.values()) #Save of the Alphabet values

CodeKey = list()

class rotors:
    def __init__(self, NumberOfRotation):
        self.NumberOfRotation = NumberOfRotation
        self.StartingLetter = int() #integer corresponding at the ID of the letter in the dict 
        self.Message = input("Enter a message ")
        self.LetterID = int()
        self.NewLetterID = int()
        self.NewLetterKey = str()
        self.NewLetter = str()
        self.NewLetterIDNF = int()
        self.NewLetterIDNF2 = int()
        self.MessageNF = str()
        self.MessageF = str()
        self.NewLetterID2 = int()
        
    def encode(self):
        self.MessageNF = self.Message 
        MessageList = list()
        for j in range(self.NumberOfRotation):
            self.StartingLetterID = randint(0, 25)
            self.StartingLetter = ListOfKeys[self.StartingLetterID]
            self.StartID = Alphabet[self.StartingLetter]
            for i in self.MessageNF:
                self.LetterID = Alphabet[i]
                self.NewLetterIDNF = self.LetterID + self.StartID
                self.NewLetterIDNF2 = self.NewLetterIDNF - 26
                self.NewLetterID = ListOfValues[self.NewLetterIDNF2 - 1]
                self.NewLetterKey = ListOfKeys[self.NewLetterID - 1]
                self.NewLetter = self.NewLetterKey 
                MessageList.append(self.NewLetter)
                CodeKey.append(self.StartingLetterID)   #create a key to decode the message 
                self.StartingLetterID += 1 
            
            self.MessageF = "".join(MessageList)
            print(self.MessageF)
            self.MessageNF = self.MessageF 
            self.MessageF = None 
            self.MessageF = str()
            MessageList = None 
            MessageList = list()
        print(self.MessageF)