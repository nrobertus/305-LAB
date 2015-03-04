class Element:
    #A class for each element in the RPCLS Game
    _name='';
    def __init__(self, name):
        self._name = name
    def name():
        return _name
    def compareTo(Element):
        raise NotImplementedError("Not yet implemented.")

class Rock(Element):
    def __init__(self, name="Rock"):
        self._name = name
    def compareTo(self, Element):
        outputString = ""
        outcome = ""
        if(Element._name == self._name):
            outputString = self._name + " equals " + self._name
            outcome = "Tie"
        elif(Element._name == "Scissors"):
            outputString = self._name + " crushes " + Element._name
            outcome = "Win"
        elif(Element._name == "Lizard"):
            outputString = self._name + " crushes " + Element._name
            outcome = "Win"
        elif(Element._name == "Paper"):
            outputString = Element._name + " covers " + self._name
            outcome = "Lose"
        elif(Element._name == "Spock"):
            outputString = Element._name +" vaporizes " + self._name
            outcome = "Lose"
        return (outputString, outcome)


class Paper(Element):
    def __init__(self, name="Paper"):
        self._name = name
    def compareTo(self, Element):
        outputString = ""
        outcome = ""
        if(Element._name == self._name):
            outputString = self._name + " equals " + self._name
            outcome = "Tie"
        elif(Element._name == "Rock"):
            outputString = self._name + " covers " + Element._name
            outcome = "Win"
        elif(Element._name == "Spock"):
            outputString = self._name + " disproves " + Element._name
            outcome = "Win"
        elif(Element._name == "Scissors"):
            outputString = Element._name + " cuts " + self._name
            outcome = "Lose"
        elif(Element._name == "Lizard"):
            outputString = Element._name +" eats " + self._name
            outcome = "Lose"
        return (outputString, outcome)

class Scissors(Element):
    def __init__(self, name="Scissors"):
        self._name= name
    def compareTo(self, Element):
        outputString = ""
        outcome = ""
        if(Element._name == self._name):
            outputString = self._name + " equals " + self._name
            outcome = "Tie"
        elif(Element._name == "Paper"):
            outputString = self._name + " cut " + Element._name
            outcome = "Win"
        elif(Element._name == "Lizard"):
            outputString = self._name + " decapitate " + Element._name
            outcome = "Win"
        elif(Element._name == "Rock"):
            outputString = Element._name + " crushes " + self._name
            outcome = "Lose"
        elif(Element._name == "Spock"):
            outputString = Element._name +" smashes " + self._name
            outcome = "Lose"
        return (outputString, outcome)

class Lizard(Element):
    def __init__(self, name="Lizard"):
        self._name=name
    def compareTo(self, Element):
        outputString = ""
        outcome = ""
        if(Element._name == self._name):
            outputString = self._name + " equals " + self._name
            outcome = "Tie"
        elif(Element._name == "Spock"):
            outputString = self._name + " poisons " + Element._name
            outcome = "Win"
        elif(Element._name == "Paper"):
            outputString = self._name + " eats " + Element._name
            outcome = "Win"
        elif(Element._name == "Rock"):
            outputString = Element._name + " crushes " + self._name
            outcome = "Lose"
        elif(Element._name == "Scissors"):
            outputString = Element._name +" decapitate " + self._name
            outcome = "Lose"
        return (outputString, outcome)

class Spock(Element):
    def compareTo(self, Element):
        outputString = ""
        outcome = ""
        if(Element._name == self._name):
            outputString = self._name + " equals " + self._name
            outcome = "Tie"
        elif(Element._name == "Scissors"):
            outputString = self._name + " smashes " + Element._name
            outcome = "Win"
        elif(Element._name == "Rock"):
            outputString = self._name + " vaporizes " + Element._name
            outcome = "Win"
        elif(Element._name == "Paper"):
            outputString = Element._name + " disproves " + self._name
            outcome = "Lose"
        elif(Element._name == "Lizard"):
            outputString = Element._name +" poisons " + self._name
            outcome = "Lose"
        return (outputString, outcome)


rock = Rock("Rock")
paper = Paper("Paper")
print rock.compareTo(paper)
print paper.compareTo(rock)
print rock.compareTo(rock)

