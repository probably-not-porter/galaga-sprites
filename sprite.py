import PIL, random, sys, argparse, math
from PIL import Image, ImageDraw
import noise

pix_width = 16
pix_height = 16
block_size = 20

width = pix_height * block_size
height = pix_height * block_size
numColors = 3

def main():
    pil_image = Image.new('RGBA', (width, height))
    pixels = pil_image.load()
    colorList = []

    for x in range(numColors):
        color = genColor(colorList)
        colorList.append(color)
    
    for i in range(pil_image.size[0] / (block_size * 2)):
        for j in range(pil_image.size[1] / block_size):
            decider = decideFill(i,j)
            if decider:
                colorBlock(i,j,pixels, colorList)
            else:
                print('block empty')
                colorBlock(i,j,pixels, [(0, 0, 0)])
    
    pil_image = pil_image.rotate(180)
    pil_image.save('output' + '.png')
    print('done')

def colorBlock(starting_x, starting_y,pixels, colors):
    print('creating block ' + str(starting_x) + ',' + str(starting_y) + '...')
    color = colors[random.randint(0,len(colors)-1)]
    for x in range(block_size):
        target_x = starting_x * block_size + x
        for y in range(block_size):
            target_y = starting_y * block_size + y
            pixels[target_x, target_y] = color
            pixels[(width - 1) - target_x, target_y] = color

def genColor(color_list):
    accept = False
    color = None
    while (accept == False):
        if color != None:
            print('Color too similar, regenerate...')
        color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if color_list == []:
            accept = True
        else:
            for c in color_list:
                for x in range(3):
                    if c[x] + 10 < color[x] or c[x] - 10 > color[x]:
                        accept = True
    return color

def decideFill(x,y):
    if (random.randint(2,(pix_width/2)) < x) and (random.randint(1,(pix_height/2)) < y+(y/5)):
        return True
    else:
        return False

if __name__ == "__main__":
    main()