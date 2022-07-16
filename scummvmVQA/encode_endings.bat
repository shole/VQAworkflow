@echo off

SET sourcefilelist=endings.txt
SET sourcepath=neat_smoother_2x_selected
SET sourcepathprefix=endings
SET identifier=

call :bink
REM call :raw
call :h264
call :h264_sbs
call :zip

goto loopend

:bink 
SET outputpostfix=
for /F "tokens=*" %%A in (%sourcefilelist%) do (
	echo %sourcefilelist% - %%A bink
	if not exist "%%A.bik" (
		dir /S /B /ON %sourcepathprefix%\%%A\%sourcepath%\*.png > %sourcefilelist%.lst
		REM where AR01_3\neat_smoother_2x_selected\*.png > frames.lst
		..\radtools\radvideo64 binkc %sourcefilelist%.lst /F15 /P32 %%A.bik /#
		if exist ..\VQA\%%A.wav (
			move %%A.bik %%A_noaudio.bik
			..\radtools\radvideo64 binkmix %%A_noaudio.bik ..\vqa\%%A.wav %%A.bik /L1 /#
		)
		del %sourcefilelist%.lst >NUL
	)
)
EXIT /B 0

:h264
SET outputpostfix=%identifier%_h264
for /F "tokens=*" %%A in (%sourcefilelist%) do (
	echo %sourcefilelist% - %%A h264
	if not exist "%%A%outputpostfix%.mp4" (
		if exist ..\VQA\%%A.wav (
			REM echo %%A.wav exists
			REM #ffmpeg -i "%*" -c:v libx264 -preset fast -crf 12 -x264-params mvrange=511 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart "%*_h264.mp4"
			REM ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -i ..\VQA\%%A.wav -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode  "%%A%outputpostfix%.mp4"
			ffmpeg -framerate 15 -i %sourcepathprefix%\%%A\%sourcepath%\%%A.vqa_%%04d.png -i ..\VQA\%%A.wav -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode  "%%A%outputpostfix%.mp4"
		) else (
			REM echo %%A.wav does NOT exist
			REM ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode "%%A%outputpostfix%.mp4"
			ffmpeg -framerate 15 -i %sourcepathprefix%\%%A\%sourcepath%\%%A.vqa_%%04d.png -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode "%%A%outputpostfix%.mp4"
		)
	)
)
EXIT /B 0

:h264_sbs
SET outputpostfix=%identifier%_h264
for /F "tokens=*" %%A in (%sourcefilelist%) do (
	echo %sourcefilelist% - %%A h264 sbs
	if not exist "%%A%outputpostfix%.mp4" (		
		if exist ..\VQA\%%A.wav (
			REM echo %%A.wav exists
			REM #ffmpeg -i "%*" -c:v libx264 -preset fast -crf 12 -x264-params mvrange=511 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart "%*_h264.mp4"
			REM ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -i ..\VQA\%%A.wav -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode  "%%A%outputpostfix%.mp4"
			REM ffmpeg -framerate 15 -i %sourcepathprefix%\%%A\%sourcepath%\%%A.vqa_%%04d.png -i ..\VQA\%%A.wav -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode  "%%A%outputpostfix%.mp4"
			ffmpeg -framerate 15 -i %sourcepathprefix%\%%A\%sourcepath%\%%A.vqa_%%04d.png -i "E:\SteamLibrary\steamapps\common\Blade Runner Enhanced Edition\bik\%%A.bik" -r 10 -filter_complex hstack -i ..\VQA\%%A.wav -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode "%%A_SBS%outputpostfix%.mp4"
		) else (
			REM echo %%A.wav does NOT exist
			REM ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode "%%A%outputpostfix%.mp4"
			REM ffmpeg -framerate 15 -i %sourcepathprefix%\%%A\%sourcepath%\%%A.vqa_%%04d.png -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode "%%A%outputpostfix%.mp4"
			ffmpeg -framerate 15 -i %sourcepathprefix%\%%A\%sourcepath%\%%A.vqa_%%04d.png -i "E:\SteamLibrary\steamapps\common\Blade Runner Enhanced Edition\bik\%%A.bik" -r 10 -filter_complex hstack  -c:v libx264 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -tune fastdecode "%%A_SBS%outputpostfix%.mp4"
		)
	)
)
EXIT /B 0

:raw 
SET outputpostfix=_raw
for /F "tokens=*" %%A in (%sourcefilelist%) do (
	echo %sourcefilelist% - %%A raw
	if not exist "%%A%outputpostfix%.mov" (
		if exist ..\VQA\%%A.wav (
			REM echo %%A.wav exists
			REM #ffmpeg -i "%*" -c:v libx264 -preset fast -crf 12 -x264-params mvrange=511 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart "%*_h264.mp4"
			REM ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -i ..\VQA\%%A.wav -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode  "%%A%outputpostfix%.mp4"
			ffmpeg -framerate 15 -i %sourcepathprefix%\%%A\%sourcepath%\%%A.vqa_%%04d.png -i ..\VQA\%%A.wav -c:a copy -c:v rawvideo -tune fastdecode "%%A%outputpostfix%.mov"
		) else (
			REM echo %%A.wav does NOT exist
			REM ffmpeg -framerate 15 -i %%A\%sourcepath%\%%A.vqa_%%04d.png -c:v libx265 -preset fast -crf 10 -maxrate 50M -bufsize 25M -pix_fmt yuv420p -movflags faststart -vtag hvc1 -tune fastdecode "%%A%outputpostfix%.mp4"
			ffmpeg -framerate 15 -i %sourcepathprefix%\%%A\%sourcepath%\%%A.vqa_%%04d.png -c:v rawvideo -tune fastdecode "%%A%outputpostfix%.mov"
		)
	)
)	
EXIT /B 0

:zip
SET outputpostfix=
for /F "tokens=*" %%A in (%sourcefilelist%) do (
	echo %sourcefilelist% - %%A zip
	if not exist %%A.7z (
		"c:\Program Files\7-Zip\7z.exe" a %%A.7z %sourcepathprefix%\%%A\%sourcepath%\*.png
	)
)
EXIT /B 0

:loopend
