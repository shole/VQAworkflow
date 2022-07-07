for /F "tokens=*" %%A in (vqadirs.txt) do (
	mkdir %%A\avipng
	ffmpeg -i %%A.avi %%A\avipng\%%A_avi_%%04d.png
)