@echo on
chcp 65001
setlocal EnableDelayedExpansion
cls

echo =============================
echo        ╖ ] / .   
echo     ╖╜╜  ╜╙╙Ü,,    
echo    ▒        `╙╖─   
echo  .╓[  ,,     ─▒╜`     FPA
echo   ─`j░░░░.   ~▒`      tool
echo   ' ░░░░░░   └ `  
echo     ░▐████░       
echo      ░░▓▓▓N           @fekko
echo ============================
echo.
echo.
echo.


set "commands="
for /f "delims=" %%a in (commands.txt) do (
    set "commands=!commands!%%a"
)

:main_loop
set /P "fpa_command=%ComputerName%/$ "
if %fpa_command% == "" (
    echo Приложение не работает с данными получеными от пользователя
    goto main_loop
)

set temp=%commands%
:parse_loop
if not defined !temp!(
    echo Error
    goto main_loop
)
set found="False"
for /f "delims=;" %%i in ("%temp%") do (
    if %fpa_command% == %%i (
        set found="True"
    )
    set "temp=!temp:*;=!"

)

:result
if %found% == "True" (
    echo Good
    goto main_loop
) else (
    goto parse_loop
)