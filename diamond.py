class A:
	def__init__(self):
	print("A")
	
	def dance(self):
		print("Naacho A")


class B(A):
	def__init__(self):
	print("B")

	def naacho(self):
		print("Naacho B")


class C(A):
	def__init__(self):
	print("C")

	def naacho(self):
		pritn("Naacho C")


class D(B,C):
def__init__(self):
self.dance()

#Check Method Resolution Order(MRO)
D.mro()


#Remove Diamond Problem

class A:
   def__init__(self):
     print("A")
  
  def Dance(self):
     print("Naacho A")


class B(A):
  def__init__(self):
     print("B")


class C:
  def__init__(self):
     print("C")


class D(B,C):
  def__init__(self):
    self.dance()

#Check the MRO again to observe the difference
  D.mro()		