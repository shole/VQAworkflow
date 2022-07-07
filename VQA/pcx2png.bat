for /F "tokens=*" %%A in (vqadirs.txt) do (
	mkdir %%A\png
	ffmpeg -i %%A\%%04d.pcx %%A\png\%%A_%%04d.png
	#del %%A\*.pcx
)