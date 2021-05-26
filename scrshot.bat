@echo off
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png C:\users\%username%\desktop
adb shell rm /sdcard/screen.png
echo finished
pause