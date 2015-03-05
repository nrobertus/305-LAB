from random import randint
import itertools

class Element:
    #A class for each element in the RPCLS Game
    _name='';
    def __init__(self, name):
        self._name = name
    def name(self):
        return self._name
    def compareTo(Element):
        raise NotImplementedError("Not yet implemented.")

class Rock(Element):
    def compareTo(self, Element):
        outputString = ""
        outcome = ""
        if(Element.name() == self.name()):
            outputString = self.name() + " equals " + self.name()
            outcome = "Tie"
        elif(Element.name() == "Scissors"):
            outputString = self.name() + " crushes " + Element.name()
            outcome = "Win"
        elif(Element.name() == "Lizard"):
            outputString = self.name() + " crushes " + Element.name()
            outcome = "Win"
        elif(Element.name() == "Paper"):
            outputString = Element.name() + " covers " + self.name()
            outcome = "Lose"
        elif(Element.name() == "Spock"):
            outputString = Element.name() +" vaporizes " + self.name()
            outcome = "Lose"
        return (outputString, outcome)


class Paper(Element):
    def compareTo(self, Element):
        outputString = ""
        outcome = ""
        if(Element.name() == self.name()):
            outputString = self.name() + " equals " + self.name()
            outcome = "Tie"
        elif(Element.name() == "Rock"):
            outputString = self.name() + " covers " + Element.name()
            outcome = "Win"
        elif(Element.name() == "Spock"):
            outputString = self.name() + " disproves " + Element.name()
            outcome = "Win"
        elif(Element.name() == "Scissors"):
            outputString = Element.name() + " cuts " + self.name()
            outcome = "Lose"
        elif(Element.name() == "Lizard"):
            outputString = Element.name() +" eats " + self.name()
            outcome = "Lose"
        return (outputString, outcome)

class Scissors(Element):
    def compareTo(self, Element):
        outputString = ""
        outcome = ""
        if(Element.name() == self.name()):
            outputString = self.name() + " equals " + self.name()
            outcome = "Tie"
        elif(Element.name() == "Paper"):
            outputString = self.name() + " cut " + Element.name()
            outcome = "Win"
        elif(Element.name() == "Lizard"):
            outputString = self.name() + " decapitate " + Element.name()
            outcome = "Win"
        elif(Element.name() == "Rock"):
            outputString = Element.name() + " crushes " + self.name()
            outcome = "Lose"
        elif(Element.name() == "Spock"):
            outputString = Element.name() +" smashes " + self.name()
            outcome = "Lose"
        return (outputString, outcome)

class Lizard(Element):
    def compareTo(self, Element):
        outputString = ""
        outcome = ""
        if(Element.name() == self.name()):
            outputString = self.name() + " equals " + self.name()
            outcome = "Tie"
        elif(Element.name() == "Spock"):
            outputString = self.name() + " poisons " + Element.name()
            outcome = "Win"
        elif(Element.name() == "Paper"):
            outputString = self.name() + " eats " + Element.name()
            outcome = "Win"
        elif(Element.name() == "Rock"):
            outputString = Element.name() + " crushes " + self.name()
            outcome = "Lose"
        elif(Element.name() == "Scissors"):
            outputString = Element.name() +" decapitate " + self.name()
            outcome = "Lose"
        return (outputString, outcome)

class Spock(Element):
    def compareTo(self, Element):
        outputString = ""
        outcome = ""
        if(Element.name() == self.name()):
            outputString = self.name() + " equals " + self.name()
            outcome = "Tie"
        elif(Element.name() == "Scissors"):
            outputString = self.name() + " smashes " + Element.name()
            outcome = "Win"
        elif(Element.name() == "Rock"):
            outputString = self.name() + " vaporizes " + Element.name()
            outcome = "Win"
        elif(Element.name() == "Paper"):
            outputString = Element.name() + " disproves " + self.name()
            outcome = "Lose"
        elif(Element.name() == "Lizard"):
            outputString = Element.name() +" poisons " + self.name()
            outcome = "Lose"
        return (outputString, outcome)

class Player:
    _name = ""
    _lastPlay = ""
    def __init__(self, name):
        self._name = name
    def name(self):
        return self._name
    def lastPlay(self):
        return self._lastPlay
    def setLastPlay(self, move):
        self._lastPlay = move
    def play(self):
        raise NotImplementedError("Not yet implemented")

class StupidBot(Player):
    def play(self):
        spock = Spock("Spock")
        self.setLastPlay(spock)
        return spock

class RandomBot(Player):
    def play(self):

        rand = randint(1, 5)
        if(rand == 1):
            move = Rock("Rock")
        elif(rand == 2):
            move = Paper("Paper")
        elif(rand == 3):
            move = Scissors("Scissors")
        elif(rand == 4):
            move = Lizard("Lizard")
        elif(rand == 5):
            move = Spock("Spock")
        self.setLastPlay(move)
        return move


