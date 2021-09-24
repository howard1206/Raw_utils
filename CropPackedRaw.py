# -*- coding:utf8 -*-
import numpy as np
import sys
import codecs
from os import makedirs
from os import walk
import os.path
import subprocess
import argparse

def even_checker(n):
    num = int(n)
    if (num % 2) == 1:
        raise argparse.ArgumentTypeError('Input number has to be even!!!') 
    else:
        return num

def bound_checker(a, b, c):
    if a + b > c:
        print("Cropping out of bound!!!")
        exit()

def crop_image(img, top, left, crop_h, crop_w):
    return data[top:top+crop_h, left:left+crop_w]

def get_parser():
    parser = argparse.ArgumentParser(description='This is a script for cropping raw(unpack raw),each pixel 10bits. Please use python3, and please unified the input raw resolution.')
    parser.add_argument('folder_path', default='./', type=str, help='The folder path contains input raw to be processed.')
    parser.add_argument('img_w', default='4096', type=even_checker, help='The width of the input raw.')
    parser.add_argument('img_h', default='3072', type=even_checker, help='The height of the input raw.')
    parser.add_argument('left', default='600', type=even_checker, help='The crop width you wish for.')
    parser.add_argument('top', default='600', type=even_checker, help='The crop height you wish for.')
    parser.add_argument('crop_w', default='1536', type=even_checker, help='The crop width you wish for.')
    parser.add_argument('crop_h', default='1024', type=even_checker, help='The crop height you wish for.')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    folderpath = args.folder_path
    print(folderpath)

    img_width = args.img_w
    img_height = args.img_h
    crop_left = args.left
    crop_top = args.top
    crop_rows = args.crop_h
    crop_cols = args.crop_w
    bound_checker(crop_left, crop_cols, img_width)
    bound_checker(crop_top, crop_rows, img_height)
    #rows = 3072 #height
    #cols = 4096 #width
    #crop_rows = 1024
    #crop_cols = 1536

    for root, dirs, files in walk(folderpath):
        for file in files:
            extension = os.path.splitext(file)[1][1:]
            if extension == 'raw' :
                file_input = folderpath + "/"+ file

                if not os.path.exists('./cropped'):
                    os.makedirs('./cropped')

                file_output = "./cropped/" + os.path.splitext(file)[0] + "_crop_w"+ str(crop_cols)+"_h"+str(crop_rows)+".raw"
                
                print(file_input)
                print(file_output)

                data = np.fromfile(file_input, dtype=np.uint16)
                data = data.reshape(img_height, img_width)
                crop_data = crop_image(data, crop_top, crop_left, crop_rows, crop_cols)

                fp = open(file_output, "wb")
                fp.write(np.ascontiguousarray(crop_data))
                fp.close()
