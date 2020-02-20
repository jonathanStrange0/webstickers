from reportlab.lib.pagesizes import letter, inch, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
from app.models import Collection, CollectionItem
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__)) # put the files in the right place no matter what!
pdfmetrics.registerFont(TTFont('Monsterrat', basedir+'/Montserrat/Montserrat-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Monsterrat-Bold', basedir+'/Montserrat/Montserrat-Bold.ttf'))
class ShippingLabel():
	# label_page_size = (8*inch, 2.75*inch)
	# PAGE_HEIGHT=label_page_size[1]
	# PAGE_WIDTH=label_page_size[0]

	def __init__(self,):
		self.label_page_size = (8*inch, 2.75*inch)
		self.PAGE_HEIGHT=self.label_page_size[1]
		self.PAGE_WIDTH=self.label_page_size[0]
		self.collection = ''
		self.color = ''
		self.order = ''
		self.num = ''
		self.date = ''
		self.path = str(basedir)+'/labels/'

	def generate_label(self,collection, color, order, num, date):
		self.collection = collection
		self.color = color
		self.order = order # must configure
		self.num = num
		self.date = date
		self.path = self.path + self.order+ '_' + self.num +'.pdf'
		label_canvas = canvas.Canvas(self.path,pagesize=self.label_page_size)

		# Set Label font and sizing & translate
		label_canvas.setLineWidth(0.3)
		label_canvas.setFont('Monsterrat', 32)
		label_canvas.translate(self.PAGE_WIDTH/2.0,self.PAGE_HEIGHT/2.0)

		# Draw RW Logo
		im = Image(basedir+'/final_logo_TM.jpg', width=3*inch, height=1*inch)
		im.drawOn(label_canvas,-1.5*inch,0.25*inch)

		# Draw the Collection Name and SKU Name
		label_canvas.drawString(-self.PAGE_WIDTH/2.0 + 0.25*inch, \
		                        self.PAGE_HEIGHT/2.0-(1.5*inch), \
		                        self.collection)

		label_canvas.drawString(-self.PAGE_WIDTH/2.0 + 0.25*inch, \
		                        self.PAGE_HEIGHT/2.0-(1.5*inch) - 46,\
		                        self.color)

		# Draw labels for production date and run number
		label_canvas.setFont('Monsterrat', 16)

		label_canvas.drawString(self.PAGE_WIDTH/2.0 - 3.5*inch, \
		                        self.PAGE_HEIGHT/2.0-(1.5*inch)-18, \
		                        'Revel Woods Order# ' +self.order)

		label_canvas.drawString(self.PAGE_WIDTH/2.0 - 3.5*inch, \
		                        self.PAGE_HEIGHT/2.0-(1.75*inch)-18, \
		                        'Prod Date: ' +self.date)

		label_canvas.drawString(self.PAGE_WIDTH/2.0 - 3.5*inch, \
		                        self.PAGE_HEIGHT/2.0-(2*inch)-18, \
		                        'Run #: '+self.num)



		label_canvas.save()
		return('labels/'+self.order+ '_' + self.num + '.pdf')

