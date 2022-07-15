@echo off

for /F "tokens=*" %%A in (vqadirs.txt) do (
	mkdir %%A\bink
	ffmpeg -i "E:\SteamLibrary\steamapps\common\Blade Runner Enhanced Edition\bik\%%A.bik" %%A\bink\%%A_bik_%%06d.png
)