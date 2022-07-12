#import imageio
import os
extensions=[
    ".png",
    ".jpg",
    ".exr",
]

filelist = sorted([x for x in os.listdir(".") if x.lower()[-4:] in extensions])
extension=filelist[0][-4:]
basename=filelist[0][:-4]

for i in range(len(basename)):
    if not basename[len(basename)-1].isdigit():
        break
    basename=basename[:-1]

print("base filename: "+basename)

filelist = sorted([x for x in filelist if x.endswith(extension) and x.startswith(basename)])

indexedfilename = basename + str(0).zfill(6) + extension
# os.rename(file,indexedfilename)
print(filelist[0] + " -> " + indexedfilename)

for fileidx in range(len(filelist)):
    file=filelist[fileidx]
    indexedfilename=basename+str(fileidx).zfill(6)+extension
    os.rename(file,indexedfilename)
    # print(file + " -> "+ indexedfilename)

print("Done.")