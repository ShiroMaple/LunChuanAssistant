@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo Checking Python environment...
python --version >nul 2>&1
if errorlevel 1 (
    echo Using built-in Python...
    python\python.exe -m pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn
    python\python.exe agent\main.py %*
) else (
    echo Using system Python...
    python -m pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn
    python agent\main.py %*
)

pause