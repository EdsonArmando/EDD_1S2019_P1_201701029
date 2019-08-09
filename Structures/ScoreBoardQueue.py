class ScoreBoardNode:
    def __init__(self,name,points):
        self.name = name
        self.points = points
        self.next = None

class ScoreBoard_Queue:
    def __init__(self):
        self.first=None
        self.last=None
    def isEmpty(self):
        if self.first is None:
            return True
        else:
            return False

    def ScoreEnqueue(self,name,points):
        new = ScoreBoardNode(name,points)
        if self.first is None:
            self.first = new
            self.last = new
        else:
            self.last.next = new
            self.last = new

    def ScoreDequeue(self):
        if self.first == self.last:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next
    def printValue(self):
        aux = self.first
        while aux !=None:
            print(aux.name, aux.points)
            aux = aux.next
