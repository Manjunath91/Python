__author__ = 'Xerix'


class Game:
    """ Game String and op    """

    numGuess = 6
    numRightGuess = 0
    wrongGuess = []
    rightGuess = []
    originalWord = ""
    playWord = ""

    def __init__(self):
        self.numGuess = 6
        self.numRightGuess = 0
        self.wrongGuess = ""
        self.rightGuess = ""
        self.originalWord = ""
        self.playWord = ""

    def Game(self  , numR , wrongGuess , rightGuess , originalGuess , playWord):
        self.numGuess = 6
        self.numRightGuess = numR
        self.wrongGuess = wrongGuess
        self.rightGuess = rightGuess
        self.originalWord = originalGuess
        self.playWord = playWord

    def allUp(self):
        self.wrongGuess = str(self.wrongGuess).upper()
        self.rightGuess = str(self.rightGuess).upper()
        self.originalWord = str(self.originalWord).upper()

    def reconstract(self , string): # take shape in example decoration
        temp = list(string)
        sum = ""
        for x in temp:
            sum += " "+x
        sum = sum.replace("  ", "   ")
        return  sum

    def set_char_playWord(self , index , ch):
        arrWord = list(self.playWord)
        arrWord[index] = ch  # multiplay by 2 becasue adding spaces btw each _ and add 2 because 2 spaces in middle
        self.playWord  = "".join(arrWord)


    def set_originalWord(self , value):
        self.originalWord = value


    def get_originalWord(self):
        return self.originalWord



    def set_wrongGuess(self , value):
        self.wrongGuess = value


    def get_wrongGuess(self):
        return self.wrongGuess


    

    def set_rightGuess(self , value):
        self.rightGuess = value



    def get_rightGuess(self):
        return self.rightGuess



    def set_numRightGuess(self , value):
        self.numRightGuess = value


    def get_numRightGuess(self):
        return self.numRightGuess



    def set_numGuess(self , value):
        self.numGuess = value


    def get_numGuess(self):
        return self.numGuess


    def set_playWord(self , value):
        self.playWord = value


    def get_PlayWord(self):
        return self.reconstract(self.playWord)