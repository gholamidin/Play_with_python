from PIL import Image
import numpy 

def image2txt(inputFile, outputFile):
	im = Image.open(inputFile).convert('L')
	charWidth = 100
	im = im.resize((charWidth, charWidth // 2))
	target_width, target_height = im.size
	data = numpy.array(im)[:target_height, :target_width]
	f = open(outputFile, 'w',encoding='utf-8')
	for row in data:
		for pixel in row:
			if pixel > 127:
				f.write('1')
			else:
				f.write(' ')
		f.write('\n')
	f.close()