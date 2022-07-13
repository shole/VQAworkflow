@echo off

for /F "tokens=*" %%A in (vqadirs.txt) do (
	ffmpeg -i %%A__h265.mp4 -i %%A_BIK__h265.mp4 -r 15 -filter_complex hstack  -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode "%%A_SBS_%outputpostfix%.mp4"
)