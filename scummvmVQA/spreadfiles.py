import os

filelist = sorted([x for x in os.listdir(".") if x.endswith('.png') and '.vqa' in x.lower()])

for file in filelist:
	basename=file[:file.lower().index(".vqa")]
	if not os.path.exists(basename):
		os.mkdir(basename)
	if not os.path.exists(basename+"\\vqa"):
		os.mkdir(basename+"\\vqa")

	os.rename(file,basename+'\\vqa\\'+file)

print("Done.")
