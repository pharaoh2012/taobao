set path=%path%;F:\git\bin;D:\soft\git\bin
cd /d %~dp0
title pull from remote git

rem set /p input=获取最新源代码？请输入y:
rem if %input%==y git pull
cls
git pull

echo %errorlevel%
pause