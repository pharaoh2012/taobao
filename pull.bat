set path=%path%;F:\git\bin;D:\soft\git\bin
cd /d %~dp0
title pull from remote git

rem set /p input=��ȡ����Դ���룿������y:
rem if %input%==y git pull
cls
git pull

echo %errorlevel%
pause