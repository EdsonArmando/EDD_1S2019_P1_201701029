import os
import subprocess
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
	def returnFirst(self):
		return self.first
	def isFind(self,name2):
		aux = self.first
		if aux != None:
			while True:
				if aux.name==name2:
					return True
				aux = aux.next
				if self.first.name == aux.name:
					return False
					break
		else:
			return False
	def generateImage(self):
		Cola1 = '\n digraph{\n rankdir=LR;  \n node [shape=record];\n label=\"User List\";\n'
		compras = '';
		aux = self.first
		while True:
			compras += aux.name
			compras += " -> ";
			compras += aux.next.name
			compras += ";\n";
			compras += aux.next.name
			compras += " -> ";
			compras += aux.name
			compras += ";\n";
			aux = aux.next
			if self.first.name == aux.name:
				break
		with open("usersList.txt",'w',encoding = 'utf-8') as f:
			f.write(Cola1+compras+'\n}')
			f.close()
		cmd='dot -Tpng usersList.txt -o user.png'
		os.system(cmd)
		#Sirve para abrir la imagen en windows
		#Descomenta subprocess para que abra la imagen en tu compu
		os.system('user.png')
		#subprocess.check_call(['open','user.png'])
	def printUser(self):
		aux = self.first
		while True:
			print(aux.name)
			aux = aux.next
			if self.first.name == aux.name:
				break
