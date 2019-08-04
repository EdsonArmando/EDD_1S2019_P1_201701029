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
    def PopScore():
