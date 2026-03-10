@echo off

REM 현재 디렉토리 기준으로 PYTHONPATH 설정
set PYTHONPATH=%CD%\package;%CD%\sim2real;%PYTHONPATH%

REM 실행
python sim2real\run.py
