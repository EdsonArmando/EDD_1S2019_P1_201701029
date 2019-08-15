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
		self.size=0
	def isEmpty(self):
		if self.first is None:
			return True
		else:
			return False
	def returnSize(self):
		return self.size
	def ScoreEnqueue(self,name,points):
		new = ScoreBoardNode(name,points)

		if self.first is None:
			self.first = new
			self.last = new
			self.size+=1
		else:
			self.last.next = new
			self.last = new
			self.size+=1

	def ScoreDequeue(self):
		if self.first == self.last:
			self.first=None
			self.last=None
			self.size-=1
		else:
			self.first=self.first.next
			self.size-=1
	def GenerateImage(self):
		texto = 'digraph {\n rankdir=LR; \n node [shape=record]; \n label="ScoreBoard";\n null [label="NULL" shape=box];\n'
		datesSocre=""
		aux = self.first
		cont=0
		while aux !=None:
			datesSocre+= str(cont)+'[label="{<data> '+'('+aux.name+','+str(aux.points)+')'+ '| <ref>  }", width=1.2]\n'
			if aux.next!=None:
				datesSocre+= str(cont)+':ref:c'+'->' +str(cont+1)+':data\n'
			cont+=1
			aux = aux.next
		with open("ScoreBoard.txt",'w',encoding = 'utf-8') as f:
			f.write(texto+datesSocre+str(cont-1)+':ref:c->null\n}')
			f.close()
		cmd='dot -Tpng ScoreBoard.txt -o scoreBoard.png'
		os.system(cmd)
		os.system('scoreBoard.png')
	def getFirst(self):
		return self.first
	def printValue(self):
		aux = self.first
		while aux !=None:
			print(aux.name, aux.points)
			aux = aux.next
