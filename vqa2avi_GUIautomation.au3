#include <MsgBoxConstants.au3>
Opt('WinWaitDelay',100)
Opt('WinDetectHiddenText',1)
Opt('MouseCoordMode',0)

Func _WinWaitActivate($title,$text,$timeout=0)
	WinWait($title,$text,$timeout)
	If Not WinActive($title,$text) Then WinActivate($title,$text)
	;WinActivate($title,$text)
	WinWaitActive($title,$text,$timeout)
EndFunc


Local $filelist=["AR01_2", "AR01_3", "AR02_2", "AR02_3", "ASCENT_E", "AWAY01_E", "AWAY02_E", "BB01_2", "BB01_3", "BB02_2", "BB02_3", "BB03_2", "BB03_3", "BB04_2", "BB04_3", "BB05OVER", "BB05_2", "BB06OVER", "BB06_2", "BB07OVER", "BB07_2", "BB08OVER", "BB08_2", "BB09_2", "BB10OVR1", "BB10OVR2", "BB10OVR3", "BB10OVR4", "BB10OVR5", "BB10_2", "BB11_2", "BB12OVER", "BB12_2", "BB51_2", "BB51_3", "BRLOGO_E", "CT01", "CT01SPNR", "CT01_2", "CT01_3", "CT02", "CT02OVER", "CT02_2", "CT02_3", "CT03", "CT03_2", "CT03_3", "CT04", "CT04_2", "CT04_3", "CT05", "CT05OVER", "CT05_2", "CT05_3", "CT06", "CT06_2", "CT06_3", "CT07", "CT08_2", "CT08_3", "CT09_2", "CT09_3", "CT10_2", "CT10_3", "CT11_2", "CT11_3", "CT12", "CT12_2", "CT12_3", "CT51_2", "CT51_3", "DEKTRA_E", "DR01_2", "DR01_3", "DR02_2", "DR02_3", "DR03_2", "DR03_3", "DR04OVER", "DR04_2", "DR04_3", "DR05OVER", "DR05_2", "DR05_3", "DR06OVER", "DR06OVR2", "DR06_2", "DR06_3", "DSCENT_E", "END01A_E", "END01B_E", "END01C_E", "END01D_E", "END01E_E", "END01F_E", "END02_E", "END03_E", "END04A_E", "END04B_E", "END04C_E", "END04D_E", "END05_E", "END06_E", "END07_E", "ESPER", "FLYTRU_E", "HC01ESP1", "HC01ESP2", "HC01ESP3", "HC01_2", "HC01_3", "HC02ESP2", "HC02ESP3", "HC02ESP4", "HC02ESP5", "HC02_2", "HC02_3", "HC03_2", "HC03_3", "HC04_2", "HC04_3", "HF01_2", "HF01_3", "HF02_2", "HF02_3", "HF03_2", "HF03_3", "HF04_2", "HF04_3", "HF05_2", "HF05_3", "HF06_2", "HF06_3", "HF07_3", "INSD01_E", "INSD02_E", "INTRGT_E", "INTRO_E", "KIAOVER", "KIA_CLUE", "KIA_CRIM", "KIA_INGM", "KIA_SUSP", "KP01_3", "KP02_3", "KP03_3", "KP04_3", "KP05_3", "KP06ESP1", "KP06ESP2", "KP06ESP3", "KP06ESP4", "KP06_3", "KP07_3", "MA01", "MA01_2", "MA02", "MA02OVER", "MA02_2", "MA02_3", "MA04", "MA04OVER", "MA04OVR2", "MA04_2", "MA04_3", "MA05", "MA05_2", "MA05_3", "MA06", "MA06ELEV", "MA06_2", "MA06_3", "MA07", "MA07_2", "MA07_3", "MW_A_E", "MW_B01_E", "MW_B02_E", "MW_B03_E", "MW_B04_E", "MW_B05_E", "MW_C01_E", "MW_C02_E", "MW_C03_E", "MW_D_E", "NR01_2", "NR01_3", "NR02_2", "NR02_3", "NR03_2", "NR03_3", "NR04OVER", "NR04_2", "NR04_3", "NR05_2", "NR05_3", "NR06ESP1", "NR06ESP2", "NR06_2", "NR06_3", "NR07ESP1", "NR07ESP2", "NR07_2", "NR07_3", "NR08_2", "NR08_3", "NR09_2", "NR09_3", "NR10_2", "NR10_3", "NR11OVER", "NR11_2", "NR11_3", "PS01", "PS01_2", "PS02", "PS02ELEV", "PS02_2", "PS03", "PS03_2", "PS04", "PS04_2", "PS05", "PS05OVER", "PS05_2", "PS06", "PS06_2", "PS07", "PS07_2", "PS09", "PS09_2", "PS09_3", "PS10", "PS10_2", "PS11", "PS11_2", "PS12", "PS12_2", "PS13", "PS13_2", "PS14", "PS14_2", "PS14_3", "PS15", "PS15_2", "RACHEL_E", "RC01", "RC01_2", "RC01_3", "RC02", "RC02ESP1", "RC02ESP2", "RC02ESP3", "RC02ESP4", "RC02ESP5", "RC02ESP6", "RC02ESP7", "RC02_3", "RC03_2", "RC03_3", "RC04_2", "RC04_3", "RC51", "RC51_3", "SCORE", "SPINNER", "TB02_2", "TB02_3", "TB03_3", "TB05_2", "TB06ESP1", "TB06ESP2", "TB06ESP3", "TB06ESP4", "TB06_2", "TB07_2", "TB07_3", "TB_FLY_E", "TWRD01_E", "TWRD02_E", "TWRD03_E", "UG01_2", "UG01_3", "UG02_2", "UG02_3", "UG03_2", "UG03_3", "UG04_2", "UG04_3", "UG05_3", "UG06_2", "UG06_3", "UG07_3", "UG08_3", "UG09_3", "UG10_2", "UG10_3", "UG12_3", "UG13_3", "UG14OVER", "UG14_3", "UG15OVER", "UG15_3", "UG16_3", "UG17OVER", "UG17_3", "UG18OVER", "UG18OVR2", "UG18OVR3", "UG18_3", "UG19_3", "VK", "VKBOB", "VKDEKT", "VKKASH", "VKLUCY", "VKRUNC", "WSTLGO_E"]

