__author__ = 'Xerix'


class GameOp:
    """  game operation  """

    data = []  #all films  names to work on

    def readFile(self):
        """  Reading file and put each string in to element 'Game try'  """
        rFile  =  open('C:/Users/Xerix/PycharmProjects/Ass1/Movies.txt' , 'r')
        x = rFile.readline()

        while x != "" :
            originalWord = x.upper()
            self.data.append(originalWord)
            x = rFile.readline()

        rFile.close()

    def stringHiding(self, value):
        """covert string to _ """
        string_replace ="ABCDEFGHIJKLMNOPQRSTUVXWYZ0123456789"
        string_replace = list(string_replace)

        for ch in string_replace:
           if ch in value:
             value = value.replace(ch, "_")

        return value

    def find(self , s, ch):
        """ enumerate (data type )  get index of element ,  i for i  while true go from range
        which can be 0  kol mara by5od el output men el ennum el hwa index of char if == ch"""
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def game(self , ch_test  , testCase ):
        """ this is main operation of the hangman game """
        # check if ch exist in word

        if (len(ch_test) > 1 or not ch_test.isalnum()): # num or alphabet
            print "please try again Not valid Character "
            return -2

        ch_test = ch_test.upper()   # check char function
        numOfChar = testCase.originalWord.count(ch_test)

        if ( numOfChar > 0):
            red = self.checkRedundancy(testCase , ch_test)

            if (red == -1):  # not duplicate char
                return -1   # error duplacate
            else:
                indexChar = self.find( testCase.get_originalWord() , ch_test)
                testCase.set_rightGuess(testCase.get_rightGuess() + (" "+ch_test)) # adding to right char

                for x in indexChar:
                    testCase.set_char_playWord( int(x) , testCase.get_originalWord()[x])

                testCase.set_numRightGuess(testCase.get_numRightGuess() + 1)   # adding to check winning

                print("You are right there are : "+ str(len(indexChar)) + " "+ ch_test)
                print("you get till now { " + testCase.get_rightGuess() +" }")
                print testCase.get_PlayWord()

                lindex = self.checkWinning(testCase)
                if(lindex == -3):
                    return  -3
                return -4 # success adding

        else:
            red = self.checkRedundancy(testCase, ch_test)
            if (red == -1):  # not duplicate char
                return -1  # error duplacate

            testCase.set_numGuess(testCase.get_numGuess() - 1)
            print("not found :P try again you still have : " + str(testCase.get_numGuess()) + " times")
            testCase.set_wrongGuess(testCase.get_wrongGuess() + (" "+ch_test))
            print("you get till now {" + testCase.get_wrongGuess() +"}")
            print testCase.get_PlayWord()
            lindex = self.checkLosing(testCase)
            if( lindex == -10):
                return -10
            return -5  # fail to add

    def checkRedundancy(self , testCase , ch_test):
            r_list = testCase.get_rightGuess().count(ch_test)
            l_list = testCase.get_wrongGuess().count(ch_test)

            if (r_list > 0 or l_list > 0):  # not duplicate char
                print("This char has been called before : \n" + testCase.get_PlayWord() + "\n")
                return -1   # error duplacate

    def checkWinning(self , testCase):

        temp1 = ''.join(set(testCase.get_originalWord()))
        spe =  sum(not c.isalnum() for c in temp1)
        if len(temp1) - spe  == testCase.get_numRightGuess(): #one for space and one for /n
            print("\nWOW you WIN :D Nice ")
            return -3 # winning

    def checkLosing(self , testCase):
        print HANGMANPICS[ 6 - testCase.get_numGuess()]
        if(testCase.get_numGuess() == 0):
            print "\nSorry :( you lost\n" + "The film was : " + testCase.get_originalWord()
            return -10  # losing
        # check if char have been chosen before
        # adding char to on of lists right or wrong
        # send back feedback and score


# -10 loosing   , -3 winning , -5 fail to add , -4 success to add  , -1 duplicate  , -2 not valid


HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
