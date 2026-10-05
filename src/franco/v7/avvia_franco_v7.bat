@echo off
REM ===========================================================================
REM  F.R.A.N.C.O. 7  --  Avvio completo in un colpo
REM  Doppio-click: apre sfera + conversazione + voce, tutto insieme.
REM  Nessuna installazione richiesta: mette src/ sul PYTHONPATH e lancia la UI.
REM ===========================================================================
setlocal enableextensions
title F.R.A.N.C.O. 7
cd /d "%~dp0"

REM --- src-layout: rende importabile "franco" senza installazione ------------
set "PYTHONPATH=%~dp0..\..;%PYTHONPATH%"
set "FRANCO_ROOT=%~dp0..\..\..\.."
set "PYEXE="

REM --- 1) runtime verificato dell'app (Python 3.12 + audio/UI) --------------
if exist "%FRANCO_ROOT%\.venv\Scripts\python.exe" set "PYEXE=%FRANCO_ROOT%\.venv\Scripts\python.exe"
if defined PYEXE goto run

REM --- 2) fallback: python del PATH -----------------------------------------
where python >nul 2>nul && set "PYEXE=python"
if not defined PYEXE where py >nul 2>nul && set "PYEXE=py -3.12"
if not defined PYEXE (
    echo.
    echo   [X] Python non trovato. Installa Python 3.10+ e riprova.
    echo.
    pause
    exit /b 1
)

:run
echo.
echo   ========================================================
echo    F.R.A.N.C.O. 7  --  avvio completo in corso...
echo    interprete: %PYEXE%
echo   ========================================================
echo.

%PYEXE% -c "from franco.v7.services import build_runtime; from franco.v7.desktop_ui import run_desktop; import sys; sys.exit(run_desktop(build_runtime()))"
set "EXITCODE=%ERRORLEVEL%"

if not "%EXITCODE%"=="0" (
    echo.
    echo   [X] FRANCO V7 e' uscito con codice %EXITCODE%.
    echo       Leggi l'errore qui sopra. Finestra lasciata aperta.
    echo.
    pause
)
endlocal
