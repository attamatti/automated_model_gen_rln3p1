#!/usr/bin/env python

import mrcfile
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np

print('Generating class images...')
classdata = open('External/job007/run.out','r').readlines()
for i in classdata:
	if 'Selected ' in i:
		classline = i
		break
classes = [int(x.strip().strip('[]'))-1 for x in classline.split(':')[1].split(',')]
print(classes)

nclasses = len(classes)
nrows = nclasses/8.0
if nclasses%8.0 !=0:
	nrows = int(nrows)+1
else:
	nrows = int(nrows)
print(nrows)

with mrcfile.open('Class2D/job006/run_it025_classes.mrcs') as mrc:
	image_data = []
	for i in classes:
		image_data.append(mrc.data[i])
	if nclasses%8.0 !=0:
		nblanks = (8*(nrows+1))-len(classes)
		for i in range(nblanks):
			image_data.append(np.zeros(mrc.data[0].shape))
fig = plt.figure()
grid = ImageGrid(fig, 111,nrows_ncols=(nrows, 8),axes_pad=0)

for ax, im in zip(grid, image_data):
	ax.imshow(im,cmap='Greys_r')
	ax.xaxis.set_visible(False)
	ax.yaxis.set_visible(False)
plt.savefig('final_classes.png')
