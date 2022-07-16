@echo off

for /F "tokens=*" %%A in (audiofiles.txt) do (
	del %%A.bik
)