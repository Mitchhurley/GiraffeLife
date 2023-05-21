
import random
import os
from time import sleep

# Concept: Giraffe game that prints an ascii giraffe and gives options for how time is spent
# you have x time, (figure out how long giraffes take to mature) after which if you have not mated you lose the game
# if you have mated then it goes again with better stats
# for actions, have a 'look for food', 'fight for social power' and 'look for mate'
# look for food will be necessary to not die, and will up a fitness stat
# fight for social power will give a result based on fitness, and will up a 'clout' variable
# mate quality is based on 'clout' and 'fitness', and will create an offspring giraffe with better stats
# based on mate quality, held in an array
# random events will occur, and there is a roll for them after every day


class Giraffe:

    def __init__(self, nl):
        self.neckLength = int(nl) #random.randrange
        self.fightingPower = self.neckLength
        self.daysLeft = 10 #TODO determine this from a parameter
        self.bestMate = 0

    def printGiraffe(self):
        print(' .-", \n `~||')
        #add in thing that shortens neck
        for i in range(self.neckLength):
            print("   ||")
        print("   ||___" + "\t Days Left:" + "[]" * self.daysLeft)
        print("   (':.)`" + "\tEvaluation: You are a " + self.calcClout())
        if self.bestMate < 1:
            print("   || ||")
        elif self.bestMate >= 1:
            print("   || ||\tYou have made an offspring")
        print("   || ||")
        print("   ^^ ^^")

    def calcClout(self):
        if self.neckLength + self.fightingPower < 4:
            return "Weak little giraffe"

        if self.neckLength + self.fightingPower < 8:
            return "Weak giraffe"

        if self.neckLength + self.fightingPower < 12:
            return "Passable giraffe"

        if self.neckLength + self.fightingPower < 16:
            return "Impressive giraffe"

        if self.neckLength + self.fightingPower < 20:
            return "Alpha giraffe"

        if self.neckLength + self.fightingPower < 30:
            return "Transcendent giraffe! congratulations you win"

    def lookForfood(self):
        # determines what happens, affected by environmental factors determined in newDay() method
        luck = random.randint(0, 100)
        #print("Your luck is " + luck)
        # if you get a 0, 1 or 2, you get eaten by lions
        if luck < 3:
            print("Unlucky! You were torn apart by lions :)")
            self.youLose()

        # if you get a 3 or 4, you get shot by confused poachers who thought you were an elephant
        if luck < 5:
            print("Unlucky! You were shot by nearsighted poachers who thought you were an elephant :)")
            self.youLose()

        # if you get 5-10, you couldn't find any food
        if luck < 11:
            print("Unlucky! You couldnt find any food")
            self.neckLength -= 1
            input("Press enter to continue")
            return
        # 11-20 is slim pickings
        if luck < 21:
            print("You found a little food, but not much")
            input("Press enter to continue")
            return
        # 21-80 is good eats
        if luck < 81:
            print("You found enough food")
            input("Press enter to continue")
            self.neckLength += 1
            return
        # 81-90 is bountiful harvest
        if luck < 91:
            print("Lucky! You found a lot of food!")
            self.neckLength += 2
            input("Press enter to continue")
            return
        # 91-95 is you find a crazy amount of food, super buff
        if luck < 96:
            print("Lucky! You found a crazy whole lot of food!")
            self.neckLength += 3
            input("Press enter to continue")
            return
        # 96 - 100 gets you a free offspring plus lots of food
        if luck < 101:
            print("Lucky! You found a crazy whole lot of food, and a giraffe you want to mate!")
            self.neckLength += 3
            self.offspring(self.neckLength)
            input("Press enter to continue")
            return
        else: print("Error: luck value of " + luck)
    def findMate(self):
        #finds mate quality based on fitness and clout, plus luck factor
        luck = random.randint(0, 10)

        if luck == 0:
            print("Unlucky, no mate")

            return
        if luck < 3:
            self.offspring(self.neckLength - 2)
            print("Unlucky, mediocre mate")
            return
        if luck < 8:
            self.offspring(self.neckLength)
            print("Your mating was fruitful and created an offspring!")
            return
        if luck < 10:
            self.offspring(self.neckLength + 1)
            print("Your mating was very fruitful and created an healthy offspring!")
            return

        if luck == 10:
            self.offspring(self.neckLength + 2)
            print("Your mating was bountiful and created an exceptional offspring!")
            return
        # if 3-7, mate based only on fitness and clout
        # if 8 or 9, mate with a higher quality giraffe
        # if 10, same as above but two offspring

    def fightForClout(self):
        luck = random.randint(0, 10)
        if self.neckLength + self.fightingPower + luck < 4:
            print("You were hurt badly and ended up succumbing to your wounds. Game Over")
            self.youLose()
        if self.neckLength + self.fightingPower + luck < 10:
            print("You were badly beaten and retreated. You feel weaker")
            self.fightingPower -= 1
            return
        if self.neckLength + self.fightingPower + luck < 16:
            print("You show out and impress many potential mates. Well done")
            self.fightingPower += 1
        else:
            print("You demonstrate yourself as the alpha, and the other giraffes respect (and fear) you.")
            self.fightingPower += 2




    def chooseAction(self):
        #print the options
        print("How do you want to Spend your time")
        choice = int(input("1 to look for food \n2 to fight other bull giraffes \n3 to look for a mate\n"))
        if choice == 1:
            self.lookForfood()
        if choice == 2:
            self.fightForClout()
            input("Press enter to continue")
        if choice == 3:
            self.findMate()
            input("Press enter to continue")

    def playDay(self):
        os.system(' ')
        self.printGiraffe()
        if self.daysLeft <= 0:
            #make offspring and start a new game
            print("Well, you got old and died. If you want, you can play again with your offspring")
            self.youLose()
        else:
            self.daysLeft -= 1
            self.chooseAction()
            self.playDay()

    def youLose(self):
        print("Thanks for Playing! If you want to, you can press 1 to end the game, or press anything else to play again with your offsping (if you have one)")
        if (input('?') == '1' or self.bestMate == 0): exit(0)
        else:
            baby = self.bestMate/2
            nextOne = Giraffe(baby)
            nextOne.playDay()


    def offspring(self, quality):
        self.bestMate = max(self.bestMate, quality)






def printTitle():
    print("░██████╗░██╗██████╗░░█████╗░███████╗███████╗███████╗        ██╗░░░░░██╗███████╗███████╗" +
    "\n██╔════╝░██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝        ██║░░░░░██║██╔════╝██╔════╝" +
    "\n██║░░██╗░██║██████╔╝███████║█████╗░░█████╗░░█████╗░░        ██║░░░░░██║█████╗░░█████╗░░" +
    "\n██║░░╚██╗██║██╔══██╗██╔══██║██╔══╝░░██╔══╝░░██╔══╝░░        ██║░░░░░██║██╔══╝░░██╔══╝░░" +
    "\n╚██████╔╝██║██║░░██║██║░░██║██║░░░░░██║░░░░░███████╗        ███████╗██║██║░░░░░███████╗" +
    "\n░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝        ╚══════╝╚═╝╚═╝░░░░░╚══════╝")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    printTitle()
    temp = min(int(input("\nHow long is Your Neck? a length of 2 is suggested\n")), 4)
    g1 = Giraffe(temp)
    g1.playDay()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

