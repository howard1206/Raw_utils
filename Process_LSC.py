# -*- coding: utf-8 -*-
import numpy as np
import sys
import codecs
from os import makedirs
from os import walk
import os.path
import subprocess
import argparse
#import rawpy
#import imageio
#import codecs
import cv2

def get_parser():
	parser = argparse.ArgumentParser(description='This is a script for cropping raw(unpack raw),each pixel 10bits. Please use python3, and please unified the input raw resolution.')
	parser.add_argument('folder_path', default='.', type=str, help='The folder path contains input raw to be processed.')
	parser.add_argument('txt_path', default='.', type=str, help='The txt path contains input meta to be processed.')
	parser.add_argument('img_w', default='4096', type=str, help='The width of the input raw.')
	parser.add_argument('img_h', default='3072', type=str, help='The height of the input raw.')
	return parser

if __name__ == '__main__':
	parser = get_parser()
	args = parser.parse_args()
	
	folderpath = args.folder_path
	txtpath = args.txt_path
	print(folderpath)
	
	img_width = args.img_w
	img_height = args.img_h
	#rows = 3072 #height
	#cols = 4096 #width
	#crop_rows = 1024
	#crop_cols = 1536
	count = 0
	for root, dirs, files in walk(folderpath):
		for file in files:
			extension = os.path.splitext(file)[1][1:]
			if extension == 'raw' or extension == 'RawPlain16LSB1' :
				file_input = folderpath + "/"+ file

				if not os.path.exists('./LSC_output'):
					os.makedirs('./LSC_output')
				
				file_output = "./LSC_output/" + '%02d' % count  + ".raw"

				print(file_input)
				print(file_output)
				raw_format = '3' # RGGB-0, GRBG-1, GBRG-2, BGGR-3
				blk_level = '64'
				raw_bit = '10'
				subprocess.run(["LSC.exe", file_input, args.img_w, args.img_h, raw_bit, raw_format, blk_level, txtpath, file_output])
				count = count + 1