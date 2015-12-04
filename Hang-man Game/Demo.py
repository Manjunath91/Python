__author__ = 'Xerix'

from Game import Game
from GameOp import GameOp


class Demo:
    """ Main Method and calling here  """

    def main(self):
        obj = GameOp()
        obj.readFile()
        i = 0

        while i < obj.data.__sizeof__():

            print("Welcome to hangMan Game :D  \n1 - Play\n2 - Quit\n")
            playOption = raw_input("What to do ?")

            if (playOption == "p"):
                print("Now we working with Movies names : ")
                stop = 0
                testCase = Game()
                testCase.set_originalWord( str(obj.data[i]) )
                testCase.set_playWord( obj.stringHiding(testCase.originalWord))
                testCase.allUp()
                print(testCase.get_PlayWord())

                while True:
                    if (stop == -3  or stop == -10):
                        break
                    else:
                        char_test = raw_input("What is your Guess char : ")
                        stop = obj.game(char_test , testCase)
                        print "\n"

                if(stop == -3):
                    i += 1
                    print "Excellent  you are in Level : " + str(i) + " Keep Working after lvl 300 you get cup of milk tea :D "
                    print "\n\n\n\n\n\n"

            else:
                print "Okay  Bye :D "
                break
Test = Demo()
Test.main()