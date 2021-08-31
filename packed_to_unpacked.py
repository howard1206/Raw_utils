# -*- coding:utf8 -*-
#import rawpy
import numpy as np
#import imageio
import matplotlib.pylab as plt
import codecs
from os import walk
import os.path
import subprocess
import argparse

#mypath = "/Users/howard1206/temp_raw_dump/50M_RAW_DUMP/"

def get_parser():
  parser = argparse.ArgumentParser(description='This is a script for unpacking raw,each pixel 10bits but packed. Please use python3, and please unified the input raw resolution.')
  parser.add_argument('folder_path', default='./', type=str, help='The folder path contains input raw to be processed.')
  parser.add_argument('img_w', default='8192', type=str, help='The width of the input raw.')
  parser.add_argument('img_h', default='6144', type=str, help='The height of the input raw.')
  return parser
if __name__ == '__main__':
  parser = get_parser()
  args = parser.parse_args()
  folderpath = args.folder_path

  for root, dirs, files in walk(folderpath):
    for file in files:
      extension = os.path.splitext(file)[1][1:]
      if extension == 'RAWMIPI10' :
        file_input = folderpath + file
        if not os.path.exists('./unpacked'):
          os.makedirs('./unpacked')
        file_output = "./unpacked/" + os.path.splitext(file)[0] + ".raw"
        print(file_output)
        subprocess.run(["./unpack", args.img_w, args.img_h, file_input, file_output])
