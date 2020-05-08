@echo off
pushd %~dp0
python checker.py %1
popd
