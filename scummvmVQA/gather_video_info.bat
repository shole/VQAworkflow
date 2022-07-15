@echo off

SET sourcepath=neat_smoother_2x_selected
SET outputpostfix=__h265

for /F "tokens=*" %%A in (vqadirs.txt) do (
	echo %%A
	ffmpeg -i %%A%outputpostfix%.mp4 2>info.tmp
	type info.tmp | findstr Duration

)
