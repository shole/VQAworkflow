@echo off

SET sourcepath=neat_smoother_2x_selected
SET outputpostfix=_h264

for /F "tokens=*" %%A in (endings.txt) do (
	echo %%A

	dir /S /B /ON endings\%%A\%sourcepath%\*.png > endingsframes.lst
	REM where AR01_3\neat_smoother_2x_selected\*.png > frames.lst
	..\radtools\radvideo64 binkc endingsframes.lst /F15 /P32 %%A.bik /#
	
	if exist ..\VQA\%%A.wav (
		REM echo %%A.wav exists
		REM #ffmpeg -i "%*" -c:v libx264 -preset fast -crf 12 -x264-params mvrange=511 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart "%*_h264.mp4"
		REM ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -i ..\VQA\%%A.wav -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode  "%%A%outputpostfix%.mp4"
		REM ffmpeg -framerate 15 -i endings\%%A\%sourcepath%\%%A.vqa_%%04d.png -i ..\VQA\%%A.wav -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode  "%%A%outputpostfix%.mp4"
		
		move %%A.bik %%A_noaudio.bik
		..\radtools\radvideo64 binkmix %%A_noaudio.bik ..\vqa\%%A.wav %%A.bik /L4 /F15 /#
	
	) else (
		REM echo %%A.wav does NOT exist
		REM ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode "%%A%outputpostfix%.mp4"
		REM ffmpeg -framerate 15 -i endings\%%A\%sourcepath%\%%A.vqa_%%04d.png -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode "%%A%outputpostfix%.mp4"
	)
)
del endingsframes.lst