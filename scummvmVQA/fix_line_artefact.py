# import imageio
import os
import sys

import cv2
import numpy as np

sourceextension=".png"
targetextension=".png"

filelist = sorted([x for x in os.listdir(".") if x.lower().endswith(sourceextension)])

if not os.path.exists("linefixed"):
	os.mkdir("linefixed")

print("asdf?")
for file in filelist:
	print(file)
	rgb = cv2.imread(file, cv2.IMREAD_COLOR)
	#rgb = cv2.imread(file, cv2.IMREAD_UNCHANGED)
	#print(type(rgb[0][0][0]))
	rgb32=rgb.astype(np.float32)
	shape=rgb.shape
	#exit()
	for xi in range(0,shape[1],4):
		for yi in range(0,shape[0],4):
			verticalpixel_1=rgb32[yi+0][xi+0]
			verticalpixel_2=rgb32[yi+2][xi+0]
			if np.all([verticalpixel_2,verticalpixel_1]):
				verticalpixel=(verticalpixel_2+verticalpixel_1)/2
				#verticalpixel_avg=(verticalpixel[0]+verticalpixel[1]+verticalpixel[2])/3

				# all other pixels in block
				# verticalbg+=rgb[yi+0][xi+0]
				# verticalbg = rgb32[yi + 0][xi + 1]
				# verticalbg += rgb32[yi + 0][xi + 2]
				# verticalbg += rgb32[yi + 0][xi + 3]
				#
				# verticalbg+=rgb32[yi+1][xi+0]
				# verticalbg+=rgb32[yi+1][xi+1]
				# verticalbg+=rgb32[yi+1][xi+2]
				# verticalbg+=rgb32[yi+1][xi+3]
				#
				# #verticalbg+=rgb[yi+0][xi+0]
				# verticalbg+=rgb32[yi+2][xi+1]
				# verticalbg+=rgb32[yi+2][xi+2]
				# verticalbg+=rgb32[yi+2][xi+3]
				#
				# verticalbg+=rgb32[yi+3][xi+0]
				# verticalbg+=rgb32[yi+3][xi+1]
				# verticalbg+=rgb32[yi+3][xi+2]
				# verticalbg+=rgb32[yi+3][xi+3]
				# verticalbg/=4*4-2


				# dither corner pixels
				# verticalbg+=rgb[yi+0][xi+0]
				verticalbg_1 = rgb32[yi + 0][xi + 1]
				# verticalbg += rgb32[yi + 0][xi + 2]
				verticalbg_2 = rgb32[yi + 0][xi + 3]

				verticalbg_3 =rgb32[yi+1][xi+0]
				# verticalbg+=rgb32[yi+1][xi+1]
				# verticalbg+=rgb32[yi+1][xi+2]
				# verticalbg+=rgb32[yi+1][xi+3]

				#verticalbg+=rgb[yi+0][xi+0]
				verticalbg_4=rgb32[yi+2][xi+1]
				# verticalbg+=rgb32[yi+2][xi+2]
				verticalbg_5=rgb32[yi+2][xi+3]

				# verticalbg+=rgb32[yi+3][xi+0]
				# verticalbg+=rgb32[yi+3][xi+1]
				# verticalbg+=rgb32[yi+3][xi+2]
				# verticalbg+=rgb32[yi+3][xi+3]
				if np.all([verticalbg_5,verticalbg_4,verticalbg_3,verticalbg_2,verticalbg_1]):
					verticalbg=(verticalbg_5+verticalbg_4+verticalbg_3+verticalbg_2+verticalbg_1)/5.
					#verticalbg_avg=(verticalbg[0]+verticalbg[1]+verticalbg[2])/3

					verticalbg_h, verticalbg_s, verticalbg_v=cv2.cvtColor(np.array([np.array([verticalbg])]),cv2.COLOR_RGB2HSV)[0][0]


					verticalpixel_h,verticalpixel_s,verticalpixel_v=cv2.cvtColor(np.array([np.array([verticalpixel])]),cv2.COLOR_RGB2HSV)[0][0]

					#verticalbg_s>.1 and
					if abs(verticalpixel_h-verticalbg_h)>.1:
						#print(verticalbg_s)
						if verticalbg[0]-verticalpixel[0]>1:
							rgb[yi + 0][xi + 0] = (255.,255.,255.)
							rgb[yi + 2][xi + 0] = (255.,255.,255.)
						if verticalbg[1]-verticalpixel[1]>1:
							rgb[yi + 0][xi + 0] = (255.,255.,255.)
							rgb[yi + 2][xi + 0] = (255.,255.,255.)
						if verticalbg[2]-verticalpixel[2]>1:
							rgb[yi + 0][xi + 0] = (255.,255.,255.)
							rgb[yi + 2][xi + 0] = (255.,255.,255.)
							#print(verticalbg)

	#rgb=rgb.astype(np.uint8)

	cv2.imwrite("linefixed\\"+file,rgb)


