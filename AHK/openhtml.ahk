#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
; alt key is ! the windows key is #, the shift key is +, and control is ^ (modifiers)
^Numpad4::
	Clipboard = 
	Send ^c

	ClipWait ;waits for the clipboard to have content

	Run, C:\Users\Charles\AppData\Local\Programs\Microsoft VS Code\Code.exe `"%clipboard%`"