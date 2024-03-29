# import imageio
import os
import sys
import time
import cv2
import numpy as np

import concurrent.futures
import datetime

sourceextension=".png"
targetextension=".png"

fixline=True

fixpoints=True

fixblack=True
blackfloor = 8
blursize = 3

debug=False

overwrite=False


filelist = sorted([x for x in os.listdir(".") if x.lower().endswith(sourceextension)])

fixedpath="linefix"

if not os.path.exists(fixedpath):
	os.mkdir(fixedpath)

cv2.setUseOptimized(True)


def fixfile(file):
	if not overwrite and os.path.exists(fixedpath+"\\"+file):
		return
	starttime = time.time()
	#rgb = cv2.imread(file, cv2.IMREAD_UNCHANGED)#.astype(np.float32)
	rgb = cv2.imread(file, cv2.IMREAD_COLOR)#.astype(np.float32)

	# with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
	# 	for _ in executor.map(lambda xi: fixfile_x(rgb,xi), range(4, rgb.shape[1], 4)):
	# 		pass

	mask = cv2.inRange(rgb, np.array([0, 0, 0]), np.array([blackfloor, blackfloor, blackfloor]))
	if fixblack:
		# print(mask)
		# rgb_blurry[mask==0]=[blackfloor,blackfloor,blackfloor]
		rgb_blurry = cv2.blur(rgb.astype(np.float32), (blursize, blursize))
		# rgb_blurry = cv2.GaussianBlur(rgb.astype(np.float32), (blursize, blursize),0)
		# rgb_blurry = cv2.bilateralFilter(rgb.astype(np.float32), 30, 75, 75, cv2.BORDER_DEFAULT)

		if debug:
			rgb[mask!=0] = [255,255,0]
		else:
			rgb_blurry=rgb_blurry+blackfloor/2
			rgb[mask!=0] = rgb_blurry[mask!=0].astype(np.uint8)

	for yi in range(4, rgb.shape[0], 4):
		for xi in range(4, rgb.shape[1], 4):

			if mask[yi,xi] is 0 or np.average(rgb[yi, xi]) >= np.average(rgb[yi, xi + 1]) or np.average(rgb[yi, xi]) >= np.average(rgb[yi, xi - 1]):
				continue

			# verticalpixel_1=rgb[yi+0][xi+0]
			# verticalpixel_2=rgb32[yi+2][xi+0]
			# verticalpixel=(verticalpixel_2+verticalpixel_1)/2

			# verticalline_left_avg = np.average(np.average(verticalline_left, axis=0), axis=0)
			# (verticalline_left_avg_B, verticalline_left_avg_G, verticalline_left_avg_R) = verticalline_left_avg

			verticalline_left = rgb[yi:yi + 4, xi - 1:xi]
			verticalline_right = rgb[yi:yi + 4, xi + 1:xi + 3]
			verticalline_bordering = np.concatenate((verticalline_left, verticalline_right), axis=1)

			verticalline_bordering_B, verticalline_bordering_G, verticalline_bordering_R = cv2.split(
				verticalline_bordering)
			verticalline_bordering_R_flat = verticalline_bordering_R.flatten()
			verticalline_bordering_G_flat = verticalline_bordering_G.flatten()
			verticalline_bordering_B_flat = verticalline_bordering_B.flatten()

			# verticalline_avg = np.max(np.max(verticalline, axis=0), axis=0)
			# (verticalline_avg_B, verticalline_avg_G, verticalline_avg_R) = verticalline_avg
			# verticalline_avg_avg=np.average(verticalline_avg)

			# print(verticalline)

			# block=rgb[yi:yi+3, xi+1:xi+3]
			# block_B, block_G, block_R=cv2.split(block)

			def range_of_vals(x, axis=0):
				return np.max(x, axis=axis) - np.min(x, axis=axis)

			#maxvariance = 10 # post neat
			maxvariance = 8 # pre neat
			# invalidate high variance bordering lines
			if not (range_of_vals(verticalline_bordering_R_flat) > maxvariance and range_of_vals(
					verticalline_bordering_G_flat) > maxvariance and range_of_vals(
				verticalline_bordering_B_flat) > maxvariance):
				if fixline:

					verticalline = rgb[yi:yi + 4, xi:xi + 1]
					(verticalline_B, verticalline_G, verticalline_R) = cv2.split(verticalline)

					verticalline_R_flat = verticalline_R.flatten()
					verticalline_G_flat = verticalline_G.flatten()
					verticalline_B_flat = verticalline_B.flatten()

					maxvariance = 4
					# invalidate high variance lines
					if not (range_of_vals(verticalline_R_flat) > maxvariance and range_of_vals(
							verticalline_G_flat) > maxvariance and range_of_vals(verticalline_B_flat) > maxvariance):

						verticalline_R_max = np.max(verticalline_R_flat).astype(np.int16)
						verticalline_G_max = np.max(verticalline_G_flat).astype(np.int16)
						verticalline_B_max = np.max(verticalline_B_flat).astype(np.int16)
						verticalline_bordering_R_min = np.min(verticalline_bordering_R_flat).astype(np.int16)
						verticalline_bordering_G_min = np.min(verticalline_bordering_G_flat).astype(np.int16)
						verticalline_bordering_B_min = np.min(verticalline_bordering_B_flat).astype(np.int16)
						minlinediff = 2

						# if ( verticalline_bordering_R_min > verticalline_R_max \
						# 	 and verticalline_bordering_G_min>verticalline_G_max \
						# 	 and verticalline_bordering_B_min>verticalline_B_max \
						# 		)  and (\
						# 	verticalline_bordering_R_min-verticalline_R_max > minlinediff \
						# 	or verticalline_bordering_G_min-verticalline_G_max > minlinediff \
						# 	or verticalline_bordering_B_min-verticalline_B_max > minlinediff \
						# 		):
						# if (verticalline_bordering_R_min>verticalline_R_max and verticalline_bordering_R_min-verticalline_R_max > minlinediff) \
						# 		or (verticalline_bordering_G_min>verticalline_G_max and verticalline_bordering_G_min-verticalline_G_max > minlinediff) \
						# 		or (verticalline_bordering_B_min>verticalline_B_max and verticalline_bordering_B_min-verticalline_B_max > minlinediff):
						if (verticalline_bordering_R_min - verticalline_R_max > minlinediff) \
								or (verticalline_bordering_G_min - verticalline_G_max > minlinediff) \
								or (verticalline_bordering_B_min - verticalline_B_max > minlinediff):
							if debug:
								rgb[yi + 0][xi + 0] = (255, 0, 0)
								rgb[yi + 1][xi + 0] = (255, 0, 0)
								rgb[yi + 2][xi + 0] = (255, 0, 0)
								rgb[yi + 3][xi + 0] = (255, 0, 0)
							# rgb[yi + 0:yi + 4][xi + 0:xi + 4]=(255, 0, 0)
							# verticalline=(255, 0, 0)
							else:
								rgb[yi + 0][xi + 0] = rgb[yi + 0][xi + 1] / 2 + rgb[yi + 0][xi - 1] / 2
								rgb[yi + 1][xi + 0] = rgb[yi + 1][xi + 1] / 2 + rgb[yi + 1][xi - 1] / 2
								rgb[yi + 2][xi + 0] = rgb[yi + 2][xi + 1] / 2 + rgb[yi + 2][xi - 1] / 2
								rgb[yi + 3][xi + 0] = rgb[yi + 3][xi + 1] / 2 + rgb[yi + 3][xi - 1] / 2

							continue

				if fixpoints:
					# block=rgb[yi:yi+4, xi+1:xi+4]
					# block_avg = np.average(np.average(block, axis=0), axis=0)
					# (block_B_avg, block_G_avg, block_R_avg) = block_avg
					# block_avg_avg=np.average(block_avg)
					#
					# verticalpixel=rgb[yi+0][xi+0]/2+rgb[yi+2][xi+0]/2
					#
					# (verticalpixel_B, verticalpixel_G, verticalpixel_R) = verticalpixel
					#
					# verticalpixel_1_surrounded = rgb[yi + 1][xi + 1] / 4 \
					# 							 + rgb[yi + 1][xi - 1] / 4 \
					# 							 + rgb[yi - 1][xi + 1] / 4 \
					# 							 + rgb[yi - 1][xi - 1] / 4
					#
					# verticalpixel_2_surrounded = rgb[yi + 3][xi + 1] / 4 \
					# 							 + rgb[yi + 3][xi - 1] / 4 \
					# 							 + rgb[yi + 1][xi + 1] / 4 \
					# 							 + rgb[yi + 1][xi - 1] / 4

					verticalpixel_1 = rgb[yi + 0][xi + 0]
					# (verticalpixel_1_B, verticalpixel_1_G, verticalpixel_1_R) = verticalpixel_1

					verticalpixel_2 = rgb[yi + 2][xi + 0]
					# (verticalpixel_2_B, verticalpixel_2_G, verticalpixel_2_R) = verticalpixel_2

					# surroundings_discard_threshold=20
					# if np.all(verticalpixel_1_surrounded-verticalpixel_1<surroundings_discard_threshold):
					# 	continue

					# verticalpixel_avg=(verticalpixel[0]+verticalpixel[1]+verticalpixel[2])/3

					# verticalpixel_1_avg=np.average(rgb[yi+0][xi+0])

					'''
					# all other pixels in block
					# verticalbg+=rgb[yi+0][xi+0]
					verticalbg = rgb32[yi + 0][xi + 1]
					verticalbg += rgb32[yi + 0][xi + 2]
					verticalbg += rgb32[yi + 0][xi + 3]

					verticalbg+=rgb32[yi+1][xi+0]
					verticalbg+=rgb32[yi+1][xi+1]
					verticalbg+=rgb32[yi+1][xi+2]
					verticalbg+=rgb32[yi+1][xi+3]

					#verticalbg+=rgb[yi+0][xi+0]
					verticalbg+=rgb32[yi+2][xi+1]
					verticalbg+=rgb32[yi+2][xi+2]
					verticalbg+=rgb32[yi+2][xi+3]

					verticalbg+=rgb32[yi+3][xi+0]
					verticalbg+=rgb32[yi+3][xi+1]
					verticalbg+=rgb32[yi+3][xi+2]
					verticalbg+=rgb32[yi+3][xi+3]
					verticalbg/=4*4-2
					'''

					# all other pixels in block
					# verticalbg+=rgb[yi+0][xi+0]
					# verticalbg_avg = np.average(rgb[yi + 0][xi + 1])
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi + 0][xi + 2]))
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi + 0][xi + 3]))
					#
					# #verticalbg_avg = min(verticalbg_avg,np.average(rgb32[yi+1][xi+0]))
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+1][xi+1]))
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+1][xi+2]))
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+1][xi+3]))
					#
					# #verticalbg_avg+=rgb[yi+0][xi+0]
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+2][xi+1]))
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+2][xi+2]))
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+2][xi+3]))
					#
					# #verticalbg_avg = min(verticalbg_avg,np.average(rgb32[yi+3][xi+0]))
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+3][xi+1]))
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+3][xi+2]))
					# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+3][xi+3]))

					# block=rgb[yi:yi+4, xi+1:xi+4]
					# block=verticalline_bordering

					block_avg = np.median(np.median(verticalline_bordering, axis=0), axis=0)

					# (block_B_avg, block_G_avg, block_R_avg) = block_avg

					# verticalbg_h, verticalbg_s, verticalbg_v=cv2.cvtColor(np.array([np.array([verticalbg])]),cv2.COLOR_RGB2HSV)[0][0]

					# verticalpixel_h,verticalpixel_s,verticalpixel_v=cv2.cvtColor(np.array([np.array([verticalpixel])]),cv2.COLOR_RGB2HSV)[0][0]

					#threshold = 10 # post neat
					threshold = 8 # pre neat
					#
					# if debug:
					# 	rgb[yi + 0][xi + 0] = (0, 0, 255)

					# if np.any(block_avg - verticalpixel_1 > threshold):
					verticalpixel_1diff = np.max(block_avg - verticalpixel_1, axis=0)
					# if block_R_avg - verticalpixel_1_R > threshold or block_G_avg - verticalpixel_1_G > threshold or block_B_avg - verticalpixel_1_B > threshold:
					if verticalpixel_1diff > threshold:
						if debug:
							rgb[yi + 0][xi + 0] = (0, 255, 255)
						else:
							# rgb[yi + 0][xi + 0] = verticalpixel_1_surrounded
							# rgb[yi + 0][xi + 0] = rgb[yi - 1][xi + 0]/2 + rgb[yi + 1][xi + 0]/2
							# rgb[yi + 0][xi + 0] = rgb[yi + 0][xi - 1]/2 + rgb[yi + 0][xi + 1]/2
							rgb[yi + 0][xi + 0] = rgb[yi + 0][xi - 1] / 4 + rgb[yi + 0][xi + 1] / 4 + rgb[yi - 1][
								xi + 0] / 4 + rgb[yi + 1][xi + 0] / 4

						#pixel_2_threshold = 5 # post neat
						pixel_2_threshold = 3 # pre neat
						# if np.all(verticalpixel_2_surrounded - verticalpixel_2 > pixel_2_threshold):
						verticalpixel_2diff = np.max(block_avg - verticalpixel_2, axis=0)
						# if block_R_avg - verticalpixel_2_R > pixel_2_threshold or block_G_avg - verticalpixel_2_G > pixel_2_threshold or block_B_avg - verticalpixel_2_B > pixel_2_threshold:
						if verticalpixel_2diff > pixel_2_threshold:

							# if (np.all(np.diff([verticalpixel_1,verticalpixel_2]))<pixel_2_threshold):

							# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+1][xi+0]))
							# verticalbg_avg = min(verticalbg_avg,np.average(rgb[yi+3][xi+0]))

							# rgb[yi + 0][xi + 0] = (0, 0, 255)
							if debug:
								rgb[yi + 2][xi + 0] = (0, 255, 0)
							else:
								# rgb[yi + 2][xi + 0] = verticalpixel_2_surrounded
								# rgb[yi + 2][xi + 0] = rgb[yi + 1][xi + 0]/2 + rgb[yi + 3][xi + 0]/2
								# rgb[yi + 2][xi + 0] = rgb[yi + 2][xi + 1]/2 + rgb[yi + 2][xi - 1]/2
								rgb[yi + 2][xi + 0] = rgb[yi + 2][xi + 1] / 4 + rgb[yi + 2][xi - 1] / 4 + rgb[yi + 1][
									xi + 0] / 4 + rgb[yi + 3][xi - 0] / 4

						continue

	print(file+' -> '+str(time.time()-starttime))
	cv2.imwrite(fixedpath+"\\"+file,rgb)

