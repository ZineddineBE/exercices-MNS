from classes.Material import Material

class Cup:
	def __init__(self, material:Material, volume, color):
		self.material = material
		self.volume = volume
		self.color = color
		self.has_handle = True
		self.content = None

	def __str__(self):
		return f"Materiel : {self.material.name} | Volume : {self.volume} | Color : {self.color} | Content : {self.content}"

	def fill(self, content):
		if not self.is_filled():
			self.content = content
		else:
			print("La tasse est déjà pleine !")
			
	def empty(self):
		self.content = None
		
	def is_filled(self):
		return self.content != None
	