color 0d
@echo off
echo Creating virtual environment if it does not exist...
if not exist textadventureenv (
    python -m venv textadventureenv
)

echo Activating virtual environment...
call textadventureenv\Scripts\activate

echo Checking necessary Python packages...

REM List of required Python packages
set packages=pygame colorama

REM Check if each package is installed
for %%i in (%packages%) do (
    pip show %%i >nul 2>&1
    if errorlevel 1 (
        echo Installing %%i...
        pip install %%i
    ) else (
        echo %%i is already installed.
    )
)

echo Starting the game...
python main_game.py
