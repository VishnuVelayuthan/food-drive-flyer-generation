from PIL import Image, ImageFilter, ImageFont, ImageDraw
import textwrap
import random

def putText(img, index, row, W, H):
	font = ImageFont.truetype("bebas.ttf", int(W/30))

	draw = ImageDraw.Draw(img)

	message = row['Note']
	para = textwrap.wrap(message, width=(70))

	current_h, pad = (H/15), 10
	for line in para:
	    w, h = draw.textsize(line, font=font)
	    draw.text(((W - w) / 2, current_h), line, font=font)
	    current_h += h + pad

	file_name = str(index+1) + ". " + row['Staff Member'] + ".png"
	img.save(file_name, "PNG")
	print("Image ", str(index+1), " generated.")

def makeDesign(index, row):
	W, H = (500, 500)
	img = Image.new("RGB", (W, H), color="rgb(70,130,180)").convert('RGBA')
	
	randomNumber = random.randint(1,4)
	fileName = 'design' + str(randomNumber) + '.png'
	foreground = Image.open(fileName).convert('RGBA')

	imageWithDesign = Image.alpha_composite(img, foreground)

	putText(imageWithDesign, index, row, W, H)