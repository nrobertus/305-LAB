from random import randint
import itertools
import pygame
import sys

# Initialize GUI systems
pygame.init()
size = width, height = 600, 600
speed = [2, 2]
black = 0, 20, 40
screen = pygame.display.set_mode(size)
background = pygame.image.load("selection_default.png")

# Pre-load the image files for the human player
default_back = pygame.image.load("RPSLS.png")
spock_back = pygame.image.load("spock.png")
paper_back = pygame.image.load("paper.png")
lizard_back = pygame.image.load("lizard.png")
rock_back = pygame.image.load("rock.png")
scissors_back = pygame.image.load("scissors.png")

# Pre-Load the images for the player selection
selection_back = pygame.image.load("selection_default.png")
human_back = pygame.image.load("selection_human.png")
stupid_back = pygame.image.load("selection_stupid.png")
random_back = pygame.image.load("selection_random.png")
iterative_back = pygame.image.load("selection_iterative.png")
lastPlay_back = pygame.image.load("selection_lastPlay.png")
my_back = pygame.image.load("selection_my.png")

# Other assorted necessary properties for the GUI generation
_player1 = ""
_player2 = ""
backrect = background.get_rect()
renderString = "Rock, Paper, Scissors, Lizard, Spock"
font=pygame.font.Font(None,30)


# coordinates: spock: (111, 259), scissors: (292, 117), paper: (488, 252), rock: (419, 475), lizard: (180, 484)
# threshold: 90 px each way
thresh = 90
spock_pos = [111, 259]
scissors_pos = [292, 117]
paper_pos = [488, 252]
rock_pos = [419, 475]
lizard_pos = [180, 484]

# coordinates: human: (177, 117), stupid: (), random: (), iterative: (), last play: (), my bot ()
# threshold: (136, 24)
thresh_x = 136
thresh_y = 24
human_pos = [177, 117]
stupid_pos = [177, 176]
random_pos = [177, 235]
iterative_pos = [177, 294]
lastPlay_pos = [177, 353]
my_pos = [177, 412]

############################################
##  PLAYER AND ELEMENT CLASS SYSTEM
############################################

'''Base class for elements'''
class Element:
    #A class for each element in the RPCLS Game
    _name='';
    def __init__(self, name):
        self._name = name
    def name(self):
        return self._name
    def compareTo(Element):
        raise NotImplementedError("Not yet implemented.")

'''Rock class and logic -- Extends Element'''
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

'''Paper class and logic -- Extends Element'''
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

'''Scissors class and logic -- Extends Element'''
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

'''Lizard class and logic -- Extends Element'''
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

'''Spock class and logic -- Extends Element'''
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

'''Base class for players'''
class Player:
    _name = ""
    _lastPlay = Lizard("Lizard")
    def __init__(self, name):
        self._name = name
    def name(self):
        return self._name
    def lastPlay(self):
        return self._lastPlay
    def setLastPlay(self, move):
        self._lastPlay = move

    def play(self, bot):
        raise NotImplementedError("Not yet implemented")

'''StupidBot class and logic -- Extends Player'''
class StupidBot(Player):
    def play(self, bot):
        spock = Spock("Spock")
        self.setLastPlay(spock)
        return spock

'''RandomBot class and logic -- Extends Player'''
class RandomBot(Player):
    def play(self, bot):

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

'''IterativeBot class and logic -- Extends Player'''
class IterativeBot(Player):
    def cycles(iterable, repeat=1):
        for item in itertools.cycle(iterable):
            for _ in xrange(repeat):
                yield item

    c = cycles([0,1,2,3,4], 1)
    def play(self, bot):
        rock = Rock("Rock")
        paper = Paper("Paper")
        spock = Spock("Spock")
        lizard = Lizard("Lizard")
        scissors = Scissors("Scissors")
        moves = [rock, paper, scissors, lizard, spock]

        move = moves[self.c.next()]
        self.setLastPlay(move)
        return move

