@echo off

SET sourcepath=fix_less_less_mid_2x_softer
SET outputpostfix=_h264

for /F "tokens=*" %%A in (done3.txt) do (
	if exist ..\VQA\%%A.wav (
		REM echo %%A.wav exists
		REM #ffmpeg -i "%*" -c:v libx264 -preset fast -crf 12 -x264-params mvrange=511 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart "%*_h264.mp4"
		REM ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -i ..\VQA\%%A.wav -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode  "%%A%outputpostfix%.mp4"
		ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -i ..\VQA\%%A.wav -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode  "%%A%outputpostfix%.mp4"
	) else (
		REM echo %%A.wav does NOT exist
		REM ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode "%%A%outputpostfix%.mp4"
		ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode "%%A%outputpostfix%.mp4"
		rem file doesn't exist
	)
)