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


rock = Rock("Rock")
paper = Paper("Paper")
print rock.compareTo(paper)
print paper.compareTo(rock)
print rock.compareTo(rock)

