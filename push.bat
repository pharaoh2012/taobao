set path=%path%;F:\git\bin;D:\soft\git\bin
cd /d %~dp0
title push to remote git
echo off
cls
echo ------------local commit
git add .
git commit -a -m "%date% %time%"


echo.
echo.

echo -------------remote commit
git push origin master 

echo %ERRORLEVEL%

rem git log --stat --since="5 minutes ago"
git log --stat -1

pause