'''LastPlayBot class and logic -- Extends Player'''
class LastPlayBot(Player):
    def play(self, bot):
        opponentMove = bot.lastPlay()
        return opponentMove

'''Human class and User Interface -- Extends Player'''
class Human(Player):
    def printUI(self):
        print "(1) : Rock"
        print "(2) : Paper"
        print "(3) : Scissors"
        print "(4) : Lizard"
        print "(5) : Spock"
    def GUI_GetPlay(self, x, y):
        if (x > (spock_pos[0] - thresh)) and (x < (spock_pos[0] + thresh)) and (y > (spock_pos[1]-thresh)) and (y < (spock_pos[1]+thresh)):
            return "spock"
        elif (x > (lizard_pos[0] - thresh)) and (x < (lizard_pos[0] + thresh)) and (y > (lizard_pos[1]-thresh)) and (y < (lizard_pos[1]+thresh)):
            return "lizard"
        elif (x > (paper_pos[0] - thresh)) and (x < (paper_pos[0] + thresh)) and (y > (paper_pos[1]-thresh)) and (y < (paper_pos[1]+thresh)):
            return "paper"
        elif (x > (rock_pos[0] - thresh)) and (x < (rock_pos[0] + thresh)) and (y > (rock_pos[1]-thresh)) and (y < (rock_pos[1]+thresh)):
            return "rock"
        elif (x > (scissors_pos[0] - thresh)) and (x < (scissors_pos[0] + thresh)) and (y > (scissors_pos[1]-thresh)) and (y < (scissors_pos[1]+thresh)):
            return "scissors"
        else:
            return "none"
    def play(self, bot):
        rock = Rock("Rock")
        paper = Paper("Paper")
        spock = Spock("Spock")
        lizard = Lizard("Lizard")
        scissors = Scissors("Scissors")
        moves = [rock, paper, scissors, lizard, spock]
        selection = 0
        noInput = True
        while noInput:
            for event in pygame.event.get():
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                play = self.GUI_GetPlay(mouse_x, mouse_y)
                if(play == "rock"):
                    background = rock_back
                elif(play=="paper"):
                    background = paper_back
                elif(play=="scissors"):
                    background=scissors_back
                elif(play == "lizard"):
                    background=lizard_back
                elif(play == "spock"):
                    background=spock_back
                else:
                    background=default_back
                if backrect.left < 0 or backrect.right > width:
                    speed[0] = -speed[0]
                if backrect.top < 0 or backrect.bottom > height:
                    speed[1] = -speed[1]
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    x_pos = pos[0]
                    y_pos = pos[1]
                    play =  self.GUI_GetPlay(x_pos, y_pos)
                    if play == "rock":
                        selection = 0
                        noInput = False
                    elif play == "paper":
                        selection = 1
                        noInput = False
                    elif play == "scissors":
                        selection = 2
                        noInput = False
                    elif play == "lizard":
                        selection = 3
                        noInput = False
                    elif play == "spock":
                        selection = 4
                        noInput = False
                    elif play == "none":
                        selection = -1
                if event.type == pygame.QUIT:
                    sys.exit()
                screen.fill(black)
                screen.blit(background, backrect)
                title=font.render(renderString,1,(255,255,255))
                player1_text = font.render("Player 1: "+_player1, 1, (255, 255, 255))
                player2_text = font.render("Player 2: "+_player2, 1, (255, 255, 255))
                screen.blit(player1_text, (5, 575))
                screen.blit(player2_text, (305, 575))
                screen.blit(title, (110, 5))
                pygame.display.flip()

        self.printUI()
        #selection = int(input("Enter your move: "))
        #if((selection > 5)| (selection <1)):
        #    selection = input("Invalid move. Please try again: ")
        #selection =(int) (selection - 1)
        print "exited"
        self.setLastPlay((moves[selection]))
        return moves[selection]