filecount = 0
filelistlen=len(filelist)
timeStart = time.time()
for file in filelist:
	fixfile(file)
	filecount += 1

	if filecount % 10 == 0:
		timePassed=time.time()-timeStart
		timeStart = time.time()
		# print(timePassed)
		estTimeRemaining=(timePassed*(filelistlen-filecount))/10
		# print(estFullTime)
		msg=str(filecount) + "/" + str(len(filelist))
		# estTimeRemaining = max(0, estFullTime - timePassed)
		msg += " " + str(datetime.timedelta(seconds=estTimeRemaining)).split('.')[0] + " remaining..."
		print(msg)

# multithreaded is slower than plain sequential - cpu is not the bottleneck!
# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
# 	filecount = 0
# 	for _ in executor.map(lambda x: fixfile(x), filelist):
# 		filecount += 1
# 		if filecount % 10 == 0:
# 			timePassed = time.time() - timeStart
# 			print(timePassed)
# 			estFullTime = (timePassed * filelistlen) / filecount
# 			print(estFullTime)
# 			msg = str(filecount) + "/" + str(len(filelist))
# 			estTimeRemaining = max(0, estFullTime - timePassed)
# 			msg += " " + str(datetime.timedelta(seconds=estTimeRemaining)).split('.')[0] + " remaining..."
# 			print(msg)