import os
import pickle
import shutil


f = open('vqa2seq.pickle','rb')

framecorrespondence=pickle.load(f)

filetype=".png"

# zeropadnumbers=8
zeropadnumbers=6
# seqprefix="less_lessmid_"
seqprefix=""
seqpath="vqasequence\\linefix\\less_lessmid_lessmid_00000000_scale_2x_prob-3_png_softer"
# seqprefix="endings_seq_"
# seqpath="endings_selected"
targetsubfolder="fix_less_less_mid_2x_softer"

# (vqafile, file, framecounter, sequencename, pathfilecounter)

filesMissing=False

zerooffset=0

if not os.path.exists(seqpath+'\\'+seqprefix+str(0).zfill(zeropadnumbers)+filetype):
	print("1-"+str(len(framecorrespondence)))
	zerooffset=1
else:
	print("0-"+str(len(framecorrespondence)-1))


# for (vqafile, file, framecounter, sequencename, pathfilecounter) in framecorrespondence:
for (vqafile, file, framecounter, sequencename) in framecorrespondence:

	sourcefilename=seqpath+'\\'+seqprefix+str(framecounter+zerooffset).zfill(zeropadnumbers)+filetype

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

	sourcefilename=seqpath+'\\'+seqprefix+str(framecounter+zerooffset).zfill(zeropadnumbers)+filetype

	if not os.path.exists(sourcefilename):
		print("file missing: "+sourcefilename)
		continue

	targetpath = vqafile + '\\' + targetsubfolder

	if not os.path.exists(targetpath):
		os.mkdir(targetpath)

	shutil.copy(sourcefilename,targetpath+'\\'+file)
	# os.rename(sourcefilename,targetpath+'\\'+file)



print("Done.")
