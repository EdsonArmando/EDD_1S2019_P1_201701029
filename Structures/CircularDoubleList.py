class NodeUser:
    def __init__(self,name):
        self.name=name
        self.next = None
        self.prev = None

class Circular_Double_List:
    def __init__(self):
        self.first=None
        self.last=None
        self.size=0

    def addUser(self,name):
        nuevo = NodeUser(name)
        if self.first is None:
            self.first=nuevo
            self.first.next=self.first
            nuevo.prev=self.last
            self.last=nuevo
        else:
            self.last.next=nuevo
            nuevo.next=self.first
            nuevo.prev=self.last
            self.last=nuevo
            self.first.prev=self.last
        self.size+=1

    def printUser(self):
        aux = self.first
        while True:
            print(aux.name)
            aux = aux.next
            if self.first.name == aux.name:
                break
list2=Circular_Double_List()
list2.addUser("Edson")
list2.addUser("Juan")
list2.addUser("Lucia")
list2.printUser()
