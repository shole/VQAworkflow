import os
import pickle
import shutil


f = open('vqa2seq.pickle','rb')

framecorrespondence=pickle.load(f)

zeropadnumbers=8
seqprefix="neat2x_sm_sel_"
seqpath="neat_smoother_2x_selected"
targetsubfolder="neat_smoother_2x_selected"

# (vqafile, file, framecounter, sequencename, pathfilecounter)

filesMissing=False

# for (vqafile, file, framecounter, sequencename, pathfilecounter) in framecorrespondence:
for (vqafile, file, framecounter, sequencename) in framecorrespondence:

	sourcefilename=seqpath+'\\'+seqprefix+str(framecounter+1).zfill(zeropadnumbers)+".png"

	if not os.path.exists(sourcefilename):
		print("file missing: "+sourcefilename)
		filesMissing=True
		continue

if filesMissing:
	print("Files were missing! :O")
	exit()

lastVqa=""
# for (vqafile, file, framecounter, sequencename, pathfilecounter) in framecorrespondence:
for (vqafile, file, framecounter, sequencename) in framecorrespondence:

	if vqafile!=lastVqa:
		print(vqafile)
		lastVqa=vqafile

	sourcefilename=seqpath+'\\'+seqprefix+str(framecounter+1).zfill(zeropadnumbers)+".png"

	if not os.path.exists(sourcefilename):
		print("file missing: "+sourcefilename)
		continue

	targetpath = vqafile + '\\' + targetsubfolder

	if not os.path.exists(targetpath):
		os.mkdir(targetpath)

	shutil.copy(sourcefilename,targetpath+'\\'+file)
	# os.rename(sourcefilename,targetpath+'\\'+file)



print("Done.")
