#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


^P::
	MouseGetPos, LocX, LocY
	MsgBox X is at %LocX% Y is at %LocY% 


^Numpad0::
	Click, 751, 319
	Click, 1168, 370
	Click, 521, 262
	
^Numpad1::
	Click, 245, 465
	Click, 276, 468
	Click, 522, 975

^Numpad2::
	run, "C:\Program Files\Google\Chrome\Application\chrome.exe" /force-device-scale-factor=1.3 "https://www.eleadcrm.com/evo2/fresh/login.asp"
