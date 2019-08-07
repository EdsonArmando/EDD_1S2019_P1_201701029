class NodeScore:
    def __init__(self,x,y):
        self.x=x
        self.y=y

        self.cont=0
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
    def printStack(self):
        aux = self.first
        while aux !=None:
            print(aux.x,aux.y)
            aux = aux.next

    def generearDoc(self):
        texto = "digraph {\n rankdir=LR; \n node [shape=record];"
        pila1 = 'subgraph cluster_0 { \n  label="Pila Scores 1"; \n struct1 [label ="|'
        datosPila1=""
        cont = 0
        aux = self.first
        while aux !=None:
            datosPila1 += "<f"
            datosPila1 += str(cont)
            datosPila1 += ">"
            datosPila1 += str(aux.x)+","+str(aux.y)
            datosPila1 += "|"
            cont+=1
            aux = aux.next
        if aux is None:
            if self.first is None:
                datosPila1="<f0>"
            datosPila1=datosPila1[:-1]
            print(datosPila1)
            datosPila1 =datosPila1 + '"];\n}\n}'
            with open("Pila1.txt",'w',encoding = 'utf-8') as f:
                f.write(texto+pila1+datosPila1)

    def PopScore(self):
        x=0
        y=0
        x = self.first.x
        y = self.first.y
        self.first=self.first.next
