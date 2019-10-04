import sys
from random import *
from PIL import Image

def check_rule(pixels, color0, color1, rule_binary, rule_slot, column, row):
    if rule_binary[rule_slot] == '0':
        pixels[column, row] = (color0)
    elif rule_binary[rule_slot] == '1':
        pixels[column, row] = (color1)

def main(width, height, pixel_size, color0, color1, rule_num, random_or_center):

    sample_width = width // pixel_size
    sample_height = height // pixel_size

    start_row = ''
    if random_or_center == 'random':
        for n in range(sample_width):
            char = str(randint(0, 1))
            start_row = start_row + char
    elif random_or_center == 'center':
        for n in range(sample_width):
            if n == sample_width // 2:
                start_row = start_row + '1'
            else:
                start_row = start_row + '0'

    if rule_num == 'random':
        rule_num = randrange(256)

    print('Rule:', rule_num)
    rule_binary = ''
    rule_value = int(rule_num)
    power = 7
    while power >= 0:
        value = 2**power
        if rule_value // value == 1:
            rule_value = rule_value - value
            rule_binary = rule_binary + '1'
            power -= 1
        elif rule_value // value == 0:
            rule_binary = rule_binary + '0'
            power -= 1

    wolfram_sample = Image.new('RGB', (sample_width, sample_height))
    pixels = wolfram_sample.load()

    for column in range(sample_width):
        if start_row[column] == '0':
            pixels[column, 0] = (color0)
        elif start_row[column] == '1':
            pixels[column, 0] = (color1)

#    for row in range(sample_height - 1):
#        pixels[0, row] = (color0)
#        pixels[sample_width - 1, row] = (color0)

    for row in range(1, sample_height):
        for column in range(sample_width):
            try:
                left = pixels[column-1, row-1]
            except:
                left = pixels[sample_width-1, row-1]
            try:
                right = pixels[column+1, row-1]
            except:
                right = pixels[0, row-1]
            middle = pixels[column, row-1]

            if row < sample_height - 1:
                if left == (color0) and middle == (color0) and right == (color0):
                    check_rule(pixels, color0, color1, rule_binary, 7, column, row)
                elif left == (color0) and middle == (color0) and right == (color1):
                    check_rule(pixels, color0, color1, rule_binary, 6, column, row)
                elif left == (color0) and middle == (color1) and right == (color0):
                    check_rule(pixels, color0, color1, rule_binary, 5, column, row)
                elif left == (color0) and middle == (color1) and right == (color1):
                    check_rule(pixels, color0, color1, rule_binary, 4, column, row)
                elif left == (color1) and middle == (color0) and right == (color0):
                    check_rule(pixels, color0, color1, rule_binary, 3, column, row)
                elif left == (color1) and middle == (color0) and right == (color1):
                    check_rule(pixels, color0, color1, rule_binary, 2, column, row)
                elif left == (color1) and middle == (color1) and right == (color0):
                    check_rule(pixels, color0, color1, rule_binary, 1, column, row)
                elif left == (color1) and middle == (color1) and right == (color1):
                    check_rule(pixels, color0, color1, rule_binary, 0, column, row)

#    wolfram_sample.show()

    wolfram_image = Image.new('RGB', (width, height))
    squares = wolfram_image.load()

    for row in range(sample_height):
        for column in range(sample_width):
            color = pixels[column, row]
            for j in range(pixel_size):
                for k in range(pixel_size):
                    squares[pixel_size*column + k, pixel_size*row + j] = color

    wolfram_image.show()


if __name__ == '__main__':
    width = 1900
    height = 1060
    pixel_size = 2
    color0 = (0,0,0) #(78,78,84)
    color1 = (255,255,255) #(104,104,112)
    rule_num = '129'
    main(width, height, pixel_size, color0, color1, rule_num, 'center')

#   Beautiful rules:
#       129; 110; 73; 169; 147; 183; 60; 105
