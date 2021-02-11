@echo off
:: This program just displays Hello World
set message = Starting Mamphi Study Web Application
echo %message%

cd "mamphi-flask/"

rem echo "Starting Web Client"

START dist/mamphiflaskify/mamphiflaskify.exe

cd "../mamphi-api/api"

START dist/mamphiApi/mamphiApi.exe

REM ECHO "REST-API running at 127.0.0.1:5000"