'''MyBot class and logic -- Extends Player'''
class MyBot(Player):
    _move = ""
    def setMove(self, move):
        self._move = move
    def getMove(self):
        return self._move

    def play(self, bot):

        rand = randint(1, 100)
        if((rand % 2)==0 ):
            self.setMove(bot.lastPlay())
        else:
            self.setMove(self.lastPlay())
        self.setLastPlay(self.getMove())
        return self.getMove()


'''Main class and game control'''
class Main:
    #Instantiate players
    _stupidBot = StupidBot("Stupid Bot")
    _randomBot = RandomBot("Random Bot")
    _iterativeBot = IterativeBot("Iterative Bot")
    _lastPlayBot = LastPlayBot("Last Play Bot")
    _human = Human("Human")
    _myBot = MyBot("My Bot")
    #set up the bots array
    bots = [_human, _stupidBot, _randomBot, _iterativeBot, _lastPlayBot, _myBot]

    _input1 = ""
    _input2 = ""

    _player1 = ""
    _player2 = ""

    _rounds = 0

    _p1_score = 0
    _p2_score = 0

    _currentState = "userInput"

    def __init__(self, rounds):
        self._rounds = rounds
        print "Welcome to Rock, Paper, Scissors, Lizard, Spock, implemented by Nathan Robertus"

    def getCurrentState(self):
        return self._currentState

    def setCurrentState(self, state):
        self._currentState = state

    def printUI(self):
        print "Please choose two players:"
        print "(1) : Human"
        print "(2) : StupidBot"
        print "(3) : RandomBot"
        print "(4) : IterativeBot"
        print "(5) : LastPlayBot"
        print "(6) : MyBot"
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

    def GUI_get_player_selection(self, x, y):
        if (x > (human_pos[0] - thresh_x)) and (x < (human_pos[0] + thresh_x)) and (y > (human_pos[1]-thresh_y)) and (y < (human_pos[1]+thresh_y)):
            return "human"
        elif (x > (stupid_pos[0] - thresh_x)) and (x < (stupid_pos[0] + thresh_x)) and (y > (stupid_pos[1]-thresh_y)) and (y < (stupid_pos[1]+thresh_y)):
            return "stupid"
        elif (x > (random_pos[0] - thresh_x)) and (x < (random_pos[0] + thresh_x)) and (y > (random_pos[1]-thresh_y)) and (y < (random_pos[1]+thresh_y)):
            return "random"
        elif (x > (iterative_pos[0] - thresh_x)) and (x < (iterative_pos[0] + thresh_x)) and (y > (iterative_pos[1]-thresh_y)) and (y < (iterative_pos[1]+thresh_y)):
            return "iterative"
        elif (x > (lastPlay_pos[0] - thresh_x)) and (x < (lastPlay_pos[0] + thresh_x)) and (y > (lastPlay_pos[1]-thresh_y)) and (y < (lastPlay_pos[1]+thresh_y)):
            return "lastPlay"
        elif (x > (my_pos[0] - thresh_x)) and (x < (my_pos[0] + thresh_x)) and (y > (my_pos[1]-thresh_y)) and (y < (my_pos[1]+thresh_y)):
            return "my"
        else:
            return "none"

    #main function
    def run(self):
        self.printUI()
        self.setCurrentState("userInput")
        player1_selection = ""
        player2_selection = ""
        noPlayers = True
        while(noPlayers):
            while self.getCurrentState() == "userInput":
                for event in pygame.event.get():
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]

                    player = self.GUI_get_player_selection(mouse_x, mouse_y)
                    if player == "human":
                        background = human_back
                    elif player == "stupid":
                        background = stupid_back
                    elif player == "random":
                        background = random_back
                    elif player == "iterative":
                        background = iterative_back
                    elif player == "lastPlay":
                        background = lastPlay_back
                    elif player == "my":
                        background = my_back
                    else:
                        background = selection_back
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        x_pos = pos[0]
                        y_pos = pos[1]
                        player = self.GUI_get_player_selection(x_pos, y_pos)
                        if(player1_selection == ""):
                            if player == "human":
                                player1_selection = "Human"
                                self.setPlayer1(self.bots[0])
                            elif player == "stupid":
                                player1_selection = "Stupid Bot"
                                self.setPlayer1(self.bots[1])
                            elif player == "random":
                                player1_selection = "Random Bot"
                                self.setPlayer1(self.bots[2])
                            elif player == "iterative":
                                player1_selection = "Iterative Bot"
                                self.setPlayer1(self.bots[3])
                            elif player == "lastPlay":
                                player1_selection = "Last Play Bot"
                                self.setPlayer1(self.bots[4])
                            elif player == "my":
                                player1_selection = "My Bot"
                                self.setPlayer1(self.bots[5])
                            else:
                                player1_selection = ""
                        elif(player2_selection == ""):
                            if player == "human":
                                player2_selection = "Human"
                                self.setPlayer2(self.bots[0])
                                noPlayers = False
                                self.setCurrentState("")
                            elif player == "stupid":
                                player2_selection = "Stupid Bot"
                                self.setPlayer2(self.bots[1])
                                noPlayers = False
                                self.setCurrentState("")
                            elif player == "random":
                                player2_selection = "Random Bot"
                                self.setPlayer2(self.bots[2])
                                noPlayers = False
                                self.setCurrentState("")
                            elif player == "iterative":
                                player2_selection = "Iterative Bot"
                                self.setPlayer2(self.bots[3])
                                noPlayers = False
                                self.setCurrentState("")
                            elif player == "lastPlay":
                                player2_selection = "Last Play Bot"
                                self.setPlayer2(self.bots[4])
                                noPlayers = False
                                self.setCurrentState("")
                            elif player == "my":
                                player2_selection = "My Bot"
                                self.setPlayer2(self.bots[5])
                                noPlayers = False
                                self.setCurrentState("")
                            else:
                                player2_selection = ""
                    screen.fill(black)
                    screen.blit(background, backrect)

                    player1_text = font.render("Player 1: "+player1_selection, 1, (255, 255, 255))
                    player2_text = font.render("Player 2: "+player2_selection, 1, (255, 255, 255))
                    screen.blit(player1_text, (5, 575))
                    screen.blit(player2_text, (305, 575))
                    pygame.display.flip()
            while self.getCurrentState() == "postGame":
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        sys.exit()

        print self.getPlayer1().name() + " vs " + self.getPlayer2().name() +". Go!"
        for round in range(1, self.rounds()+1):
            element1 = self.getPlayer1().play(self.getPlayer2())
            element2 = self.getPlayer2().play(self.getPlayer1())
            print "Round " + str(round) + ":"
            print "  " + self.getPlayer1().name() + " chose " + element1.name()
            print "  " + self.getPlayer2().name() + " chose " + element2.name()
            results = element1.compareTo(element2)
            print "  " + results[0]
            if(results[1] == "Win"):
                print "  " + self.getPlayer1().name() + " won the round\n"
                self.setP1Score(self.getP1Score()+1)
            elif(results[1] == "Lose"):
                print "  " + self.getPlayer2().name() + " won the round\n"
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
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                screen.fill(black)
                winner_text_string = ""
                if(self.getP1Score()>self.getP2Score()):
                    winner_text_string = "Player 1 won the game."
                elif(self.getP1Score()<self.getP2Score()):
                    winner_text_string = "Player 2 won the game."
                else:
                    winner_text_string = "The game was a tie."
                #screen.blit(background, backrect)
                player1_text = font.render("Player 1: "+player1_selection + " (" + str(self.getP1Score()) + ")", 1, (255, 255, 255))
                player2_text = font.render("Player 2: "+player2_selection+ " (" + str(self.getP2Score()) + ")", 1, (255, 255, 255))
                winner_text = font.render(winner_text_string, 1, (255, 255, 255))
                screen.blit(winner_text, (150, 300))
                screen.blit(player1_text, (5, 575))
                screen.blit(player2_text, (305, 575))
                pygame.display.flip()


main = Main(5) # Set up main class and decide on five rounds
main.run() # Execute the main function to prompt user for input, execute matches, and print results