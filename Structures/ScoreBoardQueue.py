import os
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
    def GenerateImage(self):
        texto = 'digraph {\n rankdir=LR; \n node [shape=record]; \n label="Cajas de Pago";\nnull [label="NULL" shape=box];\n'
        datesSocre=""
        aux = self.first
        cont=0
        while aux !=None:
            datesSocre+= str(cont)+'[label="{<data> '+'('+aux.name+','+str(aux.points)+')'+ '| <ref>  }", width=1.2]\n'
            datesSocre+= str(cont)+':ref:c'+'->' +str(cont+1)+':data'
            cont+=1
            aux = aux.next
        with open("ScoreBoard.txt",'w',encoding = 'utf-8') as f:
            f.write(texto+str(cont)+':ref:c -> null\n}'+datesSocre)
            f.close()


    def printValue(self):
        aux = self.first
        while aux !=None:
            print(aux.name, aux.points)
            aux = aux.next