;Local $filelist=["AR01_2"]


For $filename In $filelist	
	;If Not FileExists("D:\br_re\VQA\" & $filename & ".avi") Then ; avi
	If Not FileExists("D:\br_re\VQA\" & $filename ) Then ; pcx
		MsgBox($MB_SYSTEMMODAL, "", $filename, 1)


		_WinWaitActivate("VQA to AVI Converter written by Tim Kosse","")
		
		Sleep(100)


		;ClassnameNN:	Button6
		;Advanced (Class):	[CLASS:Button; INSTANCE:6]
		;ID:	3
		;Text:	&Open File

		; open file
		Send("&o")
		Sleep(100)

		_WinWaitActivate("Open","")

		Sleep(100)

		Send("e:\br_re\VQA\")
		Send($filename)
		Send(".vqa")
		Send("{ENTER}")

		_WinWaitActivate("VQA to AVI Converter written by Tim Kosse","")

		Sleep(100)


		;Class:	Static
		;Instance:	32
		;ClassnameNN:	Static32
		;Name:	
		;Advanced (Class):	[CLASS:Static; INSTANCE:32]
		;ID:	1019
		;Text:	0
		
		If ControlGetText ( "VQA to AVI Converter written by Tim Kosse", "", "Static32" ) == "0" Then ; .Wav, skip if no audio in VQA
			ContinueLoop
		EndIf
		

		;ClassnameNN:	Button1
		;Advanced (Class):	[CLASS:Button; INSTANCE:1]
		;ID:	1
		;Text:	&Convert

		; convert
		Send("&c")
		Sleep(100)
		Send("{DOWN}") ; AVI
		Send("{DOWN}") ; PCX
		Send("{DOWN}") ; Wav
		Sleep(100)
		Send("{ENTER}")

		;_WinWaitActivate("Enter output folder","") ; pcx
		_WinWaitActivate("Save As","") ; avi, wav

		Sleep(100)

		Send("e:\br_re\VQA\")
		Send($filename)
		Send("{ENTER}")

		Sleep(100)

		If WinActive("VQAtoAVI 2","") Then Send("{ENTER}"); pcx, ok to create dir?

		Sleep(100)

		If WinActive("VQAtoAVI 2","") Then Send("{ENTER}"); possible error msg

		While Not ControlCommand('VQA to AVI Converter written by Tim Kosse', '', 'Button6', 'IsEnabled', '')
			If WinActive("VQAtoAVI 2","") Then Send("{ENTER}") ; possible error msgs
			Sleep(500)
		WEnd

	EndIf
Next


MsgBox($MB_SYSTEMMODAL, "", "done")