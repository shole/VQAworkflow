@echo off

for /F "tokens=*" %%A in (vqadirs.txt) do (
	REM ffmpeg -i %%A__h265.mp4 -i %%A_BIK__h265.mp4 -r 15 -filter_complex hstack  -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode "%%A_SBS_%outputpostfix%.mp4"
	REM done1
	REM ffmpeg -framerate 15 -i %%A\neat_smoother_2x_selected\%%A.VQA_%%04d.png -i "E:\SteamLibrary\steamapps\common\Blade Runner Enhanced Edition\bik\%%A.bik" -r 15 -filter_complex hstack  -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode "%%A_SBS_%outputpostfix%_h264.mp4"
	REM done2
	REM ffmpeg -framerate 15 -i %%A\fix_less_less_mid_2x\%%A.VQA_%%04d.png -i "E:\SteamLibrary\steamapps\common\Blade Runner Enhanced Edition\bik\%%A.bik" -r 15 -filter_complex hstack  -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode "%%A_SBS_%outputpostfix%_h264.mp4"
	REM done3
	ffmpeg -framerate 15 -i %%A\fix_less_less_mid_2x_softer\%%A.VQA_%%04d.png -i "E:\SteamLibrary\steamapps\common\Blade Runner Enhanced Edition\bik\%%A.bik" -r 15 -filter_complex hstack  -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode "%%A_SBS3_%outputpostfix%_h264.mp4"
)