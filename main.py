from PIL import Image
import glob
import argparse
import os
from os.path import join

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset', required=True, type=str, help='Dataset dir')
parser.add_argument('-r', '--ratio', required=True, type=str, help='Ratio for resize')
parser.add_argument('-e', '--extension', required=True, type=str, help='File extension for saving', default='bmp')
args = parser.parse_args()

scale = int(args.ratio)
source_dir = str(args.dataset)
extension = args.extension

file_list = glob.glob(os.path.join(args.dataset, '*.bmp'), recursive=True)

for f in file_list:
    image = Image.open(f)
    resized = image.resize((238 * scale, 158 * scale), resample=Image.NEAREST)
    resized.save(join('x' + str(scale), os.path.basename(f)), extension)

pass
