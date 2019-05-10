class Label():
	def __init__(self,):
		self.collection = ''
		self.color = ''
		self.order = ''
		self.num = ''
		self.date = ''

	def generate_label(self,collection, color, order, num, date):
		self.collection = collection
		self.color = color
		self.order = order
		self.num = num
		self.date = date

		print(self.collection, self.color, self.order)
		return(self)