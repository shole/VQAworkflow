@echo off

SET sourcepath=neat_smoother_2x_selected
SET outputpostfix=

for /F "tokens=*" %%A in (vqadirs.txt) do (
	echo %%A
	ffmpeg -i %%A%outputpostfix%.bik 2>info.tmp
	type info.tmp | findstr Duration

)
