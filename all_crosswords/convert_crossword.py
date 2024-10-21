
#import libraries
import fitz
import PyPDF2
from PIL import Image
import os
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green, white, Color
from reportlab.lib.pagesizes import A4


##########################################################################################
# configuration
#input_indices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
input_indices = ['16']
#State n for nxn crosswords
dic = { '1' : 8,
	'2' : 11,
	'3' : 11,
	'4' : 11,
	'5' : 11,
	'6' : 13,	
	'7' : 15,	
	'8' : 13,
	'9' : 13,
	'10' : 13,	
	'11' : 13,		
	'12' : 13,		
	'13' : 13,
	'14' : 15,
	'15' : 11,
	'16' : 13		
	}	

##########################################################################################

def read_contents(input_idx):

	#names
	input_pdf = 'crosswords/crossword_%s.pdf'%input_idx
	image = 'crossword_%s.png'%input_idx
	image_gs = 'crossword_%s_gs.png'%input_idx

	#Get the image
	pdf = fitz.open(input_pdf)
	image_list = pdf.get_page_images(0)
	img = image_list[0]
	xref = img[0]
	pix = fitz.Pixmap(pdf, xref)
	if not os.path.exists(image):
		pix.save(image)
	img = Image.open(image).convert('L')
	if not os.path.exists(image_gs):
		img.save(image_gs)
		
	#Get image alignment
	page = pdf[0]
	items = page.get_images(full=True)
	bbox = page.get_image_bbox(items[0])
	box_x0 = bbox[0]; box_y0 = bbox[1]; box_x1 = bbox[2]; box_y1 = bbox[3];

	
	#Get the text
	PDFfile = open(input_pdf, 'rb')
	PDFfilereader = PyPDF2.PdfFileReader(PDFfile)
	page = PDFfilereader.getPage(0)
	page_width = page.mediaBox[2]
	page_height = page.mediaBox[3]
	PDFfile.close()
	

	return page_width, page_height, box_x0, box_y0, box_x1, box_y1
	

def image_geometry(input_idx):
	
	n_grid = dic[input_idx]
	image_gs = 'crossword_%s_gs.png'%input_idx
	
	#Get crossword extremities
	img = Image.open(image_gs)            
	img = np.array(img)
	#print(img.shape)#(476, 479)
	image_height = img.shape[0]
	image_width = img.shape[1]
	max_ix = 0; min_ix = img.shape[1]; max_iy = 0; min_iy = img.shape[0]
	for iy, ix in np.ndindex(img.shape):
		if img[iy, ix] < 255:
			if iy < min_iy:
				min_iy = iy
			if iy > max_iy:
				max_iy = iy
			if ix < min_ix:
				min_ix = ix
			if ix > max_ix:
				max_ix = ix						
	#print(max_ix, min_ix, max_iy, min_iy)
	
	#Get crossword pattern
	x_step =  (max_ix - min_ix) / n_grid
	y_step =  (max_iy - min_iy) / n_grid
	
	#Check off-center pixel in box to see if it's a dark or bright box
	pattern = np.zeros((n_grid, n_grid))
	for i in range(n_grid):
		for j in range(n_grid):
			pixCenter_x = int((0.8 * x_step) + (i*x_step))
			pixCenter_y = int((0.8 * y_step) + (j*y_step))
			if img[pixCenter_y, pixCenter_x] == 255:
				pattern[j,i] = 1
				
	return image_height, image_width, max_ix, min_ix, max_iy, min_iy, pattern
	
	
def make_pdf(input_idx, page_width, page_height, image_height, image_width, box_x0, box_y0, box_x1, box_y1, max_ix, min_ix, max_iy, min_iy, pattern):

	n_grid = dic[input_idx]
	image = 'crossword_%s.png'%input_idx
	image_gs = 'crossword_%s_gs.png'%input_idx
	output_pdf = 'output/crossword_%s_fill.pdf'%input_idx
	text_across = 'text/across_%s.txt'%input_idx
	text_down = 'text/down_%s.txt'%input_idx
	
	c = canvas.Canvas(output_pdf)
	c.setPageSize((page_width, page_height))
	
	c.setFont('Times-Bold', 18)
	c.drawCentredString(300, 740, 'Raju\'s Crossword - %s'%input_idx)	
	form = c.acroForm
	
	# define a transparent color
	transparent = Color( 255, 255, 255, alpha=0.0)
	
	# Draw crossword image
	# box_x0, box_y0, box_x1, box_y1, are in fitz coordinates that start from a top-left origin
	box_width = box_x1-box_x0; box_height = box_y1-box_y0
	# We convert to reportlab coordinates which start from a bottom-left origin
	box_x = box_x0 + (box_width/2) #for the reportlab-canvas
	box_y = page_height - (box_y0 + (box_height/2)) #for the reportlab-canvas
	c.drawImage(image=image_gs, x=box_x, y=box_y, preserveAspectRatio=True, width=box_width, anchorAtXY=True)
	
	# Draw fields
	#offset of image in page
	img_off_x = box_x0; img_off_y = page_height - box_y1;
	#offset of crossword square in image
	sq_off_x = (min_ix *box_width)/image_width
	sq_off_y = ((image_height-max_iy) *box_height)/image_height
	#cell width and height
	cell_width = ((max_ix - min_ix) * box_width)/(image_width*n_grid)
	cell_height= ((max_iy - min_iy) * box_height)/(image_height*n_grid)
	#full offsets
	off_x1 = img_off_x + sq_off_x; off_y1 = img_off_y + sq_off_y + ((n_grid-1)*cell_height)
	
	for i in range(n_grid):
		for j in range(n_grid):
			#cell-dependent offset
			off_x2 = i*cell_width; off_y2 = j*cell_height
			off_x = off_x1 + off_x2; off_y = off_y1 - off_y2
			if(pattern[j,i] == 1):
				form.textfield(name='', tooltip='', x=off_x, y=off_y, borderStyle='inset', borderColor=transparent, fillColor=transparent, width=cell_width, height = cell_height,
				textColor=blue, forceBorder=True, maxlen = 1, fontSize=16, fontName='Times-Bold')
	
	#add text
	c.setFont('Times-Bold', 12)
	c.drawCentredString(300, 350, 'Clues')
	
	text_a = open(text_across,'r+').read()
	text_d = open(text_down,'r+').read()
	
	textobject_A = c.beginText(50, 335); textobject_D = c.beginText(325, 335);
	textobject_A.textLine('Across'); textobject_D.textLine('Down');
	c.drawText(textobject_A); c.drawText(textobject_D)
	
	c.setFont('Times-Roman', 12)
	textobject_a = c.beginText(50, 320); textobject_d = c.beginText(325, 320);
	for line in text_a.splitlines(False):
		textobject_a.textLine(line.rstrip())
	for line in text_d.splitlines(False):
		textobject_d.textLine(line.rstrip())	
			
	c.drawText(textobject_a); c.drawText(textobject_d)

	c.save()
	os.remove(image); os.remove(image_gs)
	
	return
	


if __name__ == '__main__':

	for input_idx in input_indices:
	
		#get image and text
		page_width, page_height, box_x0, box_y0, box_x1, box_y1 = read_contents(input_idx)

		#get relavant parameters of the crossword image
		image_height, image_width, max_ix, min_ix, max_iy, min_iy, pattern = image_geometry(input_idx)

		#make a fillable crossword puzzle pdf
		make_pdf(input_idx, page_width, page_height, image_height, image_width, box_x0, box_y0, box_x1, box_y1, max_ix, min_ix, max_iy, min_iy, pattern)
















