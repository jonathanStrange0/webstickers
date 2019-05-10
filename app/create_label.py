from reportlab.lib.pagesizes import letter, inch, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

label_page_size = (8*inch, 2.5*inch)
PAGE_HEIGHT=label_page_size[1]
PAGE_WIDTH=label_page_size[0]
basedir = os.path.abspath(os.path.dirname(__file__)) # put the files in the right place no matter what!
pdfmetrics.registerFont(TTFont('Monsterrat', basedir+'/Montserrat/Montserrat-Regular.ttf'))

class Label():
	def __init__(self,):
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
		self.path = self.path + self.order+'.pdf'
		label_canvas = canvas.Canvas(self.path,pagesize=label_page_size)

		# Set Label font and sizing & translate
		label_canvas.setLineWidth(0.3)
		label_canvas.setFont('Monsterrat', 32)
		label_canvas.translate(PAGE_WIDTH/2.0,PAGE_HEIGHT/2.0)

		# Draw RW Logo
		im = Image(basedir+'/final_logo_TM.jpg', width=3*inch, height=1*inch)
		im.drawOn(label_canvas,-1.5*inch,0.25*inch)

		# Draw the Collection Name and SKU Name
		label_canvas.drawString(-PAGE_WIDTH/2.0 + 0.25*inch, \
		                        PAGE_HEIGHT/2.0-(1.5*inch), \
		                        self.collection)

		label_canvas.drawString(-PAGE_WIDTH/2.0 + 0.25*inch, \
		                        PAGE_HEIGHT/2.0-(1.5*inch) - 46,\
		                        self.color)

		# Draw labels for production date and run number
		label_canvas.setFont('Monsterrat', 16)

		label_canvas.drawString(PAGE_WIDTH/2.0 - 3.5*inch, \
		                        PAGE_HEIGHT/2.0-(1.5*inch)-18, \
		                        'Revel Woods Order# ' +self.order)

		label_canvas.drawString(PAGE_WIDTH/2.0 - 3.5*inch, \
		                        PAGE_HEIGHT/2.0-(1.75*inch)-18, \
		                        'Prod Date: ' +self.date)

		label_canvas.drawString(PAGE_WIDTH/2.0 - 3.5*inch, \
		                        PAGE_HEIGHT/2.0-(2*inch)-18, \
		                        'Run #: '+self.num)



		label_canvas.save()
		return('labels/'+self.order+'.pdf')