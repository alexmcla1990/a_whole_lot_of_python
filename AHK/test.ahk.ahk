#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance, Force 
;~ #Persistant ; will keep code running
; alt key is ! the windows key is #, the shift key is +, and control is ^ (modifiers)
^h::
^e::Edit
^r::Reload
^m::MsgBox Hello World

^n::Run Notepad.exe
+!c::Run C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe
+!g::Run C:\Program Files\Google\Chrome\Application\chrome.exe


::cma.::cmamclaughlin@gmail.com

cmamclaughlin@gmail.com is my email address 
cma. 