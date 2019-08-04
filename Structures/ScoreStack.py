class NodeScore:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.next=None
class Score_Stack:
    def __init__(self):
        self.first=None

    def PushScore(self,x,y):
        new = NodeScore(x,y)
        if self.first is None:
            self.first=new
        else:
            new.next=self.first
            self.first=new
    def PopScore(self):
        x=0
        y=0
        x = self.first.x
        y = self.first.y
        self.first=self.first.next
    def printStack(self):
        aux = self.first
        while aux !=None:
            print(aux.x,aux.y)
            aux = aux.next
stack1=Score_Stack()
stack1.PushScore(4,5)
stack1.PushScore(7,3)
stack1.PushScore(2,5)
stack1.PopScore()
stack1.printStack()