class SampleLabel():

	def __init__(self,item_id):
		self.label_page_size = (8*inch, 3*inch)
		self.PAGE_HEIGHT=self.label_page_size[1]
		self.PAGE_WIDTH=self.label_page_size[0]
		self.item = CollectionItem.query.filter_by(id=item_id).first()
		print(self.item)
		self.date = str(datetime.now().year)+str(datetime.now().month)+str(datetime.now().day)+str(datetime.now().hour)+str(datetime.now().minute)+str(datetime.now().second)`
		self.path = str(basedir)+'/labels/'
		self.path = self.path + self.item.item_name + self.date +'.pdf'

	def generate_sample_label(self):

		if os.path.isfile(self.path):
			print('File exists')
			return('/labels/'+self.item.item_name+'.pdf')
		else:

			label_canvas = canvas.Canvas(self.path,pagesize=self.label_page_size)

			# Set Label font and sizing & translate
			label_canvas.setLineWidth(0.3)
			label_canvas.setFont('Monsterrat-Bold', 24)
			label_canvas.translate(self.PAGE_WIDTH/2.0,self.PAGE_HEIGHT/2.0)

			# Draw RW Logo
			im = Image(basedir+'/final_logo_TM.jpg', width=2*inch, height=2.0/3.0*inch)
			im.drawOn(label_canvas,-3.75*inch,0.5*inch)

			if self.item.collection.collection_name == 'Eddie Bauer Adventure':
			    # Draw EB Logo
			    im = Image('Eddie Bauer HOME.jpg', width=3*inch, height=3.0/5.028*inch)
			    im.drawOn(label_canvas,0.75*inch,0.5*inch)

			# Draw the Collection Name and SKU Name
			label_canvas.drawString(-self.PAGE_WIDTH/2.0 + 0.25*inch,
			                        self.PAGE_HEIGHT/2.0-(1.5*inch),
			                        self.item.collection.collection_name+': '+self.item.item_name)


			# label_canvas.translate(-PAGE_WIDTH/2.0,-PAGE_HEIGHT/2.0)

			label_canvas.setFont('Monsterrat-Bold', 18)


			label_canvas.drawString(-self.PAGE_WIDTH/2.0 + 0.25*inch,
			                        self.PAGE_HEIGHT/2.0-(2*inch),
			                        'Species: '+self.item.species)

			label_canvas.drawString(-self.PAGE_WIDTH/2.0 + 0.25*inch,
			                        self.PAGE_HEIGHT/2.0-(2.5*inch),
			                        'Width: '+self.item.width)

			label_canvas.drawString(-self.PAGE_WIDTH/4 + 2.5*inch,
			                        self.PAGE_HEIGHT/2.0-(2*inch),
			                        'Durability: '+self.item.durability)

			label_canvas.drawString(-self.PAGE_WIDTH/4 + 2.5*inch,
			                        self.PAGE_HEIGHT/2.0-(2.5*inch),
			                        'Length: '+self.item.length)

			label_canvas.save()
			return('/labels/'+self.item.item_name+'.pdf')

class CrossoverLabel():

	def __init__(self,item_id):
		self.label_page_size = (8*inch, 3*inch)
		self.PAGE_HEIGHT=self.label_page_size[1]
		self.PAGE_WIDTH=self.label_page_size[0]
		self.item = CollectionItem.query.filter_by(id=item_id).first()
		print(self.item)
		self.date = str(datetime.now().year)+str(datetime.now().month)+str(datetime.now().day)+str(datetime.now().hour)+str(datetime.now().minute)+str(datetime.now().second)
		self.path = str(basedir)+'/labels/'
		self.path = self.path + self.item.item_name+ self.date +'-Crossover.pdf'

	def generate_crossover_label(self):

		if os.path.isfile(self.path):
			print('File exists')
			return('/labels/'+self.item.item_name+'-Crossover.pdf')
		else:

			label_canvas = canvas.Canvas(self.path,pagesize=self.label_page_size)

			# Set Label font and sizing & translate
			label_canvas.setLineWidth(0.3)
			label_canvas.setFont('Monsterrat-Bold', 24)
			label_canvas.translate(self.PAGE_WIDTH/2.0,self.PAGE_HEIGHT/2.0)

			# Draw the Collection Name and SKU Name
			label_canvas.drawString(-self.PAGE_WIDTH/2.0 + 0.25*inch,
			                        self.PAGE_HEIGHT/2.0-(1.5*inch),
			                        self.item.collection.collection_name+': '+self.item.item_name)


			# label_canvas.translate(-PAGE_WIDTH/2.0,-PAGE_HEIGHT/2.0)

			label_canvas.setFont('Monsterrat-Bold', 18)


			label_canvas.drawString(-self.PAGE_WIDTH/2.0 + 0.25*inch,
			                        self.PAGE_HEIGHT/2.0-(2*inch),
			                        'Species: '+self.item.species)

			label_canvas.drawString(-self.PAGE_WIDTH/2.0 + 0.25*inch,
			                        self.PAGE_HEIGHT/2.0-(2.5*inch),
			                        'IW Name: '+self.item.iw_name)

			label_canvas.save()
			return('/labels/'+self.item.item_name+'-Crossover.pdf')
