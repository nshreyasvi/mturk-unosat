
"""
Description:
Use this script if you want to cut up a large image before posting it online so that Turkers can annotate small portions of the image. The script was developed with the intention of cutting up high resolution 2000x2000 pixel satellite imagery so users could annotate 300 x 300 pixel squares. Once you have run this script, a folder will be created inside toWeb/public/images called the name of the image you cut up without the file extension.

If you would like to process large Satellite images, follow the steps below
1. Set imageToCut as the name of the image you would like to cut and run EXTENSION_PreprocessLargeImage.py
2. Open ASCRIPT_begin.py and set folderToPublish as the name of the image without the file extension. Run it.
3. Wait for Annotations
4. Run ASCRIPT_finish.py with the appropriate Batch ID
5. Run EXTENSION_PostprocessLargeImage.py with on the specified Batch ID 

Variable Information

imageToCut				-	Name of large image that needs to be cut. It must be located inside the folder imToCut
length					-	Sidelength (in pixels) for the images you would like to cut out
overlap 				- 	Overlap between images that get cut
"""
#====================== Set Variables below
imageToCut = 'muna.tif'
length = 400
overlap = 100
#======================

import os
from imCut import cut
iname = imageToCut.split('.')[0]

cut(imageToCut, length, overlap)

if not os.path.exists('toWeb/public/images/'+iname):
	cut(imageToCut, length, overlap)
