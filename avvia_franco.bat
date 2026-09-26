@echo off
REM ===========================================================================
REM  F.R.A.N.C.O. 6.0 NEXUS - Launcher
REM  Doppio-click per avviare tutto FRANCO. Nessun pip install richiesto:
REM  mette src/ sul PYTHONPATH e lancia il pacchetto.
REM
REM  Flag opzionali (trascinali dopo il nome o usali da terminale):
REM    avvia_franco.bat --text-only     solo testo (niente voce/UI)
REM    avvia_franco.bat --no-voice      niente riconoscimento vocale
REM    avvia_franco.bat --no-ui         headless, niente interfaccia
REM    avvia_franco.bat --debug         log dettagliati
REM    avvia_franco.bat --theme cyber   cambia tema UI
REM ===========================================================================
setlocal enableextensions
title F.R.A.N.C.O. 6.0 NEXUS
cd /d "%~dp0"

REM --- src-layout: rende importabile "franco" senza installazione ------------
set "PYTHONPATH=%~dp0src;%PYTHONPATH%"

REM --- usa prima il runtime verificato dell'app (Python 3.12 + audio/UI) ------
set "PYEXE="
if exist "%~dp0..\.venv\Scripts\python.exe" set "PYEXE=%~dp0..\.venv\Scripts\python.exe"
where python >nul 2>nul && set "PYEXE=python"
if exist "%~dp0..\.venv\Scripts\python.exe" set "PYEXE=%~dp0..\.venv\Scripts\python.exe"
if not defined PYEXE where py >nul 2>nul && set "PYEXE=py -3.12"
if not defined PYEXE (
    echo.
    echo   [X] Python non trovato nel PATH.
    echo       Installa Python 3.10+ da https://www.python.org e riprova.
    echo.
    pause
    exit /b 1
)

echo.
echo   ========================================================
echo    F.R.A.N.C.O. 6.0 NEXUS  --  avvio in corso...
echo    interprete: %PYEXE%
echo   ========================================================
echo.

%PYEXE% -m franco %*
set "EXITCODE=%ERRORLEVEL%"

if not "%EXITCODE%"=="0" (
    echo.
    echo   [X] FRANCO e' uscito con codice %EXITCODE%.
    echo       Leggi l'errore qui sopra. Finestra lasciata aperta.
    echo.
    pause
)
endlocal