class IterativeBot(Player):
    def cycles(iterable, repeat=1):
        for item in itertools.cycle(iterable):
            for _ in xrange(repeat):
                yield item

    c = cycles([0,1,2,3,4], 1)
    def play(self):
        rock = Rock("Rock")
        paper = Paper("Paper")
        spock = Spock("Spock")
        lizard = Lizard("Lizard")
        scissors = Scissors("Scissors")
        moves = [rock, paper, scissors, lizard, spock]
        return moves[self.c.next()]


class LastPlayBot(Player):
    def play(self, bot):
        opponentMove = bot.lastPlay()
        if(opponentMove == ""):
            random = RandomBot("Random Getter")
            opponentMove = random.play()
        return opponentMove

class Human(Player):
    def printUI(self):
        print "(1) : Rock"
        print "(2) : Paper"
        print "(3) : Scissors"
        print "(4) : Lizard"
        print "(5) : Spock"
    def play(self):
        rock = Rock("Rock")
        paper = Paper("Paper")
        spock = Spock("Spock")
        lizard = Lizard("Lizard")
        scissors = Scissors("Scissors")
        moves = [rock, paper, scissors, lizard, spock]
        self.printUI()
        selection = int(input("Enter your move: "))
        if((selection > 5)| (selection <1)):
            selection = input("Invalid move. Please try again: ")
        selection =(int) (selection - 1)
        return moves[selection]

class Main:
    #Instantiate players
    _stupidBot = StupidBot("Stupid Bot")
    _randomBot = RandomBot("Random Bot")
    _iterativeBot = IterativeBot("Iterative Bot")
    _lastPlayBot = LastPlayBot("Last Play Bot")
    _human = Human("Human")
    #set up the bots array
    bots = [_human, _stupidBot, _randomBot, _iterativeBot, _lastPlayBot]

    _input1 = ""
    _input2 = ""

    _player1 = ""
    _player2 = ""

    _rounds = 0

    _p1_score = 0
    _p2_score = 0

    def __init__(self, rounds):
        self._rounds = rounds
        print "Welcome to Rock, Paper, Scissors, Lizard, Spock, implemented by Nathan Robertus"

    def printUI(self):
        print "Please choose two players:"
        print "(1) : Human"
        print "(2) : StupidBot"
        print "(3) : RandomBot"
        print "(4) : IterativeBot"
        print "(5) : LastPlayBot"
    #getters and setters for the player selection variables
    def setInput1(self, input):
        self._input1 = input
    def setInput2(self, input):
        self._input2 = input
    def getInput1(self):
        return self._input1
    def getInput2(self):
        return self._input2
    #getters and setters for current player instances
    def setPlayer1(self, player):
        self._player1 = player
    def setPlayer2(self, player):
        self._player2 = player
    def getPlayer1(self):
        return self._player1
    def getPlayer2(self):
        return self._player2

    #getters and setters for scorekeeping
    def setP1Score(self, score):
        self._p1_score = score
    def setP2Score(self, score):
        self._p2_score=score
    def getP1Score(self):
        return self._p1_score
    def getP2Score(self):
        return self._p2_score

    #get the number of rounds
    def rounds(self):
        return self._rounds
    #main function
    def run(self):
        self.printUI()
        self.setInput1(int(input("Select player 1: ")))
        self.setInput2(int(input("Select player 2: ")))

        while(True):
            if((self.getInput1()>5)|(self.getInput1()<1)):
                self.setInput1(int(input("Invalid player 1 selection. Please try again: ")))
            else:
                self.setInput1(self.getInput1()-1)
                break
        while(True):
            if((self.getInput2()>5)|(self.getInput2()<1)):
                self.setInput2(int(input("Invalid player 2 selection. Please try again: ")))
            else:
                self.setInput2(self.getInput2()-1)
                break
        self.setPlayer1(self.bots[self.getInput1()])
        self.setPlayer2(self.bots[self.getInput2()])

        print self.getPlayer1().name() + " vs " + self.getPlayer2().name() +". Go!"
        for round in range(1, self.rounds()+1):
            if(self.getPlayer1().name() == "Last Play Bot"):
                element1 = self.getPlayer1().play(self.getPlayer1())
            else:
                element1 = self.getPlayer1().play()
            if(self.getPlayer2().name() == "Last Play Bot"):
                element2 = self.getPlayer2().play(self.getPlayer1())
            else:
                element2 = self.getPlayer2().play()
            print "Round " + str(round) + ":"
            print "  Player 1 chose " + element1.name()
            print "  Player 2 chose " + element2.name()
            results = element1.compareTo(element2)
            print "  " + results[0]
            if(results[1] == "Win"):
                print "  Player 1 won the round\n"
                self.setP1Score(self.getP1Score()+1)
            elif(results[1] == "Lose"):
                print "  Player 2 won the round\n"
                self.setP2Score(self.getP2Score()+1)
            else:
                print "  Round was a tie\n"

        print "The score was " + str(self.getP1Score()) + " to " + str(self.getP2Score()) + "."
        if(self.getP1Score()>self.getP2Score()):
            print self.getPlayer1().name() + " won the game."
        elif(self.getP1Score()<self.getP2Score()):
            print self.getPlayer2().name() + " won the game."
        else:
            print "Game was a draw."




main = Main(5)
main.run()

