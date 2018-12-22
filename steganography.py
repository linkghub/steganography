from re import findall
from random import randint
from PIL import Image, ImageDraw

def encrypt(path, keyfile, text, name):
	keys = []
	img = Image.open(path)
	draw = ImageDraw.Draw(img)
	width = img.size[0]
	height = img.size[1]
	pix = img.load()
	f = open(keyfile, 'w')

	for elem in ([ord(elem) for elem in text]):
		key = (randint(1, width - 10), randint(1, height - 10))
		g, b = pix[key][1:3]
		draw.point(key, (elem, g, b))
		f.write(str(key) + '\n')
	img.save(name, "PNG")
	f.close()

def decrypt(path, keyfile):
	a = []
	keys = []
	img = Image.open(path)
	pix = img.load()
	f = open(keyfile, 'r')
	y = str([line.strip() for line in f])

	for i in range(len(findall(r'\((\d+)\,',y))): 
		keys.append((int(findall(r'\((\d+)\,',y)[i]),int(findall(r'\,\s(\d+)\)',y)[i]))) 
	for key in keys: 
		a.append(pix[tuple(key)][0]) 
	return ''.join([chr(elem) for elem in